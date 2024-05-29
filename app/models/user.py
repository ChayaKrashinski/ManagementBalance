from pydantic import BaseModel

class User(BaseModel):
    id:int
    name: str = ""
    password: str = ""
    mail: str = ""

