<!-- Header -->
<p align="center">
  <a href="https://basedosdados.org">
    <img src="docs/images/logo1_mides_black.png" width="340" alt="MiDES">
  </a>
</p>


<p align="center">
    <em>Microdados de Despesas de Entes Subnacionais.</em>
</p>

MiDES (_Expenditure Microdata of Subnational Entities_ in English) is a disaggregated and harmonized dataset on public procurement and budget execution by Brazilian municipalities which currently covers around 72% of Brazilian municipalities and spans the years 2002–24. This dataset provides key information that was previously unavailable from aggregate data, such as the identities of suppliers, details on purchases, and granular information on the life cycle of each expenditure action.

Our data is generated from State Audit Courts (_TCEs_ in Portuguese) with standardization efforts. Unlike the [data-paper repo](https://github.com/municipal-budget-execution/data-paper), which shows the reproducibility codes for the results of the article [MiDES: New Data and Facts from Local Procurement and Budget Execution in Brazil](https://elibrary.worldbank.org/doi/abs/10.1596/1813-9450-10598), published in November 2023 with a photograph of the data until then, this repository aims to show the most current work developed with fiscal data.

## Data Coverage
Flags|State|Years|Budget data|Procurement data|Original Source
|:-:|:-:|:-:|:-:|:-:|:-:|
<img src="/docs/images/flags/ac.png" width=50>|AC|?|||?|
<img src="/docs/images/flags/al.png" width=50>|AL|?|||?|
<img src="/docs/images/flags/am.png" width=50>|AM|?|||?|
<img src="/docs/images/flags/ap.png" width=50>|AP|?|||?|
<img src="/docs/images/flags/ba.png" width=50>|BA|2010(1)||✓|LAI|
<img src="/docs/images/flags/ce.png" width=50>|CE|2009(1)|✓|✓|[:link:](https://api.tce.ce.gov.br/)|
<img src="/docs/images/flags/df.png" width=50>|DF|2009(1)|✓||[:link:](https://www.transparencia.df.gov.br/#/downloads#des)|
<img src="/docs/images/flags/es.png" width=50>|ES|2018(1)|✓||LAI|
<img src="/docs/images/flags/go.png" width=50>|GO|2019(1)|✓||[:link:](https://www.tcmgo.tc.br/pentaho/api/repos/cidadao/app/index.html)|
<img src="/docs/images/flags/ma.png" width=50>|MA|?|||?|
<img src="/docs/images/flags/mg.png" width=50>|MG|2014(1)|✓|✓|[:link:](https://dadosabertos.tce.mg.gov.br/)|
<img src="/docs/images/flags/ms.png" width=50>|MS|?|||?|
<img src="/docs/images/flags/mt.png" width=50>|MT|?|||?|
<img src="/docs/images/flags/pa.png" width=50>|PA|?|||?|
<img src="/docs/images/flags/pb.png" width=50>|PB|2003(1)|✓|✓|[:link:](https://dados.tce.pb.gov.br)|
<img src="/docs/images/flags/pe.png" width=50>|PE|2013(1)|✓|✓|[:link:](https://sistemas.tce.pe.gov.br/DadosAbertos/Exemplo!listar)|
<img src="/docs/images/flags/pi.png" width=50>|PI|?|||?|
<img src="/docs/images/flags/pr.png" width=50>|PR|2013(1)|✓|✓|[:link:](https://servicos.tce.pr.gov.br/TCEPR/Tribunal/Relacon/Dados/DadosConsulta/Consolidado)|
<img src="/docs/images/flags/rj.png" width=50>|RJ|2002(1)|✓||[:link:](https://tce.rj.gov.br/auditormunicipio/Default.aspx)|
<img src="/docs/images/flags/rn.png" width=50>|RN|2016(1)|✓||[:link:](https://apidadosabertos.tce.rn.gov.br/swagger/ui/index#/)|
<img src="/docs/images/flags/ro.png" width=50>|RO|2019(1)2020 |✓||[:link:](https://transparencia.tce.ro.gov.br/transparenciatce/Remessa/Pesquisar)|
<img src="/docs/images/flags/rr.png" width=50>|RR|?|||?|
<img src="/docs/images/flags/rs.png" width=50>|RS|2010(1)|✓|✓|[:link:](https://dados.tce.rs.gov.br)|
<img src="/docs/images/flags/sc.png" width=50>|SC|2015(1)|✓|✓|[:link:](https://servicos.tce.sc.gov.br/farol_externo/index.html)|
<img src="/docs/images/flags/se.png" width=50>|SE|?|||?|
<img src="/docs/images/flags/sp.png" width=50>|SP|2008(1)|✓||[:link:](https://transparencia.tce.sp.gov.br/conjunto-de-dados)|
<img src="/docs/images/flags/to.png" width=50>|TO|2013(1)|✓|✓|[:link:](https://portaldocidadao.tce.to.gov.br/estadomunicipios/index)|

## Data Access
The data is available on [BasedosDados](https://basedosdados.org/dataset/d3874769-bcbd-4ece-a38a-157ba1021514?table=14c5d05b-9830-4710-b7ac-7e0ca1bf9d8b)' public data-lake. We follow the methodology of Base dos Dados ([Dahis et al., 2022](https://osf.io/preprints/socarxiv/r76yg)) in harmonization schema and data lake storage. Base dos Dados is a non-profit organization with the mission to universalize access to high-quality data. They provide a platform in Google Cloud with more than 100 treated tables. Between the benefits, we can cross our data with population, GDP, companies, public treasure dataset, etc.  
For access database in BigQuery, you can follow these [steps](https://basedosdados.github.io/mais/access_data_bq/) to create a personal project and create your queries. The documentation also provides information on how to access the base on other platforms, such as Python, R and Stata. The most simple query example is

```sql
SELECT * FROM `basedosdados.world_wb_mides.empenho` LIMIT 100
```

The result is the 100 first observations of commitment table. Futhermore, the [Mides page](https://basedosdados.org/dataset/d3874769-bcbd-4ece-a38a-157ba1021514?table=14c5d05b-9830-4710-b7ac-7e0ca1bf9d8b#:~:text=o%20c%C3%B3digo%20abaixo%2C-,clique%20aqui,-para%20ir%20ao) in Data Basis website shows all tables, variables, and another descriptions necessary to use the dataset.  The scripts here provided differents queries that can be reproduced just changing the `project_id_bq`. We provide another analysis sample in [Colab](https://colab.research.google.com/drive/1DrYpLhaR4zueA6nxQyxqxQGZhMKQYIrp#scrollTo=lOpvFr42BvN7). 

## Updates
We created this page as a way of keeping the graphs and tables from the article released in Nov/2023 (containing 7 states) as up-to-date as possible (there are currently 13 states). In addition, the treatment codes and all the project documentation are concentrated here.
