import os

host = os.getenv('FILM_API_HOST', '127.0.0.1:5000')
scheme = [x for x in [os.getenv('FILM_API_SCHEME', '')] if x]
tag = os.getenv('AMAZON_ID_TAG')

template = {
  # "host": "film.vonapp.co",
  "host": host,
  # "schemes": ["https"],
  # "schemes": scheme,
  "schemes": ["https", "http"],
  "swagger": "2.0",
  "info": {
    "title": "Filmography API",
    "description": "API endpoints for film.vonapp.co",
    "version": "0.1.0"
  },
  "basePath": "/",
  "operationId": "get_data",
  # set tag order
  "tags": [
      {"name": "admin", "description": ""},
      {"name": "film", "description": ""},
  ]
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'spec',
            "name": 'film',
            "route": '/api/spec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/api/spec/",
    'title': 'Filmography API',
}

if host == '127.0.0.1:5000':
    debug = True
    threaded = False
else:
    debug = False
    threaded = True

print(' * Host:', host)
print(' * Scheme:', scheme)
print(' * Amazon tag:', tag)
print(' * Debug:', debug)
print(' * Threaded:', threaded)
