<!-- Header -->
<p align="center">
  <a href="https://basedosdados.org">
    <img src="/docs/images/logo1_mides_black.png" width="340" alt="MiDES">
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
  - [Constante](#constante)
  - [Constante](#constante)
  - [Constante](#constante)
  - [Constante](#constante)
 
    
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
Ip_estrageiro|✓
Link Drive|[:link:][link-drive]
Link Storage|[:link:][link-storage]
Link Licitação|X

# Logica do Site

Site de Tocantins utiliza de `GET`s para chegar ao download do `.xls` que guarda empenhos, liquidaçoes, e pagamentos

# [Raspador][raspador]
 
## [Constante][constante]
  
  Nessa sessão controlamos qual ano será raspado, definimos o caminho para o csv que se encontra as entidades e caminho para salvar e extrair arquivos raspados.
  Exemplo da sessão em codigo ⬇️:
   ```py
    ano = 2018
    csv_entidade_git = "https://raw.githubusercontent.com/Winzen/mides-rascunho/main/code/scraping/to/municipios-entidades/entidades_to.csv?      token=GHSAT0AAAAAACJFESHXRUQPOWT6TB5XH3QSZTQ44KQ"
    path_drive_input = None # Definir caso você queira salvar os arquivos em algum lugar automaticamente ou extrair eles
   ```
## [Verificar IP][verificar-ip]

## [Importação][importação]
## [Extrair][extrair]
## [Registrar ID municipios e Entidades][registrar-ids]
## [Raspagem][raspagem]
## [Verificar dados perdidos][verificar-dados]
## [Mandar para o drive Manualmente][mandar-drive]

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
