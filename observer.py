"""
* Problem
    1. A class needs to notify other classes, one way is to PULL every time to check if change happened in
    base class
 Solution
    1. Creates one to many dependencies and use PUSH mechanism, change from base gets notified to all
    observers

eg. create notification Service which notifies the needed channel based on services like CheckInService & CheckoutService
"""
from abc import ABC, abstractmethod


class NotificationService(ABC):
    def __init__(self):
        self.__notification_services = []

    @abstractmethod
    def attach(self, notification_service: NotificationService):
        pass

    @abstractmethod
    def detach(self, notification_service: NotificationService):
        pass

    @abstractmethod
    def notify(self, data):
        pass


class CheckInService(NotificationService):
    def __init__(self):
        super().__init__()
        self.__notification_services = []

    def attach(self, notification_service: NotificationService):
        self.__notification_services.append(notification_service)

    def detach(self, notification_service: NotificationService):
        self.__notification_services.remove(notification_service)

    def notify(self, data):
        for ns in self.__notification_services:
            ns.notify(data)


class CheckOutService(NotificationService):
    def __init__(self):
        super().__init__()

    def attach(self, notification_service: NotificationService):
        pass

    def detach(self, notification_service: NotificationService):
        pass

    def notify(self, data):
        pass


class NotificationChannel(ABC):
    @abstractmethod
    def notify(self, data):
        pass


class EmailNotificationChannel(NotificationChannel):

    def notify(self, data):
        pass


class PushNotificationChannel(NotificationChannel):

    def notify(self, data):
        pass


class SMSNotificationChannel(NotificationChannel):

    def notify(self, data):
        pass
