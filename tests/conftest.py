import pytest
import pymysql

@pytest.fixture(scope="module")
def db_conn():
    conn = pymysql.connect(
        host="localhost",       # 或用你的容器 IP / 服務名
        port=3306,              # MySQL 的 port，若你對外映射其他 port，請對應修改
        user="root",
        password="your_password",
        database="member_system",
        cursorclass=pymysql.cursors.DictCursor,
    )
    yield conn
    conn.close()