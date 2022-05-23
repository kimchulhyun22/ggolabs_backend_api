from fastapi import FastAPI

from app.db.init_db import init_db
from app.util.kakao_map_api import KakaoMapAPI
from app.api.api_v1.api import api_router
from app.core.config import settings

init_db()

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


app.include_router(api_router, prefix=settings.API_V1_PREFIX)
