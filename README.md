uvicorn main:app --reload = 서버 구동

#외부 접근 가능한 서버 구동
uvicorn main:app --host 0.0.0.0 --port 8000 


https://www.weatherapi.com/my/fields.aspx
https://platform.openai.com/usage


pip list [
    pip install fastapi
    pip install pymysql
    pip install httpx
    pip install sqlalchemy
    pip install openai==0.28
    pip install pytz
]