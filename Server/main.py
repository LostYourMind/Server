
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import sys
from DBControl import connect_db, disconnect_db, fetch_one

# FastAPI 앱 인스턴스를 생성
app = FastAPI()

# CORS(Cross-Origin Resource Sharing) 설정 코드
# 이 설정은 다른 출처(origin)에서도 이 API 서버로 요청을 보낼 수 있게 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 출처에서의 요청을 허용
    allow_credentials=False,  # 크로스 오리진 요청 시 쿠키를 지원
    allow_methods=["*"],  # 모든 HTTP 메소드를 허용
    allow_headers=["*"],  # 모든 헤더를 허용
)

@app.router.lifespan.on_event("startup")
async def startup_event():
    await connect_db()

@app.router.lifespan.on_event("shutdown")
async def shutdown_event():
    await disconnect_db()

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    query = "SELECT * FROM users WHERE id = :user_id"
    user = await fetch_one(query=query, values={"user_id": user_id})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


#Main End Point
@app.get("/")
def read_root():
    return {"Hello": "World"}

#Test End Point
@app.get("/run-script")
async def run_script():

    # 외부 Python 스크립트 경로
    script_path = "C:\Users\WSU\Documents\GitHub\Caps\Main\Main.py"
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True, encoding='utf-8')

    # 실행 결과 반환
    if result.returncode == 0:  # 성공
        print({"output": result.stdout})
        return {"output": result.stdout}

    else:  # 실패
        print({"error": result.stderr})
        return {"error": result.stderr}

