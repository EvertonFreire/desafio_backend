# How to

Esta é a Api construída por mim para gerenciar os dados que estão no banco de dados.

Dependências necessárias:

* Python 2.7
* Python-pip (lastest)
* Mariadb-server

Dependências do Flask (Instalação via PIP):

* Flask
* Flask-MySQL
* jsonify
* mysql-python
* mysql-connector
* PyMySQL

# Instalação

Instalar os pacotes informados acima, logo após pode ser realizada a configuração do banco de dados.

Ao configurar o banco de dados deve ser inseridas as configurações nos dois arquivos de configuração, um para o Flask e outro para a comunicação com o banco de dados. 

Inserir as configurações necessárias para o banco de dados realizadas nos arquivos:

* src/app/got_desafio.py
* src/app/connect_mysl.py

Devido a um bug onde o conector do mysql não conseguia escrever nas tabelas foi necessário criar dois arquivos de configuração.

Caso queira pode utilizar o script em sql que está na pasta para criar o banco de dados e as tabelas;

# Run

Logo após configurar os dados do banco de dados basta iniciar a api com o comando:

* python src/app/got_desafio.py
