from homework6.counter.my_counter import instances_counter


@instances_counter
class User:
    pass


@instances_counter
class Cat:
    def __init__(self, name):
        self.name = name


def test_method_get_created_instances_with_class_user():
    assert User.get_created_instances() == 0
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3


def test_method_reset_instances_counter_with_class_user():
    user, _, _ = User(), User(), User()
    assert user.reset_instances_counter() == 3
    assert user.get_created_instances() == 0


def test_method_get_created_instances_with_class_cat():
    assert Cat.get_created_instances() == 0
    cat, _, _ = Cat("name"), Cat("name"), Cat("name")
    assert cat.get_created_instances() == 3
    assert cat.name == "name"


def test_method_reset_instances_counter_with_class_cat():
    cat, _, _ = Cat("name"), Cat("name"), Cat("name")
    assert cat.reset_instances_counter() == 3
    assert cat.get_created_instances() == 0
