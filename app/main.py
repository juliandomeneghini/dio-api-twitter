from typing import List

import uvicorn
from fastapi import FastAPI
from src.responses import TrendItem
from src.services import get_trending_topics


app = FastAPI()


@app.get("/trends", response_model=List[TrendItem])
def get_trends_route():
    return get_trending_topics()


uvicorn.run(app, host="0.0.0.0", port=8080)
