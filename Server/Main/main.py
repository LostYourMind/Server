import logging
import sys
import os

sys.path.append('../')  # 상위 디렉터리 추가

from DBConn.DBControl import DataBaseControl

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from concurrent.futures import ThreadPoolExecutor

from API_CODE.Control.Main_Control import Control

test = DataBaseControl()


#region Instance


# FastAPI 앱 인스턴스를 생성
app = FastAPI()


# Main_Control.Control 인스턴스 생성
control_Instance = Control()


# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# 전역으로 재사용할 데이터베이스 연결 객체
db_connection = None



#endregion

#region CORS 설정 코드

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 출처에서의 요청을 허용
    allow_credentials=False,  # 크로스 오리진 요청 시 쿠키를 지원
    allow_methods=["*"],  # 모든 HTTP 메소드를 허용
    allow_headers=["*"],  # 모든 헤더를 허용
)

#endregion

#region Server startup & shutdown Code

@app.on_event("startup")
def startup():
    global db_connection
    try:
        with ThreadPoolExecutor() as executor:
            db_connection = executor.submit(test.connect_db).result()
        logger.info("데이터베이스 연결이 성공적으로 시작되었습니다.")
    except Exception as e:
        logger.error(f"데이터베이스 연결 시작 실패: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.on_event("shutdown")
def shutdown():
    global db_connection
    try:
        with ThreadPoolExecutor() as executor:  
            executor.submit(test.disconnect_db, db_connection)
        logger.info("데이터베이스 연결이 성공적으로 종료되었습니다.")
    except Exception as e:
        logger.error(f"데이터베이스 연결 종료 실패: {e}")

#endregion

# #Test End Point
@app.post("/users/ai")
async def Menu_Recomm():
    logger.info("/users/ai : Post Request Start")

    #region 디버깅 코드
    # script_path = r"C:\Users\WSU\Documents\GitHub\Caps\Main\Main.py"
    # result = subprocess.run([sys.executable, script_path], capture_output=True, text=True, encoding='utf-8')
    #endregion

    try:
        result = control_Instance.Control_SrInput()
        # 실행 결과 반환
        if result.returncode == 0:  # 성공
            logger.info({"output": result.stdout})
            return {"output": result.stdout}

        else:  # 실패
            logger.error({"error": result.stderr})
            return {"error": result.stderr}
        
    except Exception as e :
        logger.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))
