<!-- Header -->
<p align="center">
   <a href="https://basedosdados.org">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="/docs/images/logo1_mides_white.png">
      <source media="(prefers-color-scheme: light)" srcset="/docs/images/logo1_mides_black.png">
      <img src="/docs/images/logo1_mides_white.png" width="340" alt="MiDES">
  </picture>
  </a>
</p>

<p align="center">
    <em>Microdados de Despesas de Entes Subnacionais.</em>
</p>

# Index

- [Detalhes](#detalhes)
- [Logica do Site](#logica-do-site)
- [Raspador](#raspador)
  - [Constante](#constante)
  - [Verificar IP](#verificar-ip)
  - [Importação](#importação)
  - [Extrair](#extrair)
  - [Registrar ID municipios e Entidades](#registrar-id-municipios-e-entidades)
  - [Raspagem](#raspagem)
  - [Verificar dados perdidos](#verificar-dados-perdidos)
  - [Mandar para o drive Manualmente](#mandar-para-o-drive-manualmente)
 
    
# Detalhes
Categoria|Detalhe|
|:-:|:-:|
Bandeira|<img src="/docs/images/flags/to.png" width=50>
Nome|Tocantins
Sigla| TO
Municípios| 139
Cobertura do Raspador| 2013 - 2024
Link Site| [:link:][link-site]
Pipeline|✓
Sistema| GET
Server|Sem registros de Quedas
Ip Estrageiro|✓
Link Drive|[:link:][link-drive]
Link Storage|[:link:][link-storage]
Link Licitação|X

# [Logica do Site][link-site]

  Site de Tocantins utiliza de `GET`s para chegar ao download do `.xls` que guarda empenhos, liquidaçoes, e pagamentos

# [Raspador][raspador]

  Para a raspagem ser realizada é preciso de um arquivo de mapeamento das entidades que é gerado na sessão [registrar ID municipios e entidades][registrar-ids].
  Esse diretorios já tem gerado esse [mapeamento][csv] por padrão, mas caso seja necessario pode ser realizado a criação dele novamente utilizado os codigos em [registrair][registrar-ids].
  Depois de escolheremos o ano desejado para raspagem em [constantes][constante] podemos iniciar a [raspagem][raspagem].
  Caso definido um caminho para o salvamento no drive em [constantes][constante]. Podemos utilizar do auto-salvamento colocado no codigo de [raspagem][raspagem] ou mandar manualmente    em [Mandar para o drive][mandar-drive].
  
  *Apesar do dado extraido ser um `.xls` na verdade ele é um table html.*
  
  *Codigo pega dados de todas a entidades, porém apenas a primeira entidade de cada ano e municipio e necessario. Porque eles disponibilizam o dado de todas as entidades no mesmo arquivos. (foi descoberto no tratamento do dado)*
 
## [Constante][constante]
  
  Nessa sessão controlamos qual ano será raspado, definimos o caminho para o csv que se encontra as entidades e caminho para salvar e extrair arquivos raspados.
  Exemplo da sessão em codigo ⬇️:
   ```py
    ano = 2018
    csv_entidade_git = "https://raw.githubusercontent.com/Winzen/mides-rascunho/main/code/scraping/to/municipios-entidades/entidades_to.csv?      token=GHSAT0AAAAAACJFESHXRUQPOWT6TB5XH3QSZTQ44KQ"
    path_drive_input = None # Definir caso você queira salvar os arquivos em algum lugar automaticamente ou extrair eles
   ```
## [Verificar IP][verificar-ip]

  Aqui verificamos o IP que o colab está utilizando na sessão. Caso o IP não for de alguma das americas é recondado que reinicei sessão até um IP das americas seja provido.
  
  Exemplo da sessão em codigo ⬇️:
   ```py
    import requests
    
    my_country = requests.get("https://api.myip.com/")
    my_country.json()
   ```
## [Importação][importação]
  Grupo responsavel por ativar todas as funçoes e bibliotecas necessarias para as de mais celulas do notebook.
## [Extrair][extrair]
  Sessão responsavel por extrair possiveis dados já salvos do caminhos definido em [constantes][constante].
## [Registrar ID municipios e Entidades][registrar-ids]
  Sessão responsavel por gerar um csv de mapeamente do site. Esse csv é utilizado futuralmente para a raspagem dos dados.
  
  *Leva aproximadamente 23 minutos para ser completado*

   Exemplo da sessão em codigo ⬇️:
   ```py
http = PoolManager(maxsize=139, cert_reqs='CERT_NONE', block=True)
disable_warnings(exceptions.InsecureRequestWarning)

link = "https://portaldocidadao.tce.to.gov.br/estadomunicipios/index"
response = http.request('GET', link)

txt_html = response.data
soup = BeautifulSoup(txt_html, 'html.parser')

elementos_municipios = soup.select('select[name="comboMunicipio"] option')[1:]
anos = soup.select('select[name="comboExercicio"] option')[1:]
anos = [ano.get("value") for ano in anos]

dataframe = {elemento.text: elemento.get("value") for elemento in elementos_municipios}

entidades = []
for ano in anos:
    with concurrent.futures.ThreadPoolExecutor() as executor:
      entidades += [entidades_json
                    for entidades_json in
                    executor.map(
                    lambda id_municipio: form_link_entidade(http, id_municipio, ano),
                    dataframe.values()
                    )]


entidades_to_df = [entidade for entidades_list in entidades for entidade in entidades_list]
df_entindade = pd.DataFrame(entidades_to_df, dtype=str)
df_entindade.columns = df_entindade.columns.str.lower()
df_entindade.to_csv("entidades_to.csv", index=False)
   ```
## [Raspagem][raspagem]

  Sessão responsavel pela raspagem de dados do site. Apartir do csv com as entidades coletadas do site podemos conseguir forma links que nos leva diretamente para o download dos dados    alvos de Empenho.xls, Liquidação.xls e Pagamento.xls de cada entidade registrada no csv.

  Exemplo da sessão em codigo ⬇️:
   ```py
entidades = pd.read_csv(csv_entidade_git, dtype=str)

chucksize = 30

entidade_ano_coleta = entidades[entidades.ano == str(ano)]
categorias = ["empenho", "liquidacao", "pagamento"]
linha_coleta = [form_link_to_data(entidade, categoria)
                for entidade in entidade_ano_coleta.itertuples()
                for categoria in categorias]

chunks = list(batched(linha_coleta, chucksize))

for n, chunk in enumerate(chunks):

  try:

    start_time = time.time()
    print(f"Chunk: {n+1}/{len(chunks)} Iniciado\n")

    rows_to_extract = [row for row in chunk if verify_exists(row)]

    if rows_to_extract:

      with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_dado, rows_to_extract)

      if (n + 1) % 2 == 0:
        send_solo_drive()

      sleep(1)

    print(f"Duração da execução: {(time.time() - start_time) / 60:.2f}\n{'-' * 30}")


  except Exception as erro:
    print(f"Erro: {erro}\nFalha chunk {n+1}")
    sleep(10)


send_solo_drive()

   ```

## [Verificar dados perdidos][verificar-dados]
Sessão responsavel pela verificação dos dados que podem está sendo perdidos.
Fazemos uma verificação entre os dados raspados e os registros de entidades para encontrar dados que não foram raspados com sucesso ou ainda estão na fila de raspagem.
Podemos fazer uma verificação manual dos links que aparecem como não coletados caso necessario.

Exemplo da sessão em codigo ⬇️:

```py
path = f"/content/input/{ano}/**/**/*"
files = glob.glob(path)

ids_entidades_coletados = [path.split("/")[-2] for path in files]
ids_entidades_coletados = list(dict.fromkeys(ids_entidades_coletados))

mask = ~entidade_ano_coleta.id.isin(ids_entidades_coletados)
nao_coletados = entidade_ano_coleta[mask]

categorias = ["empenho", "liquidacao", "pagamento"]
nao_coletados = [form_link_to_data(entidade, categoria)
                for entidade in nao_coletados.itertuples()
                for categoria in categorias]

for row in nao_coletados:
  print(row.link)
```
## [Mandar para o drive Manualmente][mandar-drive]

Sessão responsavel por salvar os dados coletados para o google drive caso seja necessario.
Para utilizar dessa sessão é preciso preencher um caminho de salvamento em [constantes][constante].
Também verificar se foi gerado a conexão com o google drive ao ponto do notebook.

Exemplo da sessão em codigo ⬇️:

```py
drive.mount('/content/drive')


send_folder_drive(path_drive_input,
                f"/content/input/")
```

<!-- Referencias -->

[link-site]: https://portaldocidadao.tce.to.gov.br/estadomunicipios/index
[link-drive]: https://drive.google.com/drive/u/0/folders/1iYI1BUNfKa7C82drQvAlg23KHxF8NqWN
[link-storage]: https://console.cloud.google.com/storage/browser/basedosdados-dev/staging/world_wb_mides/raw_empenho_to?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&cloudshell=false&project=basedosdados-dev
[link-licitacao]: ...

[csv]: https://raw.githubusercontent.com/Winzen/mides-rascunho/main/code/scraping/to/municipios-entidades/entidades_to.csv?token=GHSAT0AAAAAACJFESHXRUQPOWT6TB5XH3QSZTQ44KQ

[raspador]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/to/%5Bto%5Dextrair.ipynb#scrollTo=FWmN7s8nVVEt
[constante]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/to/%5Bto%5Dextrair.ipynb#scrollTo=nFe35mrJ5Ctw
[verificar-ip]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/to/%5Bto%5Dextrair.ipynb#scrollTo=9ptCC5xP2ssI
[importação]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/to/%5Bto%5Dextrair.ipynb#scrollTo=mDgDiOXa_Uvg
[extrair]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/to/%5Bto%5Dextrair.ipynb#scrollTo=LTg1yuSe8InA
[registrar-ids]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/to/%5Bto%5Dextrair.ipynb#scrollTo=TzXgMBVbE5YV
[raspagem]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/to/%5Bto%5Dextrair.ipynb#scrollTo=mXLbK80QWH70
[verificar-dados]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/to/%5Bto%5Dextrair.ipynb#scrollTo=FTalgJh47E3y
[mandar-drive]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/to/%5Bto%5Dextrair.ipynb#scrollTo=O2IugeRyWweY
