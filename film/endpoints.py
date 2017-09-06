from .config import tag
from flask_restful import Resource


def film_search(term):
    url = 'http://test'
    if tag:
        url = url + tag
    return {'search': term, 'url': url}


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
        return film_search(term), 200
