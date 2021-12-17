"""
To clone the class without effecting it or making your class dependent on it
"""

import copy
from abc import abstractmethod, ABC


class ProtoType(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def deep_clone(self):
        pass


class A(ProtoType):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def clone(self):
        return copy.copy(self)

    def deep_clone(self):
        return copy.deepcopy(self)


a = A("a", "b", "c")
print(a)
print(a.deep_clone())
