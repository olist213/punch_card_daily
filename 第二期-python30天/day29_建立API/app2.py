from flask import Flask, render_template
import os
import json
import pymongo
from bson import json_util

app = Flask(__name__)

MONGODB_URL = 'mongodb+srv://dbliangcheng:vV43I6YdZrLlIvPi@pythonstudy.txiwo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URL)
db = client['thirty_days_of_python'] # 访问数据库

student = db.students.find()

s = json.loads(json_util.dumps(student))
print(s)

