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

# Index

- [Detalhes](#detalhes)
- [Logica do Site](#logica-do-site)

# Detalhes
Categoria|Detalhe|
|:-:|:-:|
Bandeira|<img src="/docs/images/flags/go.png" width=50>
Nome| Goiás
Sigla| Go
Municípios| 246
Cobertura do Raspador| 2019 - 2024
Link_Site| [:link:](https://www.tcmgo.tc.br/pentaho/api/repos/cidadao/app/index.html)
Pipeline|✓
Sistema| API
Server|Sem quedas registradas
Ip_estrageiro|X
Link_drive|[:link:](https://drive.google.com/drive/u/0/folders/1-BZ5mjftq98f8en8HLLSmKUwXXLaraU1)
Link_storage|[:link:](https://console.cloud.google.com/storage/browser/basedosdados-dev/staging/world_wb_mides/raw_despesa_go?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&cloudshell=false&project=basedosdados-dev)
Link_licitacao|X

# Logica do Site

Site de Goiás utiliza de uma API para ter acesso aos dados do site.

Em baixo temos o link base da API
```py
url = 'https://www.tcmgo.tc.br/pentaho/plugin/cda/api/doQuery'
```
Com a função abaixo, apenas com o nome do municipio e o ano, conseguimos forma um link que retorna todos os empenhos referente ao municipio e o ano

```py
def get_data_from_munipio_ano(municipio: str, ano: int) -> Dados:
  # Define the URL you want to send a POST request to
  url = 'https://www.tcmgo.tc.br/pentaho/plugin/cda/api/doQuery'

  # Define the data you want to send in the POST request
  data = {"paramparamMunicipio":	municipio,
  "paramparamAno":	ano,
  "path":	"/system/cidadao/dashboards/Despesas.cda",
  "dataAccessId":	"sqlEmpenhos",
  "outputIndexId":	1,
  "pageSize":	0,
  "pageStart":	0,
  "paramsearchBox":	""}

  # Make the POST request
  # response = requests.post(url, data=data).json()
  response = http.request('POST', url, fields=data).json()
  dados = response["resultset"]
  colunas = [column["colName"] for column in response['metadata']]

  return Dados(municipio, ano, dados, colunas)

```
