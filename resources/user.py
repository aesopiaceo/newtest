#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 00:06:05 2020

@author: eddomboAesopia
"""

from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',
                    type=str,
                    required=True,
                    help="Username field cannot be left blank!"
    )
    parser.add_argument('password',
                    type=str,
                    required=True,
                    help="Password field cannot be left blank!"
    )
    def post(self):    
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data["username"]): 
            return {"message": "User already exists."}, 400 # bad request
   
        user = UserModel(**data)
        user.save_to_db()
        return {"message": "User created successfully."}, 201
    
        
        
        
    
        