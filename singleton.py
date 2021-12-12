"""
Problem:
    A class is responsible for database connection creation, you dont want to create new connection always
    This will create connections overhead
Solution:
    Create single connection and save it as singleton, remember in singleton we use same object again
    Problem again:
        In multithreaded environments again this problem will arise!, every thread can create new singleton
        object thus defeats the purpose of singleton
    soln again:
        Create instance with Lock, and check if the object is already there!

"""


import threading




class Singleton(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):
    pass
