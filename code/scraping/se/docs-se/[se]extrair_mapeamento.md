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

- [Raspador](#raspador)
  - [Constante](#constante)
  - [Verificar IP](#verificar-ip)
  - [Importação](#importação)
  - [Extrair](#extrair)
  - [Formar DataFrame das entidades](#formar-dataframe-das-entidades)
  - [Extrair Paginas de coleta Mapeamento](#extrair-paginas-de-coleta-mapeamento)
  - [Mandar para o drive Manualmente](#mandar-para-o-drive-manualmente)
 
# [Raspador][raspador]

Raspador é utilizado para extrair as paginas que contem as informaçoes basicas de empenhos. Com elas podemos forma o link para acessar os empenhos detalhos com mais velocidade.
   
## [Constante][constante]
  
  Nessa sessão controlamos qual ano será raspado, definimos o caminho para o csv que se encontra as entidades e caminho para salvar e extrair arquivos raspados.
  Exemplo da sessão em codigo ⬇️:
   ```py
   path_drive_input = None # Definir caminho para salver as paginas do mapeamento
   path_drive_csv = None # Definir caminho para salver o csv das entidades
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
## [Formar DataFrame das entidades][dataframe]
  Sessão responsavel por gerar um csv com todas as entidades disponiveis para coleta.
  
  *Leva aproximadamente 23 minutos para ser completado*

   Exemplo da sessão em codigo ⬇️:
   ```py
link_confirmar_unidade = "https://www.tcese.tc.br/portaldatransparencia/Default.aspx"
link_acesse_inicio_dados = "https://www.tcese.tc.br/portaldatransparencia/DadosUnidade.aspx"


headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
  "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
  "Content-Type": "application/x-www-form-urlencoded",
  "Connection": "keep-alive"
}

rows = []

anos, municipios = get_anos_municipios()

for municipio in municipios:
  for ano in anos:
    with requests.Session() as s:

      inicial_response = s.get(link_confirmar_unidade, headers=headers)
      soup_inicial = BeautifulSoup(inicial_response.text)
      select_ano = form_data_post_ano(soup_inicial, ano, municipio, "ctl00$ContentPlaceHolder1$ddlAno")

      response_ano = s.post(link_confirmar_unidade, headers=headers, data=select_ano)
      soup_ano = BeautifulSoup(response_ano.text)
      select_municipio = form_data_post_municipio(soup_ano, ano, municipio, "ctl00$ContentPlaceHolder1$ddlMunicipios")
      response_municipio = s.post(link_confirmar_unidade, headers=headers, data=select_municipio)

      soup_municipio = BeautifulSoup(response_municipio.text)

      select_unidade = "select#ctl00_ContentPlaceHolder1_ddlUnidadeGestora option"
      element_unidades = soup_municipio.select(select_unidade)
      unidades = [form_row_entidades(municipio, unidade.text, unidade.get("value"), ano) for unidade in element_unidades]
      rows += unidades

df = pd.DataFrame(rows)
df["coletado"] = "False"
os.makedirs("csvs", exist_ok=True)
df.to_csv("csvs/entidades.csv", index=False)
   ```
## [Extrair Paginas de coleta Mapeamento][mapeamento]

  Sessão responsavel pela raspagem das paginas que contém os empenhos do site. 

  Exemplo da sessão em codigo ⬇️:
   ```py
df_entidades = pd.read_csv("/content/csvs/entidades.csv", dtype=str)
para_coletar = df_entidades[df_entidades["coletado"] == "False"]

for n, row in enumerate(para_coletar.itertuples()):

  coletado = coletar_paginas_empenho(row.municipio, row.ano, row.id_entidade)

  if coletado:
    df_entidades.loc[row.Index, "coletado"] = "True"

  if (n + 1) % 5 == 0:
    print("Salvando..")
    df_entidades.to_csv("/content/csvs/entidades.csv", index=False)
    send_solo_drive()
    print("Salvamento concluido.")


print("Salvando..")
df_entidades.to_csv("/content/csvs/entidades.csv", index=False)
send_solo_drive()
print("Salvamento concluido.")

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

[raspador]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair_mapeamento.ipynb#scrollTo=9ptCC5xP2ssI
[constante]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair_mapeamento.ipynb#scrollTo=MT-Xd5hN1rhu
[verificar-ip]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair_mapeamento.ipynb#scrollTo=9ptCC5xP2ssI
[importação]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair_mapeamento.ipynb#scrollTo=6hVL9mJ1fcnq
[extrair]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair_mapeamento.ipynb#scrollTo=3PaPn6j88Y0h
[dataframe]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair_mapeamento.ipynb#scrollTo=OKrN3wgQsfPj
[mapeamento]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair_mapeamento.ipynb#scrollTo=ScKZU3fxzQvL
[mandar-drive]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair_mapeamento.ipynb#scrollTo=98_15dAlHvyk
