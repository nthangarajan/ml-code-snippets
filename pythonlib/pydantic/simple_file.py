from pydantic import BaseModel

class Person(BaseModel):
    first_name: str
    last_name: str