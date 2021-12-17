"""

The Builder pattern is useful:
* constructors become bulky :( and for unuseful property you pass None , for each permutation of the parameters
you will have many constructors
* object creation is complex
* too many cases for objects
* different concrete classes can return different kind of objects
* A bit Java oriented, Many android classes use this design pattern
eg.
Calendar cal = new Calendar.Builder()
                           .setCalendarType("japanese")
                           .setFields(YEAR, 1, DAY_OF_YEAR, 1)
                           .build();

NotificationCompat.Builder notificationBuilder = new NotificationCompat.Builder(this)
                .setSmallIcon(R.mipmap.ic_launcher)
                .setContentTitle("Firebase Push Notification")
                .setContentText(messageBody)
                .setAutoCancel(true)
                .setSound(defaultSoundUri)
                .setContentIntent(pendingIntent);
instead of passing the values of field to constructors as null,

Python has beautiful property and setter , so not that useful in python

The other aspect of builder pattern is given in GOF, which is to simplify construction of complex object
either you want to create whole part of it or only few parts
"""

from abc import ABC, abstractmethod


class Builder(ABC):

    @abstractmethod
    def produce_part1(self):
        pass

    @abstractmethod
    def produce_part2(self):
        pass


class ConcreteBuilder(Builder):

    def __init__(self, product):
        self._product = product

    def produce_part1(self):
        self._product.append("part1")

    def produce_part2(self):
        self._product.append("part2")


class Product(list):
    pass


class Director(object):
    @staticmethod
    def produce_minimal_product():
        product = Product()
        ConcreteBuilder(product).produce_part1()

    @staticmethod
    def produce_full_product():
        product = Product()
        cb = ConcreteBuilder(product)
        cb.produce_part1()
        cb.produce_part2()


