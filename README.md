<!-- Header -->
<p align="center">
   <a href="https://basedosdados.org">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/images/logo1_mides_white.png">
      <source media="(prefers-color-scheme: light)" srcset="docs/images/logo1_mides_black.png">
      <img src="docs/images/logo1_mides_white.png" width="340" alt="MiDES">
  </picture>
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
<img src="/docs/images/flags/ba.png" width=50>|BA|2010(1)||✓|LAI|
<img src="/docs/images/flags/ce.png" width=50>|CE|2009(1)|✓|✓|[:link:][link-ce]|
<img src="/docs/images/flags/df.png" width=50>|DF|2009(1)|✓||[:link:](link-df]|
<img src="/docs/images/flags/es.png" width=50>|ES|2018(1)|✓||LAI|
<img src="/docs/images/flags/go.png" width=50>|GO|2019(1)|✓||[:link:][link-go]|
<img src="/docs/images/flags/mg.png" width=50>|MG|2014(1)|✓|✓|[:link:][link-mg]|
<img src="/docs/images/flags/pb.png" width=50>|PB|2003(1)|✓|✓|[:link:][link-pb]|
<img src="/docs/images/flags/pe.png" width=50>|PE|2013(1)|✓|✓|[:link:][link-pe]|
<img src="/docs/images/flags/pr.png" width=50>|PR|2013(1)|✓|✓|[:link:][link-pr]|
<img src="/docs/images/flags/rj.png" width=50>|RJ|2002(1)|✓||[:link:][link-rj]|
<img src="/docs/images/flags/rn.png" width=50>|RN|2016(1)|✓||[:link:][link-rn]|
<img src="/docs/images/flags/ro.png" width=50>|RO|2019(1)2020 |✓||[:link:][link-ro]|
<img src="/docs/images/flags/rs.png" width=50>|RS|2010(1)|✓|✓|[:link:][link-rs]|
<img src="/docs/images/flags/sc.png" width=50>|SC|2015(1)|✓|✓|[:link:][link-sc]|
<img src="/docs/images/flags/sp.png" width=50>|SP|2008(1)|✓||[:link:][link-sp]|
<img src="/docs/images/flags/to.png" width=50>|TO|2013(1)|✓|✓|[:link:][link-to]|

## Data Access
The data is available on [BasedosDados](https://basedosdados.org/dataset/d3874769-bcbd-4ece-a38a-157ba1021514?table=14c5d05b-9830-4710-b7ac-7e0ca1bf9d8b)' public data-lake. We follow the methodology of Base dos Dados ([Dahis et al., 2022](https://osf.io/preprints/socarxiv/r76yg)) in harmonization schema and data lake storage. Base dos Dados is a non-profit organization with the mission to universalize access to high-quality data. They provide a platform in Google Cloud with more than 100 treated tables. Between the benefits, we can cross our data with population, GDP, companies, public treasure dataset, etc.  
For access database in BigQuery, you can follow these [steps](https://basedosdados.github.io/mais/access_data_bq/) to create a personal project and create your queries. The documentation also provides information on how to access the base on other platforms, such as Python, R and Stata. The most simple query example is

```sql
SELECT * FROM `basedosdados.world_wb_mides.empenho` LIMIT 100
```

The result is the 100 first observations of commitment table. Futhermore, the [Mides page](https://basedosdados.org/dataset/d3874769-bcbd-4ece-a38a-157ba1021514?table=14c5d05b-9830-4710-b7ac-7e0ca1bf9d8b#:~:text=o%20c%C3%B3digo%20abaixo%2C-,clique%20aqui,-para%20ir%20ao) in Data Basis website shows all tables, variables, and another descriptions necessary to use the dataset.  The scripts here provided differents queries that can be reproduced just changing the `project_id_bq`. We provide another analysis sample in [Colab](https://colab.research.google.com/drive/1DrYpLhaR4zueA6nxQyxqxQGZhMKQYIrp#scrollTo=lOpvFr42BvN7). 

## Updates
We created this page as a way of keeping the graphs and tables from the article released in Nov/2023 (containing 7 states) as up-to-date as possible (there are currently 13 states). In addition, the treatment codes and all the project documentation are concentrated here.

<!-- Referencias -->

[link-ba]: ...
[link-ce]: https://api.tce.ce.gov.br/
[link-df]: https://www.transparencia.df.gov.br/#/downloads#des
[link-es]: ...
[link-go]: https://www.tcmgo.tc.br/pentaho/api/repos/cidadao/app/index.html
[link-mg]: https://dadosabertos.tce.mg.gov.br/
[link-pb]: https://dados.tce.pb.gov.brhttps://dados.tce.pb.gov.br
[link-pe]: https://sistemas.tce.pe.gov.br/DadosAbertos/Exemplo!listar
[link-pr]: https://servicos.tce.pr.gov.br/TCEPR/Tribunal/Relacon/Dados/DadosConsulta/Consolidado
[link-rj]: https://tce.rj.gov.br/auditormunicipio/Default.aspx
[link-rn]: https://apidadosabertos.tce.rn.gov.br/swagger/ui/index#/
[link-ro]: https://transparencia.tce.ro.gov.br/transparenciatce/Remessa/Pesquisar
[link-rs]: https://dados.tce.rs.gov.br
[link-sc]: https://servicos.tce.sc.gov.br/farol_externo/index.html
[link-sp]: https://transparencia.tce.sp.gov.br/conjunto-de-dados
[link-to]: https://portaldocidadao.tce.to.gov.br/estadomunicipios/index

