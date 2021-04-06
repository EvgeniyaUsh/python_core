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
    def __init__(self, data_base, table_name):
        self.data_base = data_base
        self.table_name = table_name
        self.diction = dict()  # dict for __getitem__

        try:
            self.con = sqlite3.connect(self.data_base)
            self.cursor_ = self.con.cursor()
        except sqlite3.Error:
            raise sqlite3.OperationalError(f"no such table: {self.table_name}")

    def __getitem__(self, item):
        self.cursor_.execute(f'select * from {self.table_name} where name="{item}"')
        self.diction[item] = self.cursor_.fetchone()

        if self.diction[item]:
            return self.diction[item]
        else:
            raise IndexError("no suck index")

    def __len__(self):
        """
        To get amount of records in table.
        :return: records in table.
        """
        self.cursor_.execute(f"select count(*) from {self.table_name}")
        self.length = self.cursor_.fetchone()
        return self.length[0]

    def __contains__(self, item):
        """
        checks if there is a president with the same name in the table
        :param item: name
        :return: True or False
        """
        self.cursor_.execute(
            f"SELECT * from {self.table_name} where name=:name", {"name": item}
        )

        return bool(self.cursor_.fetchone())

    def __iter__(self):
        """
        iterator by name
        :return: all names in the table
        """
        self.cursor_.execute(f"SELECT name FROM {self.table_name}")
        yield from self.cursor_.fetchall()
