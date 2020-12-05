from .database_connection_cm import DatabaseConnection


def insert_member(name, email, level):
    with DatabaseConnection('members.db') as connection:
        cursor = connection.cursor()

        cursor.execute(
            'INSERT INTO members (name, email, level) VALUES (?, ?, ?)', [
                name, email, level]
        )


def get_member_by_name(name):
    with DatabaseConnection('members.db') as connection:
        cursor = connection.cursor()

        cursor.execute(
            'SELECT * FROM members WHERE name=?', [name]
        )
        member = cursor.fetchone()
        return {'member': {'id': member[0], 'name': member[1], 'email': member[2], 'level': member[3],}}


def get_member_by_id(member_id):
    with DatabaseConnection('members.db') as connection:
        cursor = connection.cursor()

        cursor.execute(
            'SELECT * FROM members WHERE id=?', [member_id]
        )
        member = cursor.fetchone()
        return {'member': {'id': member[0], 'name': member[1], 'email': member[2], 'level': member[3],}}


def get_allmembers():
    with DatabaseConnection('members.db') as connection:
        cursor = connection.cursor()

        cursor.execute(
            'SELECT * FROM members'
        )
        return {'members':[{'id': member[0], 'name': member[1], 'email': member[2], 'level': member[3],} for member in cursor.fetchall()]}


def update_member(name, email, level, member_id):
    with DatabaseConnection('members.db') as connection:
        cursor = connection.cursor()

        cursor.execute(
            'UPDATE members SET name=?, email=?, level=? WHERE id=?', [
                name, email, level,member_id]
        )


def delete_member(member_id):
    with DatabaseConnection('members.db') as connection:
        cursor = connection.cursor()

        cursor.execute(
            'DELETE FROM members WHERE id=?', [member_id]
        )