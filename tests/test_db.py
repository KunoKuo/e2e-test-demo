import pytest

def test_members_table_has_data(db_conn):
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) as count FROM members")
        result = cursor.fetchone()
        assert result["count"] > 0, "members table is empty"

def test_members_table_schema(db_conn):
    with db_conn.cursor() as cursor:
        cursor.execute("DESCRIBE members")
        columns = {column['Field'] for column in cursor.fetchall()}
        expected_columns = {'id', 'name', 'email', 'password'}
        assert expected_columns.issubset(columns), \
            f"members table schema is not correct. Missing columns: {expected_columns - columns}"

@pytest.mark.parametrize("name, email, password", [
    ("test_user_1", "test1@example.com", "password123"),
    ("test_user_2", "test2@example.com", "password456"),
])
def test_add_and_delete_member(db_conn, name, email, password):
    with db_conn.cursor() as cursor:
        # Add a new member
        cursor.execute("INSERT INTO members (name, email, password) VALUES (%s, %s, %s)", (name, email, password))

        # Verify the member was added
        cursor.execute("SELECT * FROM members WHERE name = %s", (name,))
        new_member = cursor.fetchone()
        assert new_member is not None, "Failed to add new member"
        assert new_member['email'] == email

        new_member_id = new_member['id']

        # Delete the member
        cursor.execute("DELETE FROM members WHERE id = %s", (new_member_id,))

        # Verify the member was deleted
        cursor.execute("SELECT * FROM members WHERE id = %s", (new_member_id,))
        deleted_member = cursor.fetchone()
        assert deleted_member is None, "Failed to delete member"