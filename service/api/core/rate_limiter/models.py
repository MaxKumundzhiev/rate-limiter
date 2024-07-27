from datetime import datetime

from pydantic import BaseModel


class ToRateLimiter(BaseModel):
    user_id: str
    request_time: datetime