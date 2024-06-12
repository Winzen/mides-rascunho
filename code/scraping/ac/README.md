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
Bandeira|<img src="http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/normal_1409852740bandeiraacre.png" width=50>
Nome|Acre
Sigla| AC
Municípios| 22
Cobertura do Raspador| 2014 - 2023
Link_Site| [:link:](http://qlik.tceac.tc.br/extensions/gastospublicos/gastospublicos.html?_ga=2.234985153.1351290455.1696941468-160473323.1696941468&_gl=1*1udkbll*_ga*MTYwNDczMzIzLjE2OTY5NDE0Njg.*_ga_7W9X95Q11R*MTY5Njk0MTQ2Ny4xLjEuMTY5Njk0MTU4NS4wLjAuMA..*_ga_BGWR95NM02*MTY5Njk0MTQ2Ny4xLjEuMTY5Njk0MTU4NS4wLjAuMA..)
Pipeline|✓
Sistema|qlik sense
Server|Ficou Offline algumas vezes
Ip_estrageiro|✓
Link_drive|[:link:](https://drive.google.com/drive/u/0/folders/1XRxr0CilhDWyiGfa2XPFcFZRCzUTdpz3)
Link_storage|X
Link_licitacao|X

# Logica do Site

Raspador do Acre utiliza de [qlik sense API](https://help.qlik.com/en-US/sense-developer/May2024/Subsystems/EngineJSONAPI/Content/introduction.htm).

Primeiro utilizamos da biblioteca [websockets](https://pypi.org/project/websockets/) para abrir uma conexão com o Socket da api.

*Link da API:* 
```bash
ws://qlik.tceac.tc.br/app/cb9dbe12-5f79-4af9-93a6-a778ae7ffffa?reloadUri=http%3A%2F%2Fqlik.tceac.tc.br%2Fextensions%2Fgastospublicos%2Fgastospublicos.html%3F_ga%3D2.234985153.1351290455.1696941468-160473323.1696941468%26_gl%3D1*1udkbll*_ga*MTYwNDczMzIzLjE2OTY5NDE0Njg.*_ga_7W9X95Q11R*MTY5Njk0MTQ2Ny4xLjEuMTY5Njk0MTU4NS4wLjAuMA..*_ga_BGWR95NM02*MTY5Njk0MTQ2Ny4xLjEuMTY5Njk0MTU4NS4wLjAuMA..
```
Apos conexão estabelecida, fazemos algumas requisiçoes para conseguir o nome dos municipios e as datas disponveis para a extração.

Usamos o nome dos municipios e as datas para iniciar a extração, será extraido todos os anos disponiveis do municipio antes de passar para o proximo municipios disponivel.

Para consegui fazer as requisiçoes usamos de uma função chamada `make_envios_get_data`. Ela forma a lista de requisiçoes necessarias para chegar até o dado.

```py
sends_hs = make_envios_get_data(ano_number=ano_number, municipio_number=municipio_number)
```
`make_envios_get_data` receber dois paramentros `ano_number` e `municipio_number` esses parametros são responsaveis por alterar uma requisição responsavel por direcionar o ano e o municipio que será extraido
