#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:23:09 2020

@author: eddomboAesopia
"""


from db import db
 

class UserModel(db.Model):   #helper class - not an actual resource
    __tablename__='users' 
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String (80))
    password = db.Column(db.String (80))


    def __init__(self, username,password):
        self.username=username
        self.password=password
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod  
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
        
    
    @classmethod 
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
