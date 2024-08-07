from flask import Flask, jsonify, request
import pymongo


app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://root:mechengg.nagpur@cluster0.kxerjso.mongodb.net/?retryWrites=true&w=majority")
db = client.test

"""data = [
    {
        "name":"Kunal",
        "age":26,
        "email_id":"kunalkalkotwar21@gmail.com",
        "contact_no":"8766961829"
    },
    {
        "name":"Shubham",
        "age":24,
        "email_id":"shubhamkalkotwar21@gmail.com",
        "contact_no":"8745461829"
    },
    {
        "name":"Neha",
        "age":25,
        "email_id":"nehakalkotwar21@gmail.com",
        "contact_no":"8763421829"
    }
]"""

database = client['Sample_Database']
collection = database['Sample_Table']
# collection.insert_many(data)                  #After Inserting the data we can comment out this line as further we need not to enter data
# Fetching records
# collection.drop()                             # For Dropping the collection.
"""fetch = collection.find()
for i in fetch:
    print(i)"""

# Inserting the new records into database
@app.route('/insert/mongo', methods = ['GET','POST'])
def insert():
    if (request.method=="POST") :
        name = request.json['name']
        age = request.json['age']
        email_id = request.json['email_id']
        contact_no = request.json['contact_no']
        collection.insert_one({"name":name , "age":age , "email_id":email_id , "contact_no":contact_no})
        return (jsonify(str("Insertion Successful")))

@app.route('/update/mongo', methods = ['GET','POST'])
def update():
    if (request.method == "POST") :
        name = request.json['name']
        age = request.json['age']
        collection.update_many({"name":name},{"$set":{"age":age}})
        return (jsonify(str("Record Updatation Successful")))

@app.route("/fetch/mongo", methods = ['POST','GET'])
def fetch():
    if (request.method == "POST") :
        fetch = collection.find()
        l = []
        for i in fetch:
            l.append(i)
            print(l)
        return (jsonify(str(l)))

if __name__ == "__main__" :
    app.run(port=5001)




