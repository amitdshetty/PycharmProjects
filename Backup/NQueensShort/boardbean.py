import copy
import random

class BoardState:
    count = 0
    def __init__(self, queen_num, queen_positions=None, parent=None, path_cost=0, f_cost=0):
        self.side_length = queen_num
        if queen_positions is None:
            self.queen_num = queen_num
            self.queen_positions = frozenset(self.random_queen_position())
        else:
            self.queen_positions = queen_positions
            self.queen_num = len(self.queen_positions)
        self.path_cost = 0
        self.f_cost = f_cost
        self.parent = parent
        self.id = BoardState.count
        BoardState.count += 1

    def __str__(self):
        # string function for printing
        return '\n'.join([' '.join(['_' if (col, row) not in self.queen_positions else 'Q' for col in range(self.side_length)]) for row in range(self.side_length)])

    def __hash__(self):
        # Hash function to remove duplicate
        return hash(self.queen_positions)

    def __eq__(self, other):
        # Check if 2 nodes are same
        return self.queen_positions == other.queen_positions

    def __lt__(self, other):
        # Compare cost
        return self.f_cost < other.f_cost or (self.f_cost == other.f_cost and self.id > other.id)

    def random_queen_position(self):
        # Generate random queen position
        open_columns = list(range(self.side_length))
        queen_positions = [(open_columns.pop(random.randrange(len(open_columns))), random.randrange(self.side_length)) for _ in range(self.queen_num)]
        return queen_positions

    def get_children(self):
        # Get children from current state node
        children = []
        parent_queen_positions = list(self.queen_positions)
        for queen_index, queen in enumerate(parent_queen_positions):
            new_positions = [(queen[0], row) for row in range(self.side_length) if row != queen[1]]
            for new_position in new_positions:
                queen_positions = copy.deepcopy(parent_queen_positions)
                queen_positions[queen_index] = new_position
                children.append(BoardState(self.queen_num, queen_positions))
        return children

    def random_child(self):
        # Random child
        queen_positions = list(self.queen_positions)
        random_queen_index = random.randrange(len(self.queen_positions))
        queen_positions[random_queen_index] = (queen_positions[random_queen_index][0], random.choice([row for row in range(self.side_length) if row != queen_positions[random_queen_index][1]]))
        return BoardState(self.queen_num, queen_positions)

    def range_between(self, a, b):
        # Return positions between a and b
        if a > b:
            return range(a-1, b, -1)
        elif a < b:
            return range(a+1, b)
        else:
            return [a]

    def zip_repeat(self, a, b):
        # Repeat
        if len(a) == 1:
            a *= len(b)
        elif len(b) == 1:
            b *= len(a)
        return zip(a, b)

    def points_between(self, a, b):
        # Repeat zipped positions between a and b
        return self.zip_repeat(list(self.range_between(a[0], b[0])), list(self.range_between(a[1], b[1])))

    def is_attacking(self, queens, a, b):
        # Check if 2 positions have attacked each other
        if (a[0] == b[0]) or (a[1] == b[1]) or (abs(a[0]-b[0]) == abs(a[1]-b[1])):
            for between in self.points_between(a, b):
                if between in queens:
                    return False
            return True
        return False

    def queen_attacks(self):
        # Calculate number of queen attacking
        attacking_pairs = []
        queen_positions = list(self.queen_positions)
        left_to_check = copy.deepcopy(queen_positions)
        while left_to_check:
            a = left_to_check.pop()
            for b in left_to_check:
                if self.is_attacking(queen_positions, a, b):
                    attacking_pairs.append([a, b])
        return len(attacking_pairs)
