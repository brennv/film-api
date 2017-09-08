from film.config import swagger_config, template, debug, threaded
from film.endpoints import (Health, Film, FilmSearch, FilmImage, FilmTitle,
                            FilmActors, FilmDirectors)
from flask import Flask, jsonify, redirect
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app, template=template, config=swagger_config)

api.add_resource(Health, '/api/health')
api.add_resource(Film, '/api/film/<string:id>')
api.add_resource(FilmTitle, '/api/film/<string:id>/title')
api.add_resource(FilmActors, '/api/film/<string:id>/actors')
api.add_resource(FilmDirectors, '/api/film/<string:id>/directors')
api.add_resource(FilmImage, '/api/film/<string:id>/image')
api.add_resource(FilmSearch, '/api/films/search/<string:term>')


@app.route('/')
def index():
    return redirect('/api/spec/')


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": "Not found"}), 404


if __name__ == '__main__':
    app.run(debug=debug, threaded=threaded)
