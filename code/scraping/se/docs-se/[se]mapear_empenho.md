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

# Index

- [Raspador](#raspador)
  - [Constante](#constante)
  - [Importação](#importação)
  - [Extrair](#extrair)
  - [Mapear Empenhos](#mapear-empenhos)
     - [Dividir por anos](#dividir-por-anos)
  - [Mandar para o drive Manualmente](#mandar-para-o-drive-manualmente)
 
# [Raspador][raspador]

Notebook responsavel por extrair as informaçoes das paginas de empenhos extraida com [[se]extrair_mapeamento][extrair-mapa] e colocar em CSVs para serém usados em [[se]extrair.ipynb][main-extrair]
   
## [Constante][constante]
  
  Nessa sessão controlamos qual ano será raspado, definimos o caminho para o csv que se encontra as entidades e caminho para salvar e extrair arquivos raspados.
  Exemplo da sessão em codigo ⬇️:
   ```py
   path_drive_input = None # Onde será extraido e salvo as paginas de empenho
   path_drive_csv = None # Onde será extraido e salvo o csv das entidades
   path_drive_csv_mapeamento = # Onde será extraido e salvo os CSVs do mapeamento dos empenhos
   ```
## [Importação][importação]
  Grupo responsavel por ativar todas as funçoes e bibliotecas necessarias para as de mais celulas do notebook.

## [Extrair][extrair]
  Sessão responsavel por extrair possiveis dados já salvos do caminhos definido em [constantes][constante].

## [Mapear Empenhos][mapear]

  Sessão responsavel pela criação de um CSV com todos os possiveis empenhos até o presente momento da extração com o [raspador][extrair-mapa].
  
  *Leva aproximadamente 50 minutos para ser completado*
  
  Exemplo da sessão em codigo ⬇️:
   ```py
path_csvs = "/content/input/**/**/**/*.html"
htmls = glob.glob(path_csvs)

with concurrent.futures.ThreadPoolExecutor() as executor:
  tasks = [task for task in executor.map(extrair, htmls)]
  linhas_paginas = [task for task in tasks if type(task) != str]
  erros = [task for task in tasks if type(task) == str]

print(f"De {len(htmls)} paginas foram coletadas {len(linhas_paginas)} com sucesso")

linhas = [linha for linhas in linhas_paginas for linha in linhas]

colunas = ["ano", "municipio", "unidade",
           "numero_empenho", "data_empenho", "participante",
           "valor_empenhado", "valor_pago", "link"]

df = pd.DataFrame(linhas, columns=colunas)
df["coletado"] = False
df.to_csv("csvs/se_mapeamentos_empenhos.csv", index=False)
   ```
### [Dividir por anos][dividir]

Dividi todos os empenhos por anos em CSV.

Exemplo da sessão em codigo ⬇️:
```py
anos = df.ano.unique()
for ano in anos:
  df_ano = df[df.ano == ano]
  df_ano.to_csv(f"csvs/se_mapeamentos_empenhos_{ano}.csv", index=False)
```

## [Mandar para o drive Manualmente][mandar-drive]

Sessão responsavel por salvar os dados coletados para o google drive caso seja necessario.
Para utilizar dessa sessão é preciso preencher um caminho de salvamento em [constantes][constante].
Também verificar se foi gerado a conexão com o google drive ao inicio do notebook.

Exemplo da sessão em codigo ⬇️:

```py
drive.mount('/content/drive')


send_folder_drive(path_drive_input,
                f"/content/input/")
```

<!-- Referencias -->

[main-extrair]: https://github.com/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair.ipynb
[extrair-mapa]: https://github.com/Winzen/mides-rascunho/blob/main/code/scraping/se/docs-se/%5Bse%5Dextrair_mapeamento.md

[raspador]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dextrair_mapeamento.ipynb#scrollTo=9ptCC5xP2ssI
[constante]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dmapear_empenho.ipynb#scrollTo=1ufupK_j79Fo
[importação]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dmapear_empenho.ipynb#scrollTo=UM-EZote8LW0
[extrair]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dmapear_empenho.ipynb#scrollTo=TTb_aULe8FOB
[mapear]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dmapear_empenho.ipynb#scrollTo=R40r8jAG-fp8
[dividir]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dmapear_empenho.ipynb#scrollTo=tiwZrzhMDtZf
[mandar-drive]: https://colab.research.google.com/github/Winzen/mides-rascunho/blob/main/code/scraping/se/%5Bse%5Dmapear_empenho.ipynb#scrollTo=98_15dAlHvyk
