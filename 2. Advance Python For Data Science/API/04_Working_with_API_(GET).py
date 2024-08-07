from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://root:mechengg.nagpur@cluster0.kxerjso.mongodb.net/?retryWrites=true&w=majority")
db = client.test

@app.route("/test_get")
def test_get() :
    return("This is my first function to get")

@app.route("/test2_get")
def test2_get() :
    name = request.args.get('name')
    contact_no = request.args.get('No.')
    Email_ID = request.args.get('Email')
    return ("This is the second function to get {} {} {}".format(name,contact_no,Email_ID))
# http://127.0.0.1:5002/test2_get?name=Kunal%20Kalkotwar&No.=8766961829&Email=kunalkalkotwar21@gmail.com
"""
TASK - Write a function in python to fetch the table from MySQL/MongoDB via Browser
(This task has very extensive use in our day to day life)
"""
@app.route("/fetch")
def fetch():
    database = request.args.get("database")
    mongo_database = client[database]
    collection = request.args.get("collection")
    mongo_collection = mongo_database[collection]
    fetch = mongo_collection.find()
    l = []
    for i in fetch:
        l.append(i)
        print(l)
    return (str(l))
# http://127.0.0.1:5002/fetch?database=<database_name>&collection=<collection_name>

if __name__ == "__main__" :
    app.run(port= 5002)