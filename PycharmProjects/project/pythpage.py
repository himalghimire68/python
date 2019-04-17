import flask
from flask import render_template,request,jsonify
import imdb
from imdb import IMDbError

ia=imdb.IMDb()


############
movie = flask.Flask(__name__ ,template_folder="templates")
movie.config['DEBUG']=True
try:
    @movie.route('/')
    def index():
        return render_template('index.html')


    @movie.route('/',methods=["POST"])


    def abc():

        s_result = ia.search_movie(request.form['search_name'])
    # First In List
        the_unt = s_result[0]
        ia.update(the_unt)

        info = {

            "year": the_unt['year'],
            "name": the_unt['title'],
            "thumb": the_unt['cover url'],
            "maincharacter1": the_unt['cast'][0],
            "maincharacter2": the_unt['cast'][1],
            "director": the_unt['director'][0],
            "runtime": the_unt['runtime'],
            "rating": the_unt['rating']
        }
        return render_template('index.html',info=info)


except IMDbError as e:
    print(e)

    #################



movie.run(host='127.0.0.1',port='5003')
