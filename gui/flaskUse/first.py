from flask import request,render_template
import flask

app = flask.Flask(__name__,template_folder="templates")
app.config['DEBUG']=True

@app.route('/')

def signin():
    return render_template('signin.html')


@app.route('/index',methods=["POST"])
def index():
    name=request.form['email']
    password=request.form['password']
    return render_template('index.html',name=name,password=password)
app.run()

dict_all = [    {
        'name': 'himal',
        'roll': 21,
        'place':'nepal',
},
{
    'name': 'Sakar',
    'roll': 22,
    'place':'nepal',
    },
{
    'name': 'Asok',
    'roll': 23,
    'place':'nepal',
},
{
    'name': 'sabin',
    'roll': 24,
    'place':'nepal',
},
{
    'name': 'himal',
    'roll': 25,
    'place':'nepal'
}
]

print(dict_all)