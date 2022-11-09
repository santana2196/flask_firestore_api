from flask import Flask
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)

cred = credentials.Certificate('./firebase-admin.json')
default_app = initialize_app(cred)
db = firestore.client()
collection_bd = db.collection('users')

from app import views