"""
Makes an Adapter for a class to adapt interface used by some other class


Target: The domain specific interface or class that needs to be adapted.
Adapter Interface: The interface of the target that the adapter will need to implement.
Adapter: The concrete adapter class containing the adaption process.
Client: The client application that will use the Adapter.


"""


class Target:
    def something(self):
        pass


class Adaptee:
    def someother_thing(self):
        pass


class Adapter(Target, Adaptee):
    def something(self):
        return self.someother_thing()
