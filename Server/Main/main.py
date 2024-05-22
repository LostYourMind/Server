import logging
import sys
import os

sys.path.append('../')  # 상위 디렉터리 추가

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from API_CODE.Control.Main_Control import Control
from DBConn.DBControl import DataBaseControl

app = FastAPI()

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CORS 설정 코드
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 출처에서의 요청을 허용
    allow_credentials=True,  # 크로스 오리진 요청 시 쿠키를 지원
    allow_methods=["*"],  # 모든 HTTP 메소드를 허용
    allow_headers=["*"],  # 모든 헤더를 허용
)

class Message(BaseModel):
    text: str
    sender: str
    id: int

# Server startup & shutdown Code
@app.on_event("startup")
def startup():
    db_control = DataBaseControl(user='fastAPI', password='blue1774!')
    try:
        conn = db_control.connect_db()
        logger.info("FastAPI 서버 시작")
    except Exception as e:
        logger.error(f"Error during startup: {e}")
        raise HTTPException(status_code=500, detail="Database connection failed")

@app.post("/users/ai")
async def Menu_Recomm(message: Message, user: str = "fastAPI", password: str = "blue1774!"):
    logger.info(f"/users/ai : Post Request Start\n")
    logger.info(f"message : {message.text}")

    db_control = DataBaseControl(user, password)

    conn = None
    try:
        conn = db_control.connect_db()
        if conn is None:
            raise HTTPException(status_code=500, detail="Failed to connect to database")

        control_instance = Control(db_control)
        result = control_instance.Recomm_Menu(message.text, message.id)
        if isinstance(result, str):
            logger.info(f"/users/ai : {result}")
            return {"message": result}
        else:
            raise ValueError("Unexpected response format")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if conn:
            db_control.disconnect_db(conn)
