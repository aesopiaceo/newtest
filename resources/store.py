#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:55:30 2020

@author: eddomboAesopia
"""


from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        
        return {'message': 'No store by the name {}'.format(name)}, 404
    
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'A store by the name {} already exists'.format(name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
            
        except:
            return {'message': 'Error adding store!'}
        
        return store.json(), 201
    
    
    def delete(self, name):
        if StoreModel.find_by_name(name):
            try:
                StoreModel.delete_from_db(self)
                return {'message': 'Store removed!'}, 201
            except:
                return {'message': 'Unable to remove store!'}, 404
        return {'message':'Store was not found'}, 404   
        

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
