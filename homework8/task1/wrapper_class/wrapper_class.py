"""
We have a file that works as key-value storage,
each like is represented as key and value separated by = symbol, example:

name=kek last_name=top song_name=shadilay power=9001

Values can be strings or integer numbers.
If a value can be treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt')
that has its keys and values accessible as collection items and as attributes.
Example: storage['name'] # will be string 'kek' storage.song_name
# will be 'shadilay' storage.power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute
(for example when there's a line 1=something) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.
"""


class KeyValueStorage:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path) as file:
            for i in file:
                try:
                    if bool(int(i.split("=")[1].rstrip())) == (True or False):
                        self.__dict__[i.split("=")[0]] = int(i.split("=")[1].rstrip())
                except ValueError:
                    self.__dict__[i.split("=")[0]] = i.split("=")[1].rstrip()

    def __getitem__(self, item):
        if item in self.__dict__:
            self.value = self.__dict__[item]
            return self.value
        else:
            raise ValueError("No such key")
