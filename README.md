# Engenharia de dados do projeto imoviz
A arquitetura da engenharia de dados consiste em uma pipeline de dados
que são obitidos através de um crawler que explora uma lista de urls,
esses dados são inseridos na pipeline para serem tratados 
e inseridos no banco.

## Pipeline
A pipeline consiste em 
1. checar se os dados estão conformes ao schema definido no banco.
2. Extrair geolocalizadores.
3. Verificar a existência de dados repetidos antes de inserir no banco.
