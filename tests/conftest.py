import pytest
import pymysql

@pytest.fixture(scope="module")
def db_conn():
    conn = pymysql.connect(
        host='localhost',
        user='your_user',
        password='your_password',
        db='your_database',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    yield conn
    conn.close()
