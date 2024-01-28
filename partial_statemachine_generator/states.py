from typing import Self, List, Dict, Optional

class State:
    """
    A State is the state within the machine.
    """
    def __init__(self, factory: 'StateFactory', id: int):
        self._id: int = id
        # transitions all to a given state
        self._transition_on_all: bool = False
        self._next: Optional[Self] = None
        # consume all means that it points to itself
        self._consume_all: bool = False
        self._transitions: Dict[str, Self] = {}
        self._factory: 'StateFactory' = factory
        pass

    def add_character(self, character: str, state: Self, next: Optional[Self]=None) -> Self:
        """
        adds a character to the state machine.
        returns the next character
        """
        self._transitions[character] = state
        return self

    # rename to add_sequence
    def add_word(self, word: str, next: Optional[Self]=None) -> Self:
        """
        add a word to the state machine. 
        returns the last state
        """
        if len(word) == 0:
            return self

        c = word[0]
        if self._transitions[c]:
            return self._transitions[c].add_word(word[1:])
        else:
            next_state = self._factory.create_state()
            self._transitions[c] = next_state
            return next_state.add_word(word[1:])

    def consume_any(self, character: str) -> Self:
        self._consume_any = True
        return self


class StateFactory:
    """
    Only proper way to create a State. All states for a given output must come from the 
    same StateFactory as all States must have a unique ID
    """
    def __init__(self):
        self._id_counter = 0
        self._transitions = {}
        pass

    def get_id(self) -> int:
        return self._id_counter

    def create_state(self) -> State:
        state = State(self, self.get_id())
        return state


