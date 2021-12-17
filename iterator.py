"""
An Iterator: which iterates over ITERABLE
An interface which has "has_next" and "next" methods is basically Iterator interface
Client can traverse an aggregate without understanding its internal representation

Eg. you may iterate in BFS order of DFS order for a graph!!
or in reverse order for one iterator and in sorted manner for the other iterator

"""

from abc import ABC, abstractmethod


class IIterator(ABC):
    "An Iterator Interface"

    @staticmethod
    @abstractmethod
    def has_next():
        "Returns Boolean whether at end of collection or not"

    @staticmethod
    @abstractmethod
    def next():
        "Return the object in collection"


class Iterable(IIterator):
    "The concrete iterator (iterable)"

    def __init__(self, aggregates):
        self.index = 0
        self.aggregates = aggregates

    def next(self):
        if self.index < len(self.aggregates):
            aggregate = self.aggregates[self.index]
            self.index += 1
            return aggregate
        raise Exception("AtEndOfIteratorException", "At End of Iterator")

    def has_next(self):
        return self.index < len(self.aggregates)


class Iterable2(IIterator):
    def __init__(self, aggregates):
        self.index = len(aggregates) - 1
        self.aggregates = aggregates

    def next(self):
        if self.index >= 0:
            aggregate = self.aggregates[self.index]
            self.index -= 1
            return aggregate
        raise Exception("AtEndOfIteratorException", "At End of Iterator")

    def has_next(self):
        return self.index > 0


class IAggregate(metaclass=ABC):
    "An interface that the aggregates should implement"

    @staticmethod
    @abstractmethod
    def method():
        "a method to implement"


class Aggregate(IAggregate):
    "A concrete object"

    @staticmethod
    def method():
        print("This method has been invoked")


# The Client
AGGREGATES = [Aggregate(), Aggregate(), Aggregate(), Aggregate()]
# AGGREGATES is a python list that is already iterable by default.

# but we can create own own iterator on top anyway.
ITERABLE = Iterable(AGGREGATES)
ITERABLE2 = Iterable2(AGGREGATES)
while ITERABLE.has_next():
    ITERABLE.next().method()
