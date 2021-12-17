"""
memento is used to remember state of object!
brilliant example :
* transactions
* dumping snapshots

here we are using transactions example

"""
import datetime
from abc import ABC, abstractmethod


class Snapshot(ABC):
    """
    Memento
    """
    @abstractmethod
    def get_amount(self) -> int:
        pass

    @abstractmethod
    def get_time(self) -> datetime.datetime:
        pass


class AccountSnapshot(Snapshot):
    """
    Concrete memento
    """

    def __init__(self, amount):
        self._amount = amount
        self._date = datetime.datetime.utcnow()

    def get_amount(self) -> int:
        return self._amount

    def get_time(self) -> datetime.datetime:
        return self._date


class Bank(object):
    """
    Also called originator
    """
    _state = None

    def __init__(self, money: int):
        self._money = money

    def get_money(self):
        return self._money

    def add_money(self, amount):
        # do something here some changes
        self._money += amount

    def save_state(self):
        return AccountSnapshot(self._money)

    def restore(self, snapshot: Snapshot):
        self._money = snapshot.get_amount()


bank = Bank(2)
snaps = list()
snaps.append(bank.save_state())
bank.add_money(10)
print(bank.get_money())

snaps.append(bank.save_state())
bank.restore(snaps[0])
print(bank.get_money())

"""
There can be caretaker also which takes care of mementos lifecycle

"""