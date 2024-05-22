import mysql.connector
from mysql.connector import Error

class DataBaseControl:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def connect_db(self):
        """데이터베이스 연결을 설정."""
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user=self.user,
                password=self.password,
                database='caps'
            )
            if conn.is_connected():
                print(f"Database connection started for user {self.user}.")
                return conn
            else:
                print("Database connection failed.")
                return None
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            raise

    def disconnect_db(self, conn):
        """데이터베이스 연결을 종료합니다."""
        if conn:
            conn.close()
            print("Database connection closed.")

    def select_products_by_kiosk_id(self, kiosk_id):
        conn = None
        try:
            conn = self.connect_db()
            if conn is None:
                raise Exception("Failed to connect to database.")
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('SelectAllKiosk', [kiosk_id])

            products = []
            for result in cursor.stored_results():
                products.extend(result.fetchall())

            # Product 값을 추출
            product_values = [product['product_name'] for product in products]

            return product_values
        except Error as e:
            print(f"Error while fetching data: {e}")
            raise
        finally:
            if conn:
                cursor.close()
                self.disconnect_db(conn)
