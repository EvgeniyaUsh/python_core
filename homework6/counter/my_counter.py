"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    """
    A decorator that applies to any class and attaches 2 additional methods:
    get_created_instances() - returns the number of instances of the class created.
    reset_instances_counter() - resets the instance counter,
    returns the value before reset.
    """

    cls.counter = 0

    def __new__(cls, *args, **kwargs):
        cls.counter += 1
        return super(cls.__class__, cls).__new__(cls)

    def get_created_instances(cls):
        return cls.counter

    def reset_instances_counter(cls):
        to_return = cls.counter
        cls.counter = 0
        return to_return

    cls.__new__ = __new__
    cls.get_created_instances = classmethod(get_created_instances)
    cls.reset_instances_counter = classmethod(reset_instances_counter)

    return cls
