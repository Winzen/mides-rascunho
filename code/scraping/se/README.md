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
Bandeira|<img src="/docs/images/flags/se.png" width=50>
Nome|Sergipe
Sigla| SE
Municípios| 75
Cobertura do Raspador| 2008 - 2016
Link_Site| [:link:](https://www.tcese.tc.br/portaldatransparencia/Default.aspx)
Pipeline|X
Sistema| ASP.NET
Server|Sem registros de Quedas
Ip_estrageiro|✓
Link_drive|[:link:](https://drive.google.com/drive/u/0/folders/1-3MIVVXrPobqvSfuQCJ1ylW3xxAx2Zwx)
Link_storage|X
Link_licitacao|X

# Logica do Site

Site de Sergipe utiliza de [ASP.NET](https://help.qlik.com/en-US/sense-developer/May2024/Subsystems/EngineJSONAPI/Content/introduction.htm).

Um sistema onde podemos manipular uma sessão com sequencia de `POST`s. Apenas respeitando que o `POST`s apenas simule interação com coisas que se encontram na pagina gerada no back-end do servidor.
