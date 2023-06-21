from flask import Flask, url_for, request, render_template
from markupsafe import escape

app = Flask(__name__)

pets = [
    {"id": 1,
     "name": "soup"}
]

@app.route('/add/<name>', methods=['POST'])
def add_pet(name):
    pets.append({"id": len(pets)+1,"name":name})
    return "added " + name 

@app.route('/show', methods=['GET'])
def show_pet():
    return pets

@app.route('/yeet/<name>', methods=['DELETE'])
def yeet_pet(name):
    for p in pets:
        if p["name"] == name:
            pets.remove(p)
    return name + " is no longer with us"


@app.route('/rename/<oldname>/<newname>', methods=['PUT'])
def rename_pet(oldname,newname):
    for p in pets:
        if p["name"] == oldname:
            p["name"] = newname
    return oldname + " has been reborn as " + newname