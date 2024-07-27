from datetime import datetime

from fastapi import FastAPI

from api.core.rate_limiter.fixed_window import FixedWindowRateLimiter
from api.core.rate_limiter.models import ToRateLimiter
from api.feed.models import Response


application = FastAPI()
rate_limiter = FixedWindowRateLimiter()


@application.get("/feed/{user_id}/")
async def get(user_id: str):
    request = ToRateLimiter(
        user_id=user_id, request_time=datetime.now()
    )
    is_limited, counter = rate_limiter.process(request=request)
    return Response(
        user_id=user_id,
        requests=counter,
        allowed_to_redirect=is_limited
    )