import aiohttp

from app.config import settings


KEYWORD_SEARCH_URL = 'https://dapi.kakao.com/v2/local/search/keyword.json'


class KakaoMapAPI:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    async def search_keyword_within_radius(self, keyword: str, page_num: int, radius: int):
        places = []
        async with aiohttp.ClientSession() as session:
            async with session.get(KEYWORD_SEARCH_URL, params={
                'query': keyword,
                'page': page_num,
                'x': self.longitude,
                'y': self.latitude,
                'radius': radius
            }, headers={
                'Authorization': 'KakaoAK ' + settings.KAKAO_API_KEY
            }) as response:

                places = await response.json()

        return places['documents']
