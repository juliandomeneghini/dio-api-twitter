from typing import Optional, List

from pydantic import BaseModel


class TrendItem(BaseModel):
    name: str
    query: Optional[str] = None
    place: Optional[str] = None
    url: Optional[str] = None
    response: Optional[List[str]] = None
