from .config import amazon_access, amazon_secret, amazon_tag
from flask_restful import Resource
from amazon.api import AmazonAPI
import urllib
# from concurrent.futures import ThreadPoolExecutor

amazon = AmazonAPI(amazon_access, amazon_secret, amazon_tag)


def make_film(film):
    film = {'id': film.asin,
            'title': film.title,
            'actors': film.actors,
            'directors': film.directors,
            'genre': film.genre,
            'product_group': film.product_group,
            'studio': film.studio,
            'url': film.offer_url,
            'image': film.large_image_url}
    return film


def get_film(id):
    film = {}
    try:
        response = amazon.lookup(ItemId=id)
        film = make_film(response)
    except urllib.error.HTTPError:
        # TODO https://stackoverflow.com/questions/25344610/python-http-error-503-service-unavailable
        pass
    return film


def search_films(keywords, index='Movies'):
    films = []
    results = amazon.search(Keywords=keywords, SearchIndex=index)
    # with ThreadPoolExecutor() as executor:
    try:
        for r in results:
            film = make_film(r)
            films.append(film)
            # print(item, '\n')
    except urllib.error.HTTPError:
        pass
    return films


def get_film_title(id):
    result = {}
    try:
        response = amazon.lookup(ItemId=id)
        result = {'title': response.title}
    except urllib.error.HTTPError:
        pass
    return result


def get_film_actors(id):
    result = {}
    try:
        response = amazon.lookup(ItemId=id)
        result = {'actors': response.actors}
    except urllib.error.HTTPError:
        pass
    return result


def get_film_directors(id):
    result = {}
    try:
        response = amazon.lookup(ItemId=id)
        result = {'directors': response.directors}
    except urllib.error.HTTPError:
        pass
    return result


def get_film_image(id):
    result = {}
    try:
        response = amazon.lookup(ItemId=id)
        result = {'image': response.large_image_url}
    except urllib.error.HTTPError:
        pass
    return result


class Health(Resource):
    def get(self):
        """
        API health check
        ---
        tags:
          - admin
        responses:
         200:
           description: Status check
           schema:
             id: Status
             properties:
               status:
                 type: string
                 description: Health status of API service
                 default: ok
        """
        return {'status': 'ok'}, 200


class FilmSearch(Resource):
    def get(self, term):
        """
        Search films
        ---
        tags:
          - films
        parameters:
          - name: term
            in: path
            type: string
            required: true
            default: bill murray
        responses:
         200:
           description: Search films
        """
        return search_films(term), 200


class Film(Resource):
    def get(self, id):
        """
        Film lookup
        ---
        tags:
          - films
        parameters:
          - name: id
            in: path
            type: string
            required: true
            default: B0053ZTZNK
        responses:
         200:
           description: Film lookup
        """
        return get_film(id), 200


class FilmActors(Resource):
    def get(self, id):
        """
        Actors
        ---
        tags:
          - films
        parameters:
          - name: id
            in: path
            type: string
            required: true
            default: B0053ZTZNK
        responses:
         200:
           description: Actors
        """
        return get_film_actors(id), 200


class FilmDirectors(Resource):
    def get(self, id):
        """
        Directors
        ---
        tags:
          - films
        parameters:
          - name: id
            in: path
            type: string
            required: true
            default: B0053ZTZNK
        responses:
         200:
           description: Directors
        """
        return get_film_directors(id), 200



class FilmTitle(Resource):
    def get(self, id):
        """
        Title
        ---
        tags:
          - films
        parameters:
          - name: id
            in: path
            type: string
            required: true
            default: B0053ZTZNK
        responses:
         200:
           description: Title
        """
        return get_film_title(id), 200


class FilmImage(Resource):
    def get(self, id):
        """
        Image
        ---
        tags:
          - films
        parameters:
          - name: id
            in: path
            type: string
            required: true
            default: B0053ZTZNK
        responses:
         200:
           description: Image
        """
        return get_film_image(id), 200
