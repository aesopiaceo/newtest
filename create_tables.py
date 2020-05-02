#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:12:37 2020

@author: eddomboAesopia
"""

import sqlite3



connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE if NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)"  # AUTO-INCREMENTING ID
cursor = connection.execute(create_table)

create_table = "CREATE TABLE if NOT EXISTS items(id INTEGER PRIMARY KEY, name text, price real)"  
cursor = connection.execute(create_table)

connection.commit()
connection.close()

