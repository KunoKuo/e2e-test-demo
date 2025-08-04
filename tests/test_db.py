import sqlite3

def test_db_insert():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO test (name) VALUES ('pytest')")
    conn.commit()
    cursor.execute("SELECT name FROM test")
    result = cursor.fetchone()
    assert result[0] == "pytest"
    conn.close()
