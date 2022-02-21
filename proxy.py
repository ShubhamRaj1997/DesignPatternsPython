"""
Proxy pattern is useful for
* lazy loading for class
* caching
* logging
* authentication also

"""
from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def do_something(self):
        pass


class OriginalSubject(Subject):

    def do_something(self):
        pass


class ProxySubject(Subject):
    def __init__(self, subject: Subject):
        self._subject = subject

    def do_something(self):
        if self.can_access():
            self._subject.do_something()

    def can_access(self):
        return True
