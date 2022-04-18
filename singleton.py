"""
Problem:
    A class is responsible for database connection creation, you dont want to create new connection always
    This will create connections overhead
Solution:
    Create single connection and save it as singleton, remember in singleton we use same object again
    Problem again:
        In multi-threaded environments again this problem will arise!, every thread can create new singleton
        object thus defeats the purpose of singleton
    soln again:
        Create instance with Lock, and check if the object is already there!
This creates issues and overhead un necessary thus it is advised not to use it and considered as anti-pattern

why there is second check after locking

"""

import threading


class Singleton(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                """
                # another thread could have created the instance
                # before we acquired the lock. So check that the
                # instance is still nonexistent
                """
                if cls not in cls._instances:
                    cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):
    pass
