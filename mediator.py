"""
mediator is middleman which is responsible for communication among different objects
eg. you have a hotel room, that can be booked via booking.com or trevago or some other websites
here different websites could communicate with each other but they are communicating via HotelBooker
"""

from abc import ABC, abstractmethod
from typing import List


class Mediator(ABC):
    @abstractmethod
    def is_booked_already(self, room_id, website: Website):
        pass


class Website(ABC):
    @abstractmethod
    def is_room_booked(self, room_id):
        pass


class Trevago(Website):
    def is_room_booked(self, room_id):
        pass


class Bookingcom(Website):

    def is_room_booked(self, room_id):
        pass


class HotelBooker(Mediator):
    def __init__(self):
        self._websites: List[Website] = []

    def add(self, website: Website):
        self._websites.append(website)

    def remove(self, website: Website):
        self._websites.remove(website)

    def is_booked_already(self, room_id, website: Website):
        for wb in self._websites:
            if wb != website and wb.is_room_booked(room_id):
                return True
        return False

    def book_room(self, room_id, website: Website):
        if self.is_booked_already(room_id, website):
            raise Exception("Already booked buddy!")
        # book

bookingcom = Bookingcom()
booker = HotelBooker()
booker.add(bookingcom)
booker.is_booked_already("1",bookingcom)
