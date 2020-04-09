import boardbean

class Problem:
    def __init__(self, numberOfQueens, start_state=None):
        if not start_state:
            start_state = boardbean.BoardState(numberOfQueens)
        self.start_state = start_state

    def is_goal(self, currentBoard):
        # Check goal
        return currentBoard.queen_attacks() == 0

    def cost_function(self, currentBoard):
        # Cost function as number of queen attacking
        return currentBoard.queen_attacks()