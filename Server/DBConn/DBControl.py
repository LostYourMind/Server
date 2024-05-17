import mysql.connector
from mysql.connector import Error



class DataBaseControl :

    def connect_db(self):
        """데이터베이스 연결을 설정."""
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='fastAPI',
                password='blue1774!',
                database='caps'
            )
            if conn.is_connected():
                print("Database connection started.")
            return conn
        except Error as e:
            print(f"Error connecting to MySQL: {e}")

    def disconnect_db(self,conn):
        """데이터베이스 연결을 종료합니다."""
        if conn:
            conn.close()
            print("Database connection closed.")

    def select_all_users():
        try:
            conn = DataBaseControl.connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            users_list = cursor.fetchall()
            for user in users_list:
                print(user)
            return users_list
        finally:
            if conn:
                DataBaseControl.disconnect_db(conn)


