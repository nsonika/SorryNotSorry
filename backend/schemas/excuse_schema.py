from pydantic import BaseModel

class ExcuseRequest(BaseModel):
    category: str
    humor_level: int
    custom_context: str = None

class ExcuseResponse(BaseModel):
    excuse: str
