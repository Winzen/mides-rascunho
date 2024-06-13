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

# Detalhes
Categoria|Detalhe|
|:-:|:-:|
Bandeira|<img src="/docs/images/flags/to.png" width=50>
Nome|Tocantins
Sigla| TO
Municípios| 139
Cobertura do Raspador| 2013 - 2024
Link_Site| [:link:](https://portaldocidadao.tce.to.gov.br/estadomunicipios/index)
Pipeline|✓
Sistema| GET
Server|Sem registros de Quedas
Ip_estrageiro|✓
Link_drive|[:link:](https://drive.google.com/drive/u/0/folders/1iYI1BUNfKa7C82drQvAlg23KHxF8NqWN)
Link_storage|[:link:](https://console.cloud.google.com/storage/browser/basedosdados-dev/staging/world_wb_mides/raw_empenho_to?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&cloudshell=false&project=basedosdados-dev)
Link_licitacao|X

# Logica do Site

Site de Tocantins utiliza de `GET`s para chegar ao download do `.xls` que guarda empenhos, liquidaçoes, e pagamentos
