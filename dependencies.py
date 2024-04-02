from typing import Dict
from fastapi import Depends, HTTPException

# 하드코딩된 사용자 데이터 예시
users = {
    1: {"email": "user1@example.com"},
    2: {"email": "user2@example.com"},
    3: {"email": "user3@example.com"}
}

def get_current_username(token: str) -> str:
    try:
        user_id = int(token)  # 토큰을 사용자 ID로 간주
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid token format")

    user = users.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user["email"]  # 사용자의 이메일 반환