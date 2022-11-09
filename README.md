# flask_firestore_api

<p2> Crud utilizando o flask e firestore <p2>

<h2> Obra a Maos </h2>

<h1> 
<img src=https://media2.giphy.com/media/o28elTLxOjiRW/giphy.gif width="300px"/> 
</h1>

<h3>Criar o ambiente virtual</h3>
python3 -m venv venv

<h3>Acessar o ambiente virtual</h3>
source venv/bin/activate

<h3>Instalar dependecias</h3>
pip install -r req.txt

<h3>Arquivo de configuracao</h3>
app/__init__.py

<h3>Baixa e adicionar o arquivo com as credencial do google, linha</h3>
cred = credentials.Certificate('./firebase-admin.json')

<h3>Executar projeto na porta 808</h3>
python run.py

<h3>Segue payloads, collection a ser criada ja definida no app/__init__.py chamada users</h3>

<h3>Adicionar</h3>
curl --location --request POST 'localhost:8080/add' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nome": "fabricio",
    "idade": 35,
    "cidade": "BA",
    "linguagens": ["Java script","Java"]
}'

<h3>Listar</h3>
curl --location --request GET 'localhost:8080/list' 

<h3>Listar com argumento nomo</h3>
curl --location --request GET 'localhost:8080/list?nome=fabricio' --data-raw ''

<h3>Atualizar</h3>
curl --location --request PUT 'localhost:8080/update' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id": "fD6BFOBmVsIbUjY7OUFq" ,
    "nome": "ronaldo",
    "idade": 32,
    "cidade": "SP",
    "linguagens": ["python"]
}'

<h3>Delete com argumento id</h3>
curl --location --request DELETE 'localhost:8080/delete?id=60LnTY0jSTmibWSc3b5S' \
--data-raw ''

<h3>Deletar todo</h3>
curl --location --request DELETE 'localhost:8080/delete?id=all' \
--data-raw ''

<h3>Pontos a melhorar</h3>
- msg de erro
- filtro
- output de logs 
- uso de OOP
- adicionar wsgi
