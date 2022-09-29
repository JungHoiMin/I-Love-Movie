import json
from datetime import date, timedelta
import urllib.request
import urllib.parse


def getMoviesInfo() -> list:
    # boxoffice api 받아오기
    boxoffice_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?"
    boxoffice_key = "b8fee7ef050ac2d302137ceb102efd84"

    yesterday = date.today() - timedelta(1)
    boxoffice_targetDt = yesterday.strftime('%Y%m%d')
    boxoffice_request = urllib.request.Request(
        boxoffice_url + "key=" + boxoffice_key + "&targetDt=" + boxoffice_targetDt)
    boxoffice_response = urllib.request.urlopen(boxoffice_request)

    boxoffice_json = json.loads(boxoffice_response.read())

    cards = list()
    for top in boxoffice_json['boxOfficeResult']['dailyBoxOfficeList']:
        cards.append({
            'imageUrl': "이미지 URL(Naver api로 받아올 예정)",
            'description': top['movieNm'],
            'title': 'TOP' + str(top['rank'])
        })
    return cards
