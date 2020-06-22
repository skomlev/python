from api.states.models import State


class StateServices:

    @classmethod
    def get_all_states(cls):
        """Get all states."""
        return State.query.all()
