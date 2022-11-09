from flask import Flask, request, jsonify
from app import app, collection_bd
from .operation.my_operation import criar, ler, atualizar

@app.route('/add', methods=['POST'])
def create():
    try:
        nome = request.json['nome']
        req = request.json
        return_created = criar(req, nome)
        return jsonify({"success": return_created }), 200
    except Exception as e:
        return f"An Error Occurred: {e} {req}"

@app.route('/list', methods=['GET'])
def read():
    try:
        nome = request.args.get('nome')
        if nome == None:
            all_todos = [doc.to_dict() for doc in collection_bd.stream()]
            return jsonify(all_todos), 200
        else:
            return_list = ler(nome)
            return jsonify(return_list), 200        
    except Exception as e:
        return f"Msg de erro: {e}"

@app.route('/update', methods=['POST', 'PUT'])
def update():
    try:
        id = request.json['id']
        filtro = collection_bd.where("id", "==", id).get()
        if filtro == None:
            return jsonify({f"return": "Cliente nao localizado"}), 400
        else:
            atualizar(request.json, id)
            return jsonify({"update": "sucess"}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/delete', methods=['DELETE'])
def delete():
    try:
        id = request.args.get('id')
        print(id)
        if id == 'all':
            docs = collection_bd.stream()
            for doc in docs:
                collection_bd.document(doc.id).delete()
            return jsonify({ "Delete": "all"})
        elif id == None:
            return jsonify({ "Failed": "Favor inserir id, Exemplo: delete?id=dnfklsnfkdlnf"})
        else:
            todo = collection_bd.where("id", "==", id).get()            
            for doc in todo:
                key = doc.id
                print(collection_bd.document(key).delete())
            return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


