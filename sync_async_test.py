from fastapi import APIRouter
import time

router = APIRouter()

@router.get('/slow-sync-ping')
def slow_sync_ping():
    time.sleep(10)

    return {'msg':'pong'}

import asyncio
@router.get('/slow-async-ping')
async def slow_async_ping():
    await asyncio.sleep(10) # 10초를 기다린다. 근데 다른 작업들은 계속 실행이 된다.
    
    return {'msg':'pong'}