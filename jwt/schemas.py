from pydantic import BaseModel

class UserCreate:
    full_name: str
    email:str
    password :str