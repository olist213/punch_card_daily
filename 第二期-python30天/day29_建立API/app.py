from flask import Flask, Response
import json
import os

app = Flask(__name__)

@app.route('/api/v1.0/students', methods=['GET'])

def students():
    
    student_list = [
        {
            'name':'liangcheng',
            'country':'china',
            'city':'xxx',
            'skills':['html','css','javascript','python']
        },
        {
            'name':'zhangsan',
            'country':'china',
            'city':'beijing',
            'skills':['php','mysql','apache']
        },
        {
            'name':'lisi',
            'country':'china',
            'city':'shanghai',
            'skills':['nging','java','c']
        }
    ]
    
    return Response(json.dumps(student_list), mimetype='application/json')

if __name__ == '__main__':
    
    port = int(os.environ.get("PORT",6000))
    app.run(debug=True, host='0.0.0.0', port=port)