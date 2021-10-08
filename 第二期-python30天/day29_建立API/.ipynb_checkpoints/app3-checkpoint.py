from flask import Flask, render_template, Response
import os
import json
from bson import json_util
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo

app = Flask(__name__)

MONGODB_URL = 'mongodb+srv://dbliangcheng:vV43I6YdZrLlIvPi@pythonstudy.txiwo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URL)
db = client['thirty_days_of_python'] # 访问数据库

student = db.students.find()

s = json.loads(json_util.dumps(student))

@app.route('/api/v1.0/students', methods=['GET'])

def students():
    return Response(json.dumps(s), mimetype='application/json')

@app.route('/api/v1.0/students/<id>', methods=['GET'])

def single_student(id):
    stuednt = db.students.find({"_id":ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')

if __name__ == '__main__':
    port = int(os.environ.get("PORT",6000))
    app.run(debug=True, host='0.0.0.0', port=port)