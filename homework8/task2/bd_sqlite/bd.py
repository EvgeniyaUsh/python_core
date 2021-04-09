"""
Write a wrapper class TableData for database table, that when initialized
with database name and table acts as collection object (implements Collection protocol).
Assume all data has unique values in 'name' column.
So, if presidents = TableData(database_name='example.sqlite', table_name='presidents')

then:

- len(presidents) will give current amount of rows in presidents table in database
- presidents['Yeltsin'] should return single data row for president with name Yeltsin
- 'Yeltsin' in presidents should return if president with same name exists in table

- object implements iteration protocol. i.e. you could use it in for loops::
    for president in presidents:
        print(president['name'])

- all above mentioned calls should reflect most recent data.
If data in table changed after you created collection instance,
your calls should return updated data.

Avoid reading entire table into memory.
When iterating through records, start reading the first record,
then go to the next one, until records are exhausted.
When writing tests, it's not always necessary to mock database calls completely.
Use supplied example.sqlite file as database fixture file.
"""

import sqlite3


class TableData:
    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name

    def __getitem__(self, item):
        self._cursor.execute(
            f"SELECT * from {self.table_name} where name=:name", {"name": item}
        )
        return self._cursor.fetchone()

    def __len__(self):
        """
        To get amount of records in table.
        :return: records in table.
        """
        self._cursor.execute(f"select count(*) from {self.table_name}")
        return self._cursor.fetchone()[0]

    def __contains__(self, item):
        """
        checks if there is a president with the same name in the table
        :param item: name
        :return: True or False
        """
        self._cursor.execute(
            f"SELECT * from {self.table_name} where name=:name", {"name": item}
        )
        return bool(self._cursor.fetchone())

    def __iter__(self):
        """
        iterator by name
        :return: all names in the table
        """

        def dict_factory(row):
            d = {}
            for idx, col in enumerate(self._cursor.description):
                d[col[0]] = row[idx]
            return d

        yield from (
            dict_factory(row)
            for row in self._cursor.execute(f"select * from {self.table_name}")
        )

    def __enter__(self):
        """
        connect with our database sqlite3
        """
        self._connect = sqlite3.connect(self.database_name)
        self._cursor = self._connect.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        close connect our with database sqlite3
        """
        return self._connect.close()
