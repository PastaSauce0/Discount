from flask import Flask, jsonify
from pymongo import MongoClient
import certifi
import datetime
from flask import request
import json
from bson.json_util import dumps

client = MongoClient("mongodb+srv://admin:###@cluster0.nknoe.mongodb.net/Cluster0?retryWrites=true&w=majority", tlsCAFile=certifi.where())
# db = client.test
db = client.gettingStarted
people = db.people


app = Flask(__name__)

def parse_json(data):
 return json.loads(dumps(data))

@app.route('/insert', methods = ['POST'])

def get_articles():
 data = request.get_json()

 personDocument = {
  "name": { "first": data['first'], "last": data['last'] },
  "birth": datetime.datetime(1912, 6, 23),
  "death": datetime.datetime(1954, 6, 7),
  "contribs": [ "Turing machine", "Turing test", "Turingery" ],
  "views": 1250000
 }
 people.insert_one(personDocument)
 return data



@app.route('/filter', methods = ['POST'])

def filter_articles():
 found = people.find(
  {
   "name.first":"Alan"
  }
 )

 return jsonify(parse_json(found))


if __name__ == "__main__":
 app.run(debug=True)
 
 
 
 
 
