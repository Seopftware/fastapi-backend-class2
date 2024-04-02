from pydantic import BaseModel
from typing import List
from typing import Optional

# schemas/item.py
# schemas/user.py

# pydantic -> 데이터 유효성 검증
class ItemBase(BaseModel):
    title: str
    description: str

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True # orm 방식으로 데이터 필드 읽기가 가능

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    title: Optional[str] = None
    description: Optional[str] = None

class UserBase(BaseModel):
    email: str

class User(UserBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    hashed_password: str

class UserUpdate(UserBase):
    # email: str | None = None # 3.10부터... | 등장.
    email: Optional[str] = None # 3.10부터... | 등장.
    hashed_password: Optional[str] = None

# 그럼 api 만 잘 해도 잔고랑 뭐 다른건 공부 안해도 될까여,,
# - 백엔드 신입 최소 조건, 역량 + Auth + DB (NoSQL)
# - 면접 라이브 코딩 => 검색: 네이버 검색(기본 검색: 구글, bing)
# 시작 연봉
# REST API + DB(SQL) + AUTH + DB(NoSQL) + 기술(Chatting, Streaming .. )