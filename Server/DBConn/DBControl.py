import mysql.connector
from mysql.connector import Error

class DataBaseControl:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'fastAPI'
        self.password = 'blue1774!'
        self.database = 'caps'
        self.conn = None

    def connect_db(self):
        """데이터베이스 연결을 설정."""
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.conn.is_connected():
                print("Database connection started.")
            return self.conn
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    def disconnect_db(self):
        """데이터베이스 연결을 종료합니다."""
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Database connection closed.")
            
    def select_products_by_kiosk_id(self, kiosk_id):
        if not self.conn or not self.conn.is_connected():
            self.connect_db()
        
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.callproc('SelectAllKiosk', [kiosk_id])
            results = []
            for result in cursor.stored_results():
                results.extend(result.fetchall())
            cursor.close()
            return results
        except Error as e:
            print(f"Error executing procedure: {e}")
            return []
