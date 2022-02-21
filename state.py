"""
State pattern , does the different algos based on state of the object

Like in Parking lot we have to implement gates exits and enters, there each gate has state like opened
closed and accordingly we take decisions based on payment
"""

from abc import abstractmethod, ABC


class GateProcessor:
    def __init__(self, state: Gate):
        self._state = state

    def process(self):
        self._state.operate()

class Gate(ABC):
    @staticmethod
    @abstractmethod
    def operate():
        pass

    @staticmethod
    @abstractmethod
    def read_failed():
        pass


class EntryStateGate(Gate):
    @staticmethod
    def read_failed():
        """
        Let customer pass on, we will read based on the state of card, basically card state was better example
        """
        pass

    @staticmethod
    def operate():
        pass


class ExitStateGate(Gate):
    @staticmethod
    def read_failed():
        """
        Do not let the customer pass
        """
        pass

    @staticmethod
    def operate():
        pass


# get state for user
def get_state(user):
    return ExitStateGate()


gate_state = get_state("user")
gate_state.operate()

gate_processor = GateProcessor(ExitStateGate())
gate_processor.process()
