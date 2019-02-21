from flask import request,render_template,jsonify
import flask
from first import  dict

app = flask.Flask(__name__)
app.config['DEBUG']=True

@app.route('/',methods=['GET'])

def signin():
    return "Hello"


@app.route('/index',methods=["GET"])
def api_all():
    return jsonify(dict_all)
app.run()