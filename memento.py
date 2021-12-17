"""
memento is used to remember state of object!
brilliant example :
* transactions
* dumping snapshots

here we are using transactions example

"""
from abc import ABC, abstractmethod
class Memento(object):
    def __init__(self, temp, pressure, volume):
        self.temp = temp
        self.pressure = pressure
        self.volume = volume

class Originator()
