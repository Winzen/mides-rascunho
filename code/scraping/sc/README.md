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
Bandeira|<img src="/docs/images/flags/sc.png" width=50>
Nome|Santa Catarina
Sigla| SC
Municípios| 295
Cobertura do Raspador| 2021 - 2024
Link_Site| [:link:](https://paineistransparencia.tce.sc.gov.br/extensions/appDespesasMunicipaisExternoNovo/index.html)
Pipeline|✓
Sistema| qlik sense
Server|Registro de Lentidão
Ip_estrageiro|✓
Link_drive|[:link:](https://drive.google.com/drive/u/0/folders/1VvDVFLQ9CHo2TZiyx-IOE9ebIq-yfnSl)
Link_storage|[:link:](https://console.cloud.google.com/storage/browser/basedosdados-dev/staging/world_wb_mides/raw_empenho_sc?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&cloudshell=false&project=basedosdados-dev)
Link_licitacao|[:link:](https://drive.google.com/drive/u/0/folders/1phCHuuMHJNNFnzd6wm10KvIy7eAWL5o0)

# Logica do Site

Site de Santa Catarina utiliza de [qlik sense API](https://help.qlik.com/en-US/sense-developer/May2024/Subsystems/EngineJSONAPI/Content/introduction.htm).

Porém, na atual versão do raspador ele não está fazendo uso dessa API e sim atravès do selenium executando varias interaçoes que nos leva aos dados

Futuramente atualizar o codigo para ele utilizar da [qlik sense API](https://help.qlik.com/en-US/sense-developer/May2024/Subsystems/EngineJSONAPI/Content/introduction.htm)..
