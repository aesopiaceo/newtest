#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:11:39 2020

@author: eddomboAesopia
"""

from flask import Flask #request
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from db import db


    
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.secret_key='eddombo'
api=Api(app)



jwt = JWT(app, authenticate, identity)   #JSON Web Token (JWT) - creates a /auth endpoint
                
@app.before_first_request
def create_tables():
    db.create_all()
    
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList,'/items')

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister,'/register')

if __name__ == '__main__':  # this means this app will not run unless it is main that is being run
    db.init_app(app)
    app.run(port=5000, debug=True)

