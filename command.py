"""
Receiver: The object that will receive and execute the command.
Invoker: The object that sends the command to the receiver. E.g., A button.
Command Object: Itself, an object, that implements an execute, or action method, and contains all required information to execute it.
Client: The application or component that is aware of the Receiver, Invoker and Commands.

Problem:
    Developed UI for buttons, you create a Button class and there are 10 of buttons on UI
    you created 10 subclasses!!!, you could use strategy pattern also
    Like 5 buttons saving some data to database, you will implement same in all 5 subclasses
    Multi- undo redo


    Basically
    Invoker can have additional functionalities like recording the commands and history for same
    Command Object contains Receiver object and perform commands on that receiver
    Command objects implements ICommand Interface and override execute method
    which in turn executes the command on receiver
"""
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass


class SaveData(Command):

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self, *args, **kwargs):
        self._receiver.save_data(*args, **kwargs)


class UpdateData(Command):

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self, *args, **kwargs):
        self._receiver.update_data(*args, **kwargs)

class MongoDb:
    def save_data(self, *args, **kwargs):
        pass

class RedisCache:
    def update_data(self, *args, **kwargs):
        pass


class Button(object):
    """
    Invoker
    """
    _commands = []

    def add_command(self, command:Command):
        self._commands.append(command)

    def remove_command(self, command:Command):
        self._commands.remove(command)

    def perform_activity(self):
        mdb= MongoDb()
        redis_db = RedisCache()
        # use different commands as dict and perform as well
        for command in self._commands:
            command.execute(mdb)
            command.execute(redis_db)

