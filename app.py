import os

from flask import Flask
from flask_restful import Api # Dont have to use jsonify, flask_restful does that for us.
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #extension behavior change.
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) # creates new endpoint/route : /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__': #If this file is being executed by something else, lika an import, the next row will not be executed.
    from db import db
    db.init_app(app) 
    app.run(port=5000, debug=True)
