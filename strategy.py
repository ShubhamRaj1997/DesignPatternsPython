"""
* Mainly used when we want to separate out behaviours to classes
* We can change behaviour of class without extending it!
* HLBC -> High Level Business Class which deals with business logic like store data
* LLBC -> Low Level Base class which deals with low level stuff like using particular db/cache
* Why to use?
    PROBLEM
    1. You develop system, first create low level classes then high level business logic, this makes HLBC dependent on
    LLBC
    example, the CacheLayer class gets dependent on LRUCache class if we use it directly

    SOLUTION
    1. You use dependency injection (inversion), now make your HLBC independent of LLBC by introducing interface
    eg. CacheStrategy is the interface which inverts the dependency, now LLBC depends on interface not the HLBC
    dependent on LLBC

* Example we are designing a cache, we can use different caching strategies like LRUCache, LFUCache
    1. You may think how is it different from normal inheritance?
        i. if you have subclass B,C,D of class A.
        ii. B(A) and C(A) has common methods and may not require all method of A to implement otherwise
        we will break
        then we can create separate subclass BC(A) and D(A)
        iii. class B(BC) and C(BC) can implement BC(A) abstract class
        iv. We created BC(A) to avoid code duplication!!!

"""
from abc import ABC, abstractmethod


class CacheStrategy(ABC):
    @abstractmethod
    def store_data(self, data):
        pass

    @abstractmethod
    def get_data(self):
        pass


class LRUCacheStrategy(CacheStrategy):
    def store_data(self, data):
        pass

    def get_data(self):
        pass


class LFUCacheStrategy(CacheStrategy):
    def store_data(self, data):
        pass

    def get_data(self):
        pass


class CacheLayer(object):
    def __init__(self, cache_strategy):
        self._cache_strategy = cache_strategy

    @property
    def cache_strategy(self):
        return self._cache_strategy

    @cache_strategy.setter
    def cache_strategy(self, cache_strategy: CacheStrategy):
        self._cache_strategy = cache_strategy

    def store_data(self, data):
        # preprocess
        self._cache_strategy.store_data(data)
        # postprocess

    def get_data(self):
        # preprocess
        data = self._cache_strategy.get()
        # postprocess
        return data


lru = CacheLayer(LRUCacheStrategy())
lru.store_data("data")

lfu = CacheLayer(LFUCacheStrategy())
lfu.store_data("data1")
