def test_users_table_has_data(db_conn):
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) as count FROM users")
        result = cursor.fetchone()
        assert result["count"] > 0, "users table is empty"
