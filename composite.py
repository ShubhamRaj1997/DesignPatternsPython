"""
Your code may have heirarchies of objects! graph like code, there you use the composite design patterns
like one object has bunch of objects and those having other objects also
So we have leaf and internal nodes as objects (are called composites)


both leaf and composites should have same "operation" no changes
INTERFACE segregation means your class should not be forced to use interface methods which are useless for it
Like HTML templates
"""
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @abstractmethod
    def operation(self):
        """ Most important function"""
        pass

    def add(self):
        pass

    def remove(self):
        pass


class Leaf(Component):

    def operation(self):
        pass


class Composite(Component):
    def __init__(self):
        self._children: List[Component] = []

    @staticmethod
    def is_composite():
        return True

    def operation(self):
        ret = []
        for child in self._children:
            ret.append(child.operation())
        return ret
