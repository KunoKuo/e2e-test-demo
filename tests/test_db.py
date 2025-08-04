def test_members_table_has_data(db_conn):
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) as count FROM members")
        result = cursor.fetchone()
        assert result["count"] > 0, "members table is empty"