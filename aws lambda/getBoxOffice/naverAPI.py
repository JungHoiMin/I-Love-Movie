import json
import urllib.request
import urllib.parse


def getMovieImgUrl(movieName: str) -> str:
    # naver api 받아오기
    naver_client_id = "aWy0k8NDijglh9PlJsXn"
    naver_client_secret = "knBqRgvf5h"
    naver_url = "https://openapi.naver.com/v1/search/movie.json"
    query = urllib.parse.quote(movieName)
    naver_request = urllib.request.Request(naver_url + '?query=' + query + '&filter=small')
    naver_request.add_header("X-Naver-Client-Id", naver_client_id)
    naver_request.add_header("X-Naver-Client-Secret", naver_client_secret)
    naver_response = urllib.request.urlopen(naver_request)
    naver_json = json.loads(naver_response.read())

    movie_item = naver_json['items'][0]
    movie_image_url = movie_item['image']
    return movie_image_url

