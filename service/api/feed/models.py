from pydantic import BaseModel


class Request(BaseModel):
    user_id: str


class Response(BaseModel):
    user_id: str
    requests: int
    allowed_to_redirect: bool


