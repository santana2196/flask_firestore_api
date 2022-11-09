# flask_firestore_api

<p2> Obra a Maos </p2>

<h1> 
<img src=https://giphy.com/embed/o28elTLxOjiRW width="300px"/> 
</h1>

<h2>criar o ambiente virtual</h2>
python3 -m venv venv

<h2>Acessar o ambiente virtual</h2>
source venv/bin/activate

<h2>instalar dependecia</h2>
pip install -r req.txt

<h2>arquivo de configuraca</h2>
app/__init__.py

<h2>Baixa e adicionar o arquivo com as credencial do google, linha</h2>
cred = credentials.Certificate('./firebase-admin.json')

<h2>executar na porta 808</h2>
python run.py

<h2>Segue payloads, collection a ser criada ja definida no app/__init__.py chamada users</h2>

<h2>ad</h2>
curl --location --request POST 'localhost:8080/add' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nome": "fabricio",
    "idade": 35,
    "cidade": "BA",
    "linguagens": ["Java script","Java"]
}'

<h2>Lis</h2>
curl --location --request GET 'localhost:8080/list' 

<h2>list com argumento nom</h2>
curl --location --request GET 'localhost:8080/list?nome=fabricio' --data-raw ''

<h2>updat</h2>
curl --location --request PUT 'localhost:8080/update' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id": "fD6BFOBmVsIbUjY7OUFq" ,
    "nome": "ronaldo",
    "idade": 32,
    "cidade": "SP",
    "linguagens": ["python"]
}'

<h2>delete com argumento i</h2>
curl --location --request DELETE 'localhost:8080/delete?id=60LnTY0jSTmibWSc3b5S' \
--data-raw ''

<h2>deletar todo</h2>
curl --location --request DELETE 'localhost:8080/delete?id=all' \
--data-raw ''

<h2>Pontos a melhora</h2>
- msg de erro
- filtro
- output de logs 
- uso de OOP
- adicionar wsgi