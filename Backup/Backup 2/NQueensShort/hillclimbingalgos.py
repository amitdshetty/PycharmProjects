import random

def steepest_ascent(board_wrapper, allow_sideways=False, max_sideways=100):
    # Steepest ascent with option of sideway move
    node = board_wrapper.start_state
    node_cost = board_wrapper.cost_function(node)
    path = []
    sideways_moves = 0
    while True:
        path.append(node)
        best_child = get_best_child(node, board_wrapper)
        best_child_cost = board_wrapper.cost_function(best_child)
        if best_child_cost > node_cost:
            break
        elif best_child_cost == node_cost:
            if not allow_sideways or sideways_moves == max_sideways:
                break
            else:
                sideways_moves += 1
        else:
            sideways_moves = 0
        node = best_child
        node_cost = best_child_cost
    return {'is_final_state': 1 if board_wrapper.is_goal(node) else 0, 'solution': path , 'problem': board_wrapper}

def random_restart(random_board, noofQueensOnBoard):
    # Random restart using steepest ascent
    num_restarts = 100
    path = []
    for _ in range(num_restarts):
        result = steepest_ascent(random_board(noofQueensOnBoard))
        path += result['solution']
        if result['is_final_state'] == 1:
            break
    result['solution'] = path
    return result

def get_best_child(node, problem):
    # Get best child with minimum cost
    children = node.get_children()
    children_cost = [problem.cost_function(child) for child in children]
    min_cost = min(children_cost)
    best_child = random.choice([child for child_index, child in enumerate(children) if children_cost[child_index] == min_cost])
    return best_child