"""
Template method is where you know the process but some of the steps may differ
We know some parts of its process but some parts are variable
It helps in removing IF and ELSE boilerplate code!!
"""
from abc import ABC, abstractmethod


class Reader(ABC):
    def process(self):
        self.sort()
        self.display()

    @abstractmethod
    def sort(self):
        pass

    def display(self):
        pass


class Sort(Reader):
    def sort(self):
        """ sort the array"""
        pass

class RevSort(Reader):
    def sort(self):
        """reverse sort the array"""
        pass


RevSort().process()
Sort().process()
