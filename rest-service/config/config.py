from flask_rebar import Rebar
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from flask import Flask

# App
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Versioning
rebar = Rebar()
v1_registry = rebar.create_handler_registry(prefix='/v1')
mimetype_json = 'application/json'

# Persistence
client = MongoClient()
db: Database = client.get_database("test")
cow_collection: Collection = db.get_collection("cow")