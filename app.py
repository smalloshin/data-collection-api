import os
from flask import Response, Flask, redirect, url_for, request, render_template,jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

# this is for docker. please change the client to the connection string you want.
client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],27017)

@app.route('/data_collection', methods=['GET'])
def data_collection():
    try:
        target_db = request.args.get("db",default="default_db")
        target_collection = request.args.get("collection",default="default_collection")   

        item_doc = dict()
        for x in request.args:
            item_doc[x]=request.args.get(x)
    
        db = client[target_db]
        db[target_collection].insert_one(item_doc)
       
        content = {'Status':'Data Inserted.'}
        return jsonify(content),201
    except Exception as e:
        content = {'Exception':str(e)}
        return jsonify(content),500

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
