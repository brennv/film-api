# film-api

RESTful mash-up of theMovieDB and Amazon Product APIs http://film.vonapp.co

See: [film.vonapp.co](http://film.vonapp.co)

## Endpoints

### admin

GET **/api/health** API health check

### films

GET **/api/film/{id}** Film lookup

GET **/api/film/{id}/actors** Actors

GET **/api/film/{id}/directors** Directors

GET **/api/film/{id}/image** Image

GET **/api/film/{id}/title** Title

GET **/api/films/search/{term}** Search films

## Example film object

```json
{
    "id": "B0053ZTZNK",
    "title": "The Man Who Knew Too Little",
    "actors": [
        "Bill Murray",
        "Peter Gallagher",
        "Joanne Whalley",
        "Alfred Molina",
        "Richard Wilson"
    ],
    "directors": [
        "Jon Amiel"
    ],
    "genre": "Action - Crime",
    "product_group": "Movie",
    "studio": "Warner Bros.",
    "running_time": "93",
    "release_date": "2010-12-01",
    "url": "http://www.amazon.com/dp/B0053ZTZNK/?tag=von0d7-20",
    "image": "https://images-na.ssl-images-amazon.com/images/I/51FULcd7mML.jpg",
    "reviews": "https://www.amazon.com/reviews/iframe?akid=AKIAJIOBB5G7XTECPIMA&alinkCode=xm2&asin=B0053ZTZNK&atag=von0d7-20&exp=2017-09-09T15%3A41%3A04Z&v=2&sig=wLU%252Fy0WPSplpRE5DBHIBMQoJ%252BPrW0TBj%252F06In6GSm1o%253D"
}
```
