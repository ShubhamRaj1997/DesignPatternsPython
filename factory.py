"""
Problem:
    Client has to similar operations on two different objects which are similar
    but different changes in objects (like instantiation) will result in changing the client code

Solution:
    Move the dependency to separate class Factory, this improves as
    * Single Responsibility Principle
    * Dependency injection like we do in strategy pattern
"""

from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def open_file(self):
        pass


class PDFHandler(FileHandler):

    def open_file(self):
        pass


class ZIPHandler(FileHandler):

    def open_file(self):
        pass


class FileHandlerCreator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def close_file(self, path_to_file):
        pass


class PDFHandlerCreator(FileHandlerCreator):
    def factory_method(self):
        pass
