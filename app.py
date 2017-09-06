from film.config import swagger_config, template, debug, threaded
from film.endpoints import Health, FilmSearch
from flask import Flask, jsonify, redirect
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app, template=template, config=swagger_config)

api.add_resource(Health, '/api/health')
api.add_resource(FilmSearch, '/api/films/search/<string:term>')


@app.route('/')
def index():
    return redirect('/api/spec/')


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": "Not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, threaded=False)
