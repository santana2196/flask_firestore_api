# flask_firestore_api

# criar o ambiente virtual 
python3 -m venv venv

# Acessar o ambiente virtual 
source venv/bin/activate

# instalar dependecias
pip install -r req.txt

# arquivo de configuracao
app/__init__.py

# Baixa e adicionar o arquivo com as credencial do google, linha 
cred = credentials.Certificate('./firebase-admin.json')

# executar na porta 8080
python run.py

# Segue payloads, collection a ser criada ja definida no app/__init__.py chamada users:

# add
curl --location --request POST 'localhost:8080/add' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nome": "fabricio",
    "idade": 35,
    "cidade": "BA",
    "linguagens": ["Java script","Java"]
}'

# List
curl --location --request GET 'localhost:8080/list' 

# list com argumento nome
curl --location --request GET 'localhost:8080/list?nome=fabricio' --data-raw ''

# update
curl --location --request PUT 'localhost:8080/update' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id": "fD6BFOBmVsIbUjY7OUFq" ,
    "nome": "ronaldo",
    "idade": 32,
    "cidade": "SP",
    "linguagens": ["python"]
}'

# delete com argumento id
curl --location --request DELETE 'localhost:8080/delete?id=60LnTY0jSTmibWSc3b5S' \
--data-raw ''

# deletar todos
curl --location --request DELETE 'localhost:8080/delete?id=all' \
--data-raw ''

# Pontos a melhorar
- msg de erro
- filtro
- output de logs 
- uso de OOP
- adicionar wsgi