import pytest
import pymysql
import subprocess
import os
import signal
import time
import requests

# 啟動 Flask server（只有 module 內第一次測試執行前會啟動）
@pytest.fixture(scope="module", autouse=True)
def start_flask_server():
    proc = subprocess.Popen(
        ["python", "app/main.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        preexec_fn=os.setsid
    )

    time.sleep(2)  # 等 server 起來

    # 驗證 Flask server 是否正常啟動
    try:
        response = requests.get("http://127.0.0.1:5000/items")
        if response.status_code != 200:
            raise RuntimeError("Flask server response not 200")
    except Exception as e:
        print("[ERROR] Flask server failed to start")
        out, err = proc.communicate(timeout=2)
        print("[stdout]", out.decode())
        print("[stderr]", err.decode())
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        raise

    yield

    # 停止 Flask server
    try:
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
    except ProcessLookupError:
        print("[WARNING] Flask server already exited")


# 提供資料庫連線
@pytest.fixture(scope="module")
def db_conn():
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="your_password",
        database="member_system",
        cursorclass=pymysql.cursors.DictCursor,
    )
    yield conn
    conn.close()