import subprocess
import time
import pytest

@pytest.fixture(scope="session", autouse=True)
def start_server():
    proc = subprocess.Popen(["python3", "app/main.py"])
    time.sleep(2)
    yield
    proc.terminate()
