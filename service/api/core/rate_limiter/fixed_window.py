from datetime import datetime

from api.core.rate_limiter.models import ToRateLimiter


class FixedWindowRateLimiter:
    def __init__(self, limit: int = 10) -> None:
        self.limit = limit
        self.storage = {}
    
    def retrive_hour(self, time: datetime) -> str:
        """Method, which retrives hour from datetime in format of HH"""
        return time.hour
    
    def retrive_minute(self, time: datetime) -> str:
        """Method, which retrives minute from datetime in format of MM"""
        return time.minute

    def process(self, request: ToRateLimiter) -> bool:
        """
            Method, which processes income requests 
            and manages counter for certain user.
        """
        user_id = request.user_id
        hour, minute = self.retrive_hour(request.request_time), \
                       self.retrive_minute(request.request_time)
        interval, default_counter = f"{hour}:{minute}", 1

        if user_id not in self.storage:
            self.storage[user_id] = {interval:default_counter}
            return (True, counter)
        else:
            history = self.storage.get(user_id)
            counter = history.get(interval, False)

            #@TODO: add logic to reset counter

            # interval does not exists (no counter)
            if not counter:
                self.storage[user_id].update({interval:default_counter})
                return (True, default_counter)
            # interval exist (there counter with some value)
            else:
                counter += 1
                self.storage[user_id][interval] = counter
                if counter > self.limit:
                    return (False, counter)
                else:
                    return (True, counter)

