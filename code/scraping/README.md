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

Nesse diretorios temos como foco armazenar e informar sobre os codigos de raspagem utilizados durante a coleta de dados do projeto. A ideia também é você conseguir fazer extraçoes facialmente pelos codigos.

Cada raspador funciona de uma forma um tanto diferente. Você pode conseguir informaçoes sobre como eles funcionam e acessar os devidos codigos indo diretamente ao diretorio ou usando a tabela [abaixo](/code/scraping#resumo)

## Resumo
flag|nome|sigla|online|link_site|pipeline|sistema|ip_estrageiro|link_raspador|link_drive|link_storage|link_licitacao
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
<img src="/docs/images/flags/ac.png">|Acre|AC|✓|[:link:](http://qlik.tceac.tc.br/extensions/gastospublicos/gastospublicos.html?_ga=2.234985153.1351290455.1696941468-160473323.1696941468&_gl=1*1udkbll*_ga*MTYwNDczMzIzLjE2OTY5NDE0Njg.*_ga_7W9X95Q11R*MTY5Njk0MTQ2Ny4xLjEuMTY5Njk0MTU4NS4wLjAuMA..*_ga_BGWR95NM02*MTY5Njk0MTQ2Ny4xLjEuMTY5Njk0MTU4NS4wLjAuMA..)|✓|qlik sense|✓|[:link:](/code/scraping/ac/)|[:link:](https://drive.google.com/drive/u/0/folders/1XRxr0CilhDWyiGfa2XPFcFZRCzUTdpz3)|X|X
<img src="/docs/images/flags/ba.png">|Bahia|BA|✓|[:link:](https://www.tcm.ba.gov.br/controle-social/consulta-de-despesas/)|X|reCAPTCHA v3|X|[:link:](/code/scraping/ba/)|[:link:](https://drive.google.com/drive/u/0/folders/1HFhCqiUNC_AZawX43MQxs5hosY0B757V)|X|[:link:](https://drive.google.com/drive/u/0/folders/1EOrHv1tnydgwsahaZROwpZJbUg5Uf3JC)
<img src="/docs/images/flags/go.png">|Goiás|GO|✓|[:link:](https://www.tcmgo.tc.br/pentaho/api/repos/cidadao/app/index.html)|✓|API|✓|[:link:](/code/scraping/go/)|[:link:](https://drive.google.com/drive/u/0/folders/1-BZ5mjftq98f8en8HLLSmKUwXXLaraU1)|[:link:](https://console.cloud.google.com/storage/browser/basedosdados-dev/staging/world_wb_mides/raw_despesa_go?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&cloudshell=false&project=basedosdados-dev)|X
<img src="/docs/images/flags/rn.png">|Rio Grande do Norte|RN|X|[:link:](https://apidadosabertos.tce.rn.gov.br/swagger/ui/index)|X|API|✓|[:link:](/code/scraping/rn/)|[:link:](https://drive.google.com/drive/u/0/folders/1f68Ow51jihexn_NBZmduKrWktM5i72u0)|[:link:](https://console.cloud.google.com/storage/browser/basedosdados-dev/staging/world_wb_mides/raw_empenho_rn?cloudshell=false&project=basedosdados-dev&pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22)))|[:link:](https://drive.google.com/drive/u/0/folders/1flx-RFUy0NhdLI0EQ4dhXej26FFs6YSh)
<img src="/docs/images/flags/ro.png">|Rondônia|RO|✓|[:link:](https://transparencia.tce.ro.gov.br/transparenciatce/Remessa/Pesquisar)|X|POST|✓|[:link:](/code/scraping/ro/)|[:link:](https://drive.google.com/drive/u/0/folders/1-ZkJqL6VfGOHua9A0Yca7C5t5XGYM87O)|[:link:](https://console.cloud.google.com/storage/browser/basedosdados-dev/staging/world_wb_mides/raw_empenho_ro?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&cloudshell=false&project=basedosdados-dev)|X
<img src="/docs/images/flags/sc.png">|Santa Catarina|SC|✓|[:link:](https://paineistransparencia.tce.sc.gov.br/extensions/appDespesasMunicipaisExternoNovo/index.html)|✓|qlik sense|✓|[:link:](/code/scraping/sc/)|[:link:](https://drive.google.com/drive/u/0/folders/1VvDVFLQ9CHo2TZiyx-IOE9ebIq-yfnSl)|[:link:](https://console.cloud.google.com/storage/browser/basedosdados-dev/staging/world_wb_mides/raw_empenho_sc?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&cloudshell=false&project=basedosdados-dev)|[:link:](https://drive.google.com/drive/u/0/folders/1phCHuuMHJNNFnzd6wm10KvIy7eAWL5o0)
<img src="/docs/images/flags/se.png">|Sergipe|SE|✓|[:link:](https://www.tcese.tc.br/portaldatransparencia/Default.aspx)|X|ASP.NET|✓|[:link:](/code/scraping/se/)|[:link:](https://drive.google.com/drive/u/0/folders/1-3MIVVXrPobqvSfuQCJ1ylW3xxAx2Zwx)|X|X
<img src="/docs/images/flags/to.png">|Tocantins|TO|✓|[:link:](https://portaldocidadao.tce.to.gov.br/estadomunicipios/index)|✓|GET|✓|[:link:](/code/scraping/to/)|[:link:](https://drive.google.com/drive/u/0/folders/1iYI1BUNfKa7C82drQvAlg23KHxF8NqWN)|[:link:](https://console.cloud.google.com/storage/browser/basedosdados-dev/staging/world_wb_mides/raw_empenho_to?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&cloudshell=false&project=basedosdados-dev)|X
