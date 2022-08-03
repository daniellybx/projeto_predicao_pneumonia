# Predição de mortalidade em internações por pneumonias bacterianas sensíveis à Atenção Primária no Brasil, 2017 - 2021

## Contexto 

Condições Sensíveis a Atenção Primária (CSAP) são definidas como condições de saúde que podem ser detectadas em uma boa atenção primária e prevenidas de uma possível atenção hospitalar. Ainda engloba complicações que podem ser prevenidas com cuidados precoces ou imunização, além de doenças crônicas que devem ser diagnosticadas e acompanhadas na atenção primária. 

A principal causa de internação por condições sensíveis à APS no Brasil são as pneumonias bacterianas. O Brasil é um dos países em que ocorre o maior número de casos. O tratamento de pneumonia bacteriana também é conhecido, sendo predominantemente a antibioticoterapia a primeira linha de cuidado da doença

Diante desse cenário, é importante identificar quais os fatores que estão associados a um desfecho de mortalidade para a doença em um cenário de internação plenamente evitável. Nesse sentido, o objetivo do trabalho é predizer a mortalidade em pacientes internados por pneumonia bacteriana no SUS e identificar fatores associados a esse desfecho.

## Objetivo 

 - Predizer mortalidade em pacientes internados por pneumonia bacteriana no SUS 
 - Identificar fatores associados à mortalidade por pneumonia bacteriana em pacientes internados 

## Material e Métodos

Estudo preditivo considerando como desfecho a morte de pessoas internadas por pneumonia bacteriana no Brasil entre 2017 e 2021. O estudo considera todas as internações por pneumonia bacteriana no período. 

A fonte de dados é a base anonimizada de Autorizações de Internação Hospitalar (AIH) reduzidas do Sistema de Informações Hospitalares do Sistema Único de Saúde (SIH-SUS), disponível publicamente por meio Departamento de Informática do SUS (DATASUS) do endereço <https://datasus.saude.gov.br/transferencia-de-arquivos/>. 

Para o projeto, são consideradas as CID elencadas na Portaria Nº 221, de 17 de abril de 2008 considerando o grupo 6, que inclui as pneumonias bacterianas. Nesse grupo, estão incluídos os seguintes códigos de Classificação Internacional de Doenças (CID)- 10ª versão: 

- 	Pneumonia Pneumocócica (J13)
- 	Pneumonia por Haemophilus infuenzae (J14)
- 	Pneumonia por Streptococus (J15.3, J15.4)
-	Pneumonia bacteriana NE (J15.8, J15.9)
-	Pneumonia lobar NE (J18.1)

Como variável dependente é considerada a morte e como vaáriaveis preditoras são consideradas as 8 variáveis disponíveis na tabela.

|Variável |Identificação no SIH| Descrição| 
|---------|--------------------|----------|
|Morte|MORTE   |Indica se o internado evoluiu à óbito|
|Idade  |IDADE      |Indica a idade do internado no momento da internação |
|Sexo  |SEXO      |Indica o sexo do internado |
|Unidade Federada  |UF_ZI      |Código do IBGE para a unidade da federação em que a internação ocorreu |
|Permanência   |DIAS_PERM      |Indica quantos dias o internado permaneceu no estabelecimento de saúde |
|Número de filhos  |NUM_FILHOS      |Indica a quantidade de filhos declarada pelo internado |
|Grau de instrução  |INSTRU      |Indica o grau de instrução do internado |
|Tipo de UTI  |MARCA_UTI      |Indica qual o tipo de UTI utilizada pelo internado |
|Infecção hospitalar  |INFEHOSP     |Indica o status de infeção hospitalar do internado |

## Índice do repositório

### Pastas

- documentos: arquivos auxiliares da análise, como dicionário de dados e manuais do SIH;
- notebooks: notebooks e arquivos de dados da análise exploratória e da análise preditiva;
- scripts: scripts de *download* e tratamento de dados;

## Tecnologias usadas

- Python 3.8.10
- Jupyter Notebook
