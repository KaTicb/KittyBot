import aiosqlite
from typing import Iterable
import asyncio
from datetime import datetime


class DatabaseManager:
    def __init__(self, db_name: str = "wish_list.db"):
        self.db_name = db_name

    async def init_database(self):
        """Creation of the database"""
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute('''
                CREATE TABLE IF NOT EXISTS wish_list (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    owner TEXT NOT NULL,
                    created_at DATETIME,
                    item_name TEXT
                )
            ''')
            await db.commit()

    async def create_item(self, item_name: str, owner: str) -> int:
        """Creation of a new record"""
        async with aiosqlite.connect(self.db_name) as db:
            time = datetime.now()

            cursor = await db.execute(
                'INSERT INTO wish_list (owner, item_name, created_at) VALUES (?, ?, ?)',
                (owner, item_name, time)
            )
            await db.commit()
            return cursor.lastrowid

    async def update_item(self, item_id: int, **kwargs) -> bool:
        """Update a record"""
        async with aiosqlite.connect(self.db_name) as db:
            columns = []
            values = []

            for key, value in kwargs.items():
                columns.append(f"{key}=?")
                values.append(value)

            values.append(item_id)

            query = f"UPDATE wish_list SET {', '.join(columns)} WHERE id=?"
            cursor = await db.execute(query, values)
            await db.commit()

            return cursor.rowcount > 0

    async def delete_item(self, item_id: int, user_name: str) -> bool:
        """Delete a record by ID"""
        async with aiosqlite.connect(self.db_name) as db:
            cursor = await db.execute('DELETE FROM wish_list WHERE id=? AND owner=?', (item_id, user_name))
            await db.commit()
            return cursor.rowcount > 0

    async def get_list_by_owner(self, owner: str) -> Iterable:
        """Read owner's records"""
        async with aiosqlite.connect(self.db_name) as db:
            cursor = await db.execute('SELECT * FROM wish_list WHERE owner=?', (owner,))
            rows = await cursor.fetchall()

        return rows

    async def get_all_list(self) -> Iterable:
        """Read all records"""
        async with aiosqlite.connect(self.db_name) as db:
            cursor = await db.execute('SELECT * FROM wish_list ORDER BY owner')
            rows = await cursor.fetchall()

        return rows


async def main():
    db = DatabaseManager(db_name="../wish_list.db")
    await db.init_database()


if __name__ == '__main__':
    asyncio.run(main())
