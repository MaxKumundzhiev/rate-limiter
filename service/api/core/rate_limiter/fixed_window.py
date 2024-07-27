from uuid import UUID
from datetime import datetime



class FixedWindowRateLimiter:
    def __init__(self) -> None:
        self.requests_limit_per_minute_per_user = 10
        self.storage = {}
    
    def process(
        self, user_id: UUID, request_time: datetime
    ) -> bool:

        user_exists = self.storage.get(user_id, False)

        if not user_exists:
            self.storage[user_id] = ...