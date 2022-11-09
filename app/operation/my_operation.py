from app import collection_bd, firestore

def criar(payload, nome):
    id = collection_bd.document().id
    payload.update({"created": firestore.SERVER_TIMESTAMP,"update": firestore.SERVER_TIMESTAMP, "id": id})
    collection_bd.document(id).set(payload)
    filtro_list = collection_bd.where("nome", "==", nome).get()
    my_list = []
    for filtro in filtro_list:
        my_list.append(f'{filtro.id} => {filtro.to_dict()}')
    if not my_list:
        return "Created"
    else:
        return my_list

def ler(nome):
    my_list = []
    todo = collection_bd.where("nome", "==", nome).get()
    for doc in todo:
        my_list.append(f'{doc.id} => {doc.to_dict()}')
    return my_list

def atualizar(payload, id):
    payload.update({ "update": firestore.SERVER_TIMESTAMP })
    collection_bd.document(id).update(payload)
    return payload
