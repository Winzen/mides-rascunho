<!-- Header -->
<p align="center">
  <a href="https://basedosdados.org">
    <img src="/docs/images/logo1_mides_black.png" width="340" alt="MiDES">
  </a>
</p>


<p align="center">
    <em>Microdados de Despesas de Entes Subnacionais.</em>
</p>

MiDES (_Expenditure Microdata of Subnational Entities_ in English) is a disaggregated and harmonized dataset on public procurement and budget execution by Brazilian municipalities which currently covers around 72% of Brazilian municipalities and spans the years 2002–24. This dataset provides key information that was previously unavailable from aggregate data, such as the identities of suppliers, details on purchases, and granular information on the life cycle of each expenditure action.

Our data is generated from State Audit Courts (_TCEs_ in Portuguese) with standardization efforts. Unlike the [data-paper repo](https://github.com/municipal-budget-execution/data-paper), which shows the reproducibility codes for the results of the article [MiDES: New Data and Facts from Local Procurement and Budget Execution in Brazil](https://elibrary.worldbank.org/doi/abs/10.1596/1813-9450-10598), published in November 2023 with a photograph of the data until then, this repository aims to show the most current work developed with fiscal data.

## Data Coverage
flag|nome|sigla|online|link_site|pipeline|sistema|ip_estrageiro|link_raspador|link_drive|link_storage|link_licitacao
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
<img src="http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/normal_1409852743bandeirasantacatarina.png">|Santa Catarina|SC|✓|[:link:](https://servicos.tce.sc.gov.br/farol_externo/index.html)|✓|qlik sense|✓|[:link:](/code/scraping/sc/[sc]extrair.ipynb)|[:link:](https://drive.google.com/drive/u/0/folders/1VvDVFLQ9CHo2TZiyx-IOE9ebIq-yfnSl)|[:link:](https://console.cloud.google.com/storage/browser/basedosdados-dev/staging/world_wb_mides/raw_empenho_sc?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&cloudshell=false&project=basedosdados-dev)|[:link:](https://drive.google.com/drive/u/0/folders/1phCHuuMHJNNFnzd6wm10KvIy7eAWL5o0)

## Data Access
The data is available on [BasedosDados](https://basedosdados.org/dataset/d3874769-bcbd-4ece-a38a-157ba1021514?table=14c5d05b-9830-4710-b7ac-7e0ca1bf9d8b)' public data-lake. We follow the methodology of Base dos Dados ([Dahis et al., 2022](https://osf.io/preprints/socarxiv/r76yg)) in harmonization schema and data lake storage. Base dos Dados is a non-profit organization with the mission to universalize access to high-quality data. They provide a platform in Google Cloud with more than 100 treated tables. Between the benefits, we can cross our data with population, GDP, companies, public treasure dataset, etc.  
For access database in BigQuery, you can follow these [steps](https://basedosdados.github.io/mais/access_data_bq/) to create a personal project and create your queries. The documentation also provides information on how to access the base on other platforms, such as Python, R and Stata. The most simple query example is

```sql
SELECT * FROM `basedosdados.world_wb_mides.empenho` LIMIT 100
```

The result is the 100 first observations of commitment table. Futhermore, the [Mides page](https://basedosdados.org/dataset/d3874769-bcbd-4ece-a38a-157ba1021514?table=14c5d05b-9830-4710-b7ac-7e0ca1bf9d8b#:~:text=o%20c%C3%B3digo%20abaixo%2C-,clique%20aqui,-para%20ir%20ao) in Data Basis website shows all tables, variables, and another descriptions necessary to use the dataset.  The scripts here provided differents queries that can be reproduced just changing the `project_id_bq`. We provide another analysis sample in [Colab](https://colab.research.google.com/drive/1DrYpLhaR4zueA6nxQyxqxQGZhMKQYIrp#scrollTo=lOpvFr42BvN7). 

## Updates
We created this page as a way of keeping the graphs and tables from the article released in Nov/2023 (containing 7 states) as up-to-date as possible (there are currently 13 states). In addition, the treatment codes and all the project documentation are concentrated here.
