"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50
order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""

from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    Algorithm invocation interface.
    """

    @abstractmethod
    def do_algorithm(self):
        pass


class Order:
    def __init__(self, price, strategy: Strategy):
        """
        The constructor adopts the strategy.
        :param price: some int
        :param strategy: Strategy
        """
        self.price = price
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def final_price(self):
        """
        Business logic.
        :return: some number
        """
        result = self._strategy.do_algorithm(self) * self.price
        return result


class MorningDiscount(Strategy):
    """
    Implementation of the algorithm from the Strategy interface.
    """

    def do_algorithm(self):
        return 0.5


class ElderDiscount(Strategy):
    """
    Implementation of the algorithm from the Strategy interface
    """

    def do_algorithm(self):
        return 0.1