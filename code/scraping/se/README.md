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
Bandeira|src="http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/normal_1409852743bandeirasergipe.png" width=50>
Nome|Sergipe
Sigla| SE
Municípios| 75
Cobertura do Raspador| 2008 - 2016
Link_Site| [:link:](https://www.tcese.tc.br/portaldatransparencia/Default.aspx)
Pipeline|X
Sistema| ASP.NET
Server|Registro de Lentidão
Ip_estrageiro|✓
Link_drive|[:link:](https://drive.google.com/drive/u/0/folders/1-3MIVVXrPobqvSfuQCJ1ylW3xxAx2Zwx)
Link_storage|X
Link_licitacao|X

# Logica do Site

Site de Sergipe utiliza de [ASP.NET](https://help.qlik.com/en-US/sense-developer/May2024/Subsystems/EngineJSONAPI/Content/introduction.htm).

Um sistema onde podemos manipular uma sessão com sequencia de `POST`s. Apenas respeitando que o `POST`s apenas simule interação com coisas que se encontram na pagina gerada no back-end do servidor.
