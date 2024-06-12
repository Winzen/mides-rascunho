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
Bandeira|<img src="http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/normal_1409852741bandeirabahia.png" width=50>
Nome|Bahia
Sigla| BA
Municípios| 417
Cobertura do Raspador| 2010 - 2024
Pipeline|✓
Sistema| reCAPTCHA v3
Ip_estrageiro|X
Link_drive|[:link:](https://drive.google.com/drive/u/0/folders/1HFhCqiUNC_AZawX43MQxs5hosY0B757V)
Link_storage|X
Link_licitacao|[:link:](https://drive.google.com/drive/u/0/folders/1EOrHv1tnydgwsahaZROwpZJbUg5Uf3JC)

# Logica do Site

Site da Bahia utiliza de [reCAPTCHA v3](https://developers.google.com/recaptcha/docs/v3?hl=pt-br).

Basicamente para acessar os elementos da pagina precisamos de um token gerado pelo google que será validado em cada interação.
Normalmente é gerado um token por pagina, sendo assim você pode apenas fazer uma interação por vez.

Te obrigando a seguir um caminho fixo para chegar até as paginas do devido empenho.
O reCATCHA também tem a forçar um erro dado um certo numero de empenhos consultados em sequencia. Podendo varias entre 4 ou 6 empenhos em sequencia antes de algum erro acontecer.
Depois de um erro ocorrer você teria que iniciar todos os filtros novamente, clickar pagina a pagina para voltar onde estava extraindo.

E temos mais de 15 milhoes de Empenhos para ser consultados.

Para contornar isso, foi usado o [selenium](https://pypi.org/project/selenium/) apenas para gerar tokens do [reCAPTCHA v3](https://developers.google.com/recaptcha/docs/v3?hl=pt-br).

Abrimos um quantidade X de navedores, cada navegador pode gerar 21 tokens.
Usamos das funçoes abaixo dentro do selenium para conseguir gerar tokens. ⬇️

```js
function carregar_tokens(){
    for (var i = 0; i < 21; i++) {
    validar_ids(i + 1)
    }
};

async function validar_ids(n_index){
   await grecaptcha.ready(function() {
            grecaptcha.execute('6Lc5jcsbAAAAADmXWT8NNXy_8mFEu944y99PVFUr', {action:'validate_captcha'})
                      .then(function(token) {
            $('.id_validation' + (n_index)).val(token);
        });
    });

};
carregar_tokens();
```
Colocamos os tokens gerado como parametros que são utilizados para gerar links que vão diretamente para os empenhos por via de requisição `GET`

Só é possivel formar os links que vão direto ao empenho pegando informaçoes basicas dos empenhos posteriomente de um JSON em um `div`.
Ele normalmente se encontra na primeira pagina de pesquisa de empenhos. Ele contem informaçoes basicas de todos os empenhos relacionados a consulta.
