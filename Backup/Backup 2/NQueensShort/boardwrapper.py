import board

class BoardWrapper:
    '''
    n Queen Problem
    '''
    def __init__(self, noofQueensOnBoard, start_state=None):
        if not start_state:
            start_state = board.Board(noofQueensOnBoard)
        self.start_state = start_state

    def is_goal(self, state):
        # Check goal
        return state.calculate_possible_attacks() == 0

    def cost_function(self, state):
        # Cost function as number of queen attacking
        return state.calculate_possible_attacks()