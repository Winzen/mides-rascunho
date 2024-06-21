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

# Detalhes
Categoria|Detalhe|
|:-:|:-:|
Bandeira|<img src="/docs/images/flags/se.png" width=50>
Nome|Sergipe
Sigla| SE
Municípios| 75
Cobertura do Raspador| 2008 - 2016
Link_Site| [:link:](https://www.tcese.tc.br/portaldatransparencia/Default.aspx)
Pipeline|X
Sistema| ASP.NET
Server|Sem registros de Quedas
Ip_estrageiro|✓
Link_drive|[:link:](https://drive.google.com/drive/u/0/folders/1-3MIVVXrPobqvSfuQCJ1ylW3xxAx2Zwx)
Link_storage|X
Link_licitacao|X

# Logica do Site

Site de Sergipe utiliza de [ASP.NET](https://help.qlik.com/en-US/sense-developer/May2024/Subsystems/EngineJSONAPI/Content/introduction.htm).

Um sistema onde podemos manipular uma sessão com sequencia de `POST`s. Apenas respeitando que o `POST`s apenas simule interação com coisas que se encontram na pagina gerada no back-end do servidor.

# [Raspador][raspador]

  Raspadores de Sergipe é divido em três notebooks [[se]extrair.ipynb][extrair], [[se]extrair_mapeamento.ipynb][extrair-mapeamento] e [[se]mapear_empenho.ipynb][mapear].
  - [[se]extrair.ipynb][extrair] é responsavel por completar a extração dos empenhos depois do mapeamento estiver pronto
  - [[se]extrair_mapeamento.ipynb][extrair-mapeamento] é responsavel por extrair as paginas de empenhos para pode gerar o mapeamento.
  - [[se]mapear_empenho.ipynb][mapear] forma o mapeamento dos empenhos e divide eles por ano. 

   Para mais informaçoes do funcionamento de [[se]extrair_mapeamento.ipynb][extrair-mapeamento] e [[se]mapear_empenho.ipynb][mapear].
   
   Acesse suas documentaçoes: [doc-[se]extrair_mapeamento.ipynb][doc-mapeamento] e [doc-[se]mapear_empenho.ipynb][doc-mapeamento]
 
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

## [Raspagem][raspagem]

  Sessão responsavel pela raspagem de dados do site. Apartir do csv com as entidades coletadas do site podemos conseguir forma links que nos leva diretamente para o empenhos.
  
  Exemplo da sessão em codigo ⬇️:
   ```py
para_coletar = df[df["coletado"] == "False"]

chunks = make_list_chunks(para_coletar.itertuples(), 60)
disable_warnings(exceptions.InsecureRequestWarning)

for n, rows in enumerate(chunks):

  print(f"{'-' * 30}\nIniciando extração: {n + 1}/{len(chunks)}")
  start_time = time.time()

  with concurrent.futures.ThreadPoolExecutor() as executor:
    tasks = [task for task in executor.map(extrair, rows)]
    tasks_done = [task.Index for task in tasks if task]

  df.loc[tasks_done, "coletado"] = "True"

  print(f"De {len(rows)} paginas, foram coletadas {len(tasks_done)} com sucesso")

  segundo_execucao = time.time() - start_time

  print(f"Duração da execução: {segundo_execucao / 60:.2f}\n{'-' * 30}")
  print(f"Intervalo\nRespeito de {segundo_execucao * 0.2: 0.2f} segudos ao servidor")

  sleep(segundo_execucao * 0.2)

  if (n + 1) % 40 == 0:
    print("Salvando..")
    df.to_csv(csv_coleta_name, index=False)
    send_solo_drive()
    print("Salvamento concluido.")

print("Salvando..")
df.to_csv(csv_coleta_name, index=False)
send_solo_drive()
print("Salvamento concluido.")
   ```

## [Verificar dados perdidos][verificar-dados]
Sessão responsavel pela verificação dos dados que podem está sendo perdidos.
Fazemos uma verificação entre os dados raspados e os registros de entidades para encontrar dados que não foram raspados com sucesso ou ainda estão na fila de raspagem.
Podemos fazer uma verificação manual dos links que aparecem como não coletados caso necessario.

Exemplo da sessão em codigo ⬇️:

```py
path_csvs = "/content/input/**/**/**/*.html"
htmls = glob.glob(path_csvs)
htmls = list(dict.fromkeys(htmls))
registrados = df[df["coletado"] == "True"].shape[0]
print(len(htmls) == registrados)
print(f"Valores nesse momento são coletado {len(htmls)} e registrados {registrados}")
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

[extrair]: https://github.com/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair.ipynb
[extrair-mapeamento]: https://github.com/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair_mapeamento.ipynb
[mapear]: https://github.com/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dmapear_empenho.ipynb

[doc-mapeamento]: https://github.com/Winzen/mides-rascunho/blob/main/code/scraping/se/docs-se/%5Bse%5Dextrair_mapeamento.md

[raspador]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair.ipynb#scrollTo=CpVNwZaGLZd0
[constante]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair.ipynb#scrollTo=iuLdqHBy_3co
[verificar-ip]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair.ipynb#scrollTo=9ptCC5xP2ssI
[importação]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair.ipynb#scrollTo=_VXXXORnNegL
[extrair]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair.ipynb#scrollTo=TTb_aULe8FOB
[raspagem]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair.ipynb#scrollTo=_3EoBWtuPvIL
[verificar-dados]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/to/%5Bto%5Dextrair.ipynb#scrollTo=FTalgJh47E3y
[mandar-drive]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair.ipynb#scrollTo=98_15dAlHvyk
