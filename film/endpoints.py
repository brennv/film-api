from .config import amazon_access, amazon_secret, amazon_tag
from flask_restful import Resource
from amazon.api import AmazonAPI
import urllib
# from concurrent.futures import ThreadPoolExecutor

amazon = AmazonAPI(amazon_access, amazon_secret, amazon_tag)


def make_film(film):
    film = {'asin': film.asin,
            'actors': film.actors,
            'directors': film.directors,
            'genre': film.genre,
            'offer_url': film.offer_url,
            'product_group': film.product_group,
            'product_type_name': film.product_type_name,
            'studio': film.studio,
            'title': film.title,
            'large_image_url': film.large_image_url,
            'medium_image_url': film.medium_image_url,
            'small_image_url': film.small_image_url,
            'tiny_image_url': film.tiny_image_url}
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
        Search films
        ---
        tags:
          - films
        parameters:
          - name: id
            in: path
            type: string
            required: true
            default: bill murray
        responses:
         200:
           description: Search films
        """
        return get_film(id), 200
