# Rede Wikipedia de Currais Novos 

## Membros
1) Fernando Lucas Sousa Silva |  20220080534</p>
2) Teophilo Vitor de Carvalho Clemente | 20220080516</p>

## Objetivo 
Este penúltimo projeto da disciplina tem por objetivo a análise e construção de uma rede com base em um página da wikipédia. Escolhemos para isso, a página wikipedia de Currais Novos, cidade que nós componentes do grupo, nascemos. 

<p align='center'><img src='./images/currais_praca.jpeg'></p>

## Solução

O notebook contendo todos os códigos produzidos e as análises completas acerca do trabalho pode ser acessado aqui[![Jupyter](https://img.shields.io/badge/-Notebook-191A1B?style=flat-square&logo=jupyter)](https://github.com/TeophiloVitor/data_structure2/blob/main/week11-12/AEDII_T3U2.ipynb)</p>

Para o desenvolvimento do projeto foram utilizadas as seguintes bibliotecas: nxviz, networkx, wikipedia, pandas, matplotlib e outras. Dado isso, foi feito o processamento dos dados a serem trabalhados, posteriormente, feitas as análises pedidas para o projeto com as dadas visualizações por gráficos como veremos ao longo desta explicação.

## Processamento dos dados

A rede de Currais Novos possui 2557 nós e 3602 arestas, para fins de visualização e retirada de  relações mínimas, filtramos a rede para permanecer somente as que tinha grau maior que 8 e com isso a rede final analisada ficou com 12 nós e 68 arestas, com isso permaneceram somente as relações mais pertinentes como podemos ver a seguir:</p>
```
11 Brazil
9 Rio Grande Do Norte
8 Regions Of Brazil
7 Northeast Region, Brazil
7 States Of Brazil
7 Geographic Coordinate System
6 Municipalities Of Brazil
3 Apertados Canyon
3 Currais Novos
3 Vicente De Lima
2 Flag Of Currais Novos
2 Seal Of Currais Novos
```
Através do gráfico também podemos verificar a representação destas conexões e suas interrelações. Duas relações devemos destacar, apesar de não terem a maior pertinência. A de Vicente de Lima, atleta curraisnovense de renome nacional e internacional por ter participado de 3 olimpíadas e ter conquistado 1 medalha de prata e 1 de  bronze na modalidade de atletismo e Canyon dos Apertados, um ponto turístico da cidade e que faz parte do Geoparque Seridó. A seguir o gráfico que ilustra as relações:

<p align='center'><img src='./images/garfico_nos-conexao.png'></p>

## Análise das métricas pedidas

As métricas que serão analisadas são: grau, proximidade, autovetor e intermediação. O grau indica o nó com maior grau de acordo com o número de seus vizinhos. A proximidade  indica a distância ou proximidade média do nó. O autovetor verifica se a vizinhança do nó é importante para a rede. Por último, a intermediação é útil para entendimento de fluxo, ela calcula quantas vezes determinado nó fez parte de um caminho entre dois nós distintos.</p>

A seguir temos a imagem que mostra o resultado para cada métrica, ao lado temos uma legenda de cor, do azul (valor baixo) ao vermelho (valor alto), a partir dela podemos visualizar o resultado para cada métrica como podemos ver a seguir:

<p align='center'><img src='./images/graficos_metricas_inico.png'></p>

## Centralidade

As distribuições de centralidade serão analisadas nos próximos gráficos. Inicialmente vamos analisar o histograma da rede, assim analisaremos o grau de cada nó da rede e com isso, vemos que os nós têm valor de passo distribuído entre 6 e 17 e com um pico no meio.

<p align='center'><img src='./images/histograma.png'></p>

Posteriormente foi feita a análise do Gráfico densidade de probabilidade, essa  análise nos mostrará a densidade dos nós em relação a rede de acordo com o grau. Nela podemos ver a curva em vermelho que permeia os dados e notamos como visto anteriormente a distribuição dos valores e a curva que acompanho, principalmente na região central.

<p align='center'><img src='./images/grafico_pdf.png'></p>

A seguir foi plotado o Gráfico de densidade cumulativa, ele indica a porcentagem de conexões que os nós de determinado grau possuem em relação às conexões da rede. Aqui podemos enxergar a curva em vermelho que começa com o valor baixo e após cresce, isso se dá por ela crescer ao mesmo passo que os valores no histograma crescem e se acumulam e com isso no final ela está no nível mais alto.

<p align='center'><img src='./images/grafico_cdf.png'></p>

Para efeito de comparação, agora é plotado um gráfico com todas as métricas. Como vemos, devido a termos usado somente às relações com grau maior que 8, notamos em todas as métricas uma simetria positiva e com comportamento geral com  grau pequeno como podemos ver a seguir:

<p align='center'><img src='./images/graficos_metricas_resumo.png'></p>

## Decomposição do Núcleo

A decomposição do núcleo tem relação direta à hierarquia de núcleos, para isso analisaremos as métricas, k-core e k-shell. O k-core refere-se a uma sub-rede na qual todos nós possuem pelo menos k vizinhos. Outrossim, os nós que são eliminados para atingir um k-core são chamados de shell. As métricas podem ser vistas na figura a seguir, o core em vermelho e o shell em azul e as suas respectivas ligações.

<p align='center'><img src='./images/decomposição_núcleo.png'></p>

## Como executar 

Para executar esse projeto recomendamos que abra um Google Colaboratory e execute o nosso notebook de solução[![Jupyter](https://img.shields.io/badge/-Notebook-191A1B?style=flat-square&logo=jupyter)](https://github.com/TeophiloVitor/data_structure2/blob/main/week11-12/AEDII_T3U2.ipynb), basta executar as células na ordem indicada e obterá a solução aqui visualizada.

## Referências
-Página Currais Novos no wikipedia [[Link]](https://pt.wikipedia.org/wiki/Currais_Novos)</p>
-Repositório Professor Ivanovitch[![Repository](https://img.shields.io/badge/-Repo-191A1B?style=flat-square&logo=github)](https://github.com/ivanovitchm/datastructure)





