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
  - [Verificar IP](#verificar-ip)
  - [Importação](#importação)
  - [Pegar Municipios Id e Entidades](#pegar-municipios-id-e-entidades)
  - [Pegar links dos ZIPs](#pegar-links-dos-zips)
  - [Download dos Zips](#download-dos-zips)
  - [Manda para o Drive](#manda-para-o-drive)

# Detalhes
Categoria|Detalhe|
|:-:|:-:|
Bandeira|<img src="/docs/images/flags/ro.png" width=50>
Nome|Rondônia
Sigla| RO
Municípios| 52
Cobertura do Raspador| 2019 - 2020
Link Site| [:link:](https://transparencia.tce.ro.gov.br/transparenciatce/Remessa/Pesquisar)
Pipeline|X
Sistema| POST
Server|Sem Registros de Quedas
Ip estrageiro|✓
Link drive|[:link:](https://drive.google.com/drive/u/0/folders/1-ZkJqL6VfGOHua9A0Yca7C5t5XGYM87O)
Link storage|[:link:](https://console.cloud.google.com/storage/browser/basedosdados-dev/staging/world_wb_mides/raw_empenho_ro?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&cloudshell=false&project=basedosdados-dev)
Link_licitacao|X

# Logica do Site

No Site de Rondônia foi utilizados de `POST`s para conseguir chegar ao link direto dos ZIPs.

Infelizmente, os unicos dados disponveis são 2019 e 2020.

Após a coleta de todos os links de download dos zips.
È feito o download e armazenamento dos mesmo.

# [Raspador][raspador]

  Raspadores de Sergipe é divido em três notebooks [[se]extrair.ipynb][extrair], [[se]extrair_mapeamento.ipynb][extrair-mapeamento] e [[se]mapear_empenho.ipynb][mapear].
  - [[se]extrair.ipynb][extrair] é responsavel por completar a extração dos empenhos depois do mapeamento estiver pronto
  - [[se]extrair_mapeamento.ipynb][extrair-mapeamento] é responsavel por extrair as paginas de empenhos para pode gerar o mapeamento.
  - [[se]mapear_empenho.ipynb][mapear] forma o mapeamento dos empenhos e divide eles por ano. 

   Para mais informaçoes do funcionamento de [[se]extrair_mapeamento.ipynb][extrair-mapeamento] e [[se]mapear_empenho.ipynb][mapear].
   
   Acesse suas documentaçoes: [doc-[se]extrair_mapeamento.ipynb][doc-mapeamento] e [doc-[se]mapear_empenho.ipynb][doc-mapear]

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

## [Pegar Municipios Id e Entidades][pegar-municipios]
  Sessão responsavel por extrair possiveis dados já salvos do caminhos definido em [constantes][constante].

## [Pegar links dos ZIPs][pegar-links]

  Sessão responsavel pela raspagem de dados do site. Apartir do csv com as entidades coletadas do site podemos conseguir forma links que nos leva diretamente para o empenhos.
  
  Exemplo da sessão em codigo ⬇️:
   ```py
   ```

## [Download dos Zips][download]
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
## [Manda para o Drive][mandar-drive]

Sessão responsavel por salvar os dados coletados para o google drive caso seja necessario.
Para utilizar dessa sessão é preciso preencher um caminho de salvamento em [constantes][constante].
Também verificar se foi gerado a conexão com o google drive ao ponto do notebook.

Exemplo da sessão em codigo ⬇️:

```py
drive.mount('/content/drive')

df.to_csv(csv_coleta_name, index=False)

send_folder_drive(path_drive_input,
                "/content/input/")

send_folder_drive(path_drive_csv,
                "/content/csvs")
```

<!-- Referencias -->

[extrair]: https://github.com/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair.ipynb
[extrair-mapeamento]: https://github.com/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair_mapeamento.ipynb
[mapear]: https://github.com/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dmapear_empenho.ipynb

[doc-mapeamento]: https://github.com/Winzen/mides-rascunho/blob/main/docs/scraping/%5Bse%5Dextrair_mapeamento.md
[doc-mapear]: https://github.com/Winzen/mides-rascunho/blob/main/docs/scraping/%5Bse%5Dmapear_empenho.md

[raspador]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/ro/[ro]extrair.ipynb
[verificar-ip]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/ro/[ro]extrair.ipynb#scrollTo=epToHlxZBG35
[importação]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/ro/[ro]extrair.ipynb#scrollTo=0KXJ4Keo9eYe
[pegar-municipios]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/ro/[ro]extrair.ipynb#scrollTo=FtyeVeEA9jGX
[pegar-links]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/ro/[ro]extrair.ipynb#scrollTo=gml1tKEk9qHS
[download]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/ro/[ro]extrair.ipynb#scrollTo=qShzweX09vua
[mandar-drive]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/ro/[ro]extrair.ipynb#scrollTo=3DdZJ5-dyTPC

