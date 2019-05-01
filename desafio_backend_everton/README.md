# Desafio backend iTFLEX Tecnologia

O desafio é criar uma API de consulta de livros, casas e personagens do
show Game of Thrones.

A API deve ter disponibilizar as operações de consulta, cadastro e
remoção de itens, e também deve permitir a consulta textual dos itens.

Requisitos técnicos:

* Desenvolver em Python, NodeJS, PHP ou Ruby
* API deve seguir os princípios REST
* Salvar as informações necessárias em um dos bancos de dados relacionais abaixo:
  * Sqlite
  * PostgreSQL
  * MySQL
* Documentar como rodar o projeto

Requisitos funcionais:

* Dados das APIs no formato JSON;
* Operações CRUD de livros, casas e personagens;
* API de consulta de todos os itens por nome (retornar campo com tipo do item);
* Script/Código para cadastrar os dados por meio da API (usar os dados de [./data](./data)).

Para ganhar alguns pontos extras, podem ser implementadas as funcionalidades abaixo:

* Paginação das APIs de listagem;
* Autenticação por tokens assinados (JWT ou similar);
* Permissões de consulta por tipo de item;
* Pesquisa full text search, com score de itens encontrados.
