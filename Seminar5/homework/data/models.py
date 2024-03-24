from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    password: Optional[str] = None
    
users = [
    User(id = 0, name = 'Dima', email= 'string@g.ru', password = '1111'),
    User(id = 1, name = 'Vova', email= 'vovv@g.ru', password = '234314'), 
    User(id = 2, name = 'Vera', email= 'gggv@g.ru', password = '3523'),     
]
