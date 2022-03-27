from fastapi import FastAPI

from app.util.kakao_map_api import KakaoMapAPI

app = FastAPI()


@app.get('/')
async def root():
    return {
        'Hello': 'World!'
    }


@app.post('/api/v1/test/search/keyword')
async def search_keyword(keyword: str, page_num: int,
                         latitude: float, longitude: float, radius: int):
    kakao_map = KakaoMapAPI(latitude, longitude)

    return await kakao_map.search_keyword_within_radius(keyword=keyword, page_num=page_num, radius=radius)
