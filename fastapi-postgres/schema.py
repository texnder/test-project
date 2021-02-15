from pydantic import BaseModel

class UserBase(BaseModel):
    id: int
    username: str
    
class UserCreate(UserBase):
    password: str


class PostCreate(BaseModel):
    title: str
    caption: str
    body: str
    user_id: int
