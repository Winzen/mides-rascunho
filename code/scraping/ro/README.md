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
Bandeira|<img src="http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/normal_1409852743bandeirarondonia.png" width=50>
Nome|Rondônia
Sigla| RO
Municípios| 52
Cobertura do Raspador| 2019 - 2020
Link_Site| [:link:](https://transparencia.tce.ro.gov.br/transparenciatce/Remessa/Pesquisar)
Pipeline|X
Sistema| POST
Server|Sem Registros de Quedas
Ip_estrageiro|✓
Link_drive|[:link:](https://drive.google.com/drive/u/0/folders/1-ZkJqL6VfGOHua9A0Yca7C5t5XGYM87O)
Link_storage|[:link:](https://console.cloud.google.com/storage/browser/basedosdados-dev/staging/world_wb_mides/raw_empenho_ro?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&cloudshell=false&project=basedosdados-dev)
Link_licitacao|X

# Logica do Site

No Site de Rondônia foi utilizados de `POST`s para conseguir chegar ao link direto dos ZIPs.

Infelizmente, os unicos dados disponveis são 2019 e 2020.

Após a coleta de todos os links de download dos zips.
È feito o download e armazenamento dos mesmo.
