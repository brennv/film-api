from .config import amazon_access, amazon_secret, amazon_tag
from flask_restful import Resource
from amazon.api import AmazonAPI
# from concurrent.futures import ThreadPoolExecutor

amazon = AmazonAPI(amazon_access, amazon_secret, amazon_tag)


def get_films(keywords, index='Movies'):
    films = []
    results = amazon.search(Keywords=keywords, SearchIndex=index)
    # with ThreadPoolExecutor() as executor:
    for r in results:
        try:
            item = {}
            item['actors'] = r.actors
            item['directors'] = r.directors
            item['genre'] = r.genre
            item['offer_ur'] = r.offer_url
            item['product_group'] = r.product_group
            item['product_type_name'] = r.product_type_name
            # item['release_date'] = r.release_date
            item['studio'] = r.studio
            item['title'] = r.title
            item['large_image_url'] = r.large_image_url
            item['medium_image_url'] = r.medium_image_url
            item['small_image_url'] = r.small_image_url
            item['tiny_image_url'] = r.tiny_image_url
            films.append(item)
            print(item, '\n')
        except HTTPError as e:
            # print(e)
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
        return get_films(term), 200
