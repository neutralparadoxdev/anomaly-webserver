from .states import State, StateFactory


def http11StateMachine() -> State:
    """

    """
    factory = StateFactory()

    start = factory.create_state()

    post_state_term = start.add_word('POST')
    get_state_term = start.add_word('GET')
    put_state_term = start.add_word('PUT')
    delete_state_term = start.add_word('DELETE')

    return start

