# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:50:32 2021

@author: utilisateur
"""

from pymongo import MongoClient
from flask import Flask
from flask import request
app = Flask(__name__)
client = MongoClient('146.59.153.190', 5555)
db = client["Import_Cadastre"]
collection = db["Cadastre_Fr_Parcelles"]

def find_parcelles(city, prefix, section, number):
    #result = collection.find({"properties.commune":city,"properties.prefixe":prefix,"properties.section":section,"properties.numero":number}) #ligne qui appelle MongoDB
    result=city+prefix+section+number
    return result

@app.route("/")
def test():
    return "OK"

@app.route("/parcelles")
def job():
    city = request.args.get('commune')
    prefix = request.args.get('prefixe')
    section = request.args.get('section')
    number = request.args.get('numero')
    result = find_parcelles(city, prefix, section, number)
    return result

app.run(debug=True)