from flask import request,render_template,jsonify
import flask
from dictfile import *

applic= flask.Flask(__name__)
applic.config['DEBUG']=True

@applic.route('/',methods=['GET'])
def show():
    return 'Hello'

@applic.route('/index',methods=['GET'])
def display():
    return jsonify(dict_all)

@applic.route('/book',methods=['GET'])
def api_id():
    if 'roll' in request.args:
        id=int(request.args['roll'])
    else:
        return "<h1>Sorry Wrong id</h1>"
    res=[]
    for book in dict_all:
        if id==book['roll']:
            res.append(book)

    return jsonify(res)


applic.run(host='127.0.0.1',port='5002')