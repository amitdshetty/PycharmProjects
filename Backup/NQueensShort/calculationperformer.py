import random

def get_best_child(node, problem):
    # Get best child with minimum cost
    children = node.get_children()
    children_cost = [problem.cost_function(child) for child in children]
    min_cost = min(children_cost)
    best_child = random.choice([child for child_index, child in enumerate(children) if children_cost[child_index] == min_cost])
    return best_child

def steepest_ascent(problem):
    # Steepest ascent with option of sideway move
    node = problem.start_state
    node_cost = problem.cost_function(node)
    path = []
    while True:
        path.append(node)
        best_child = get_best_child(node, problem)
        best_child_cost = problem.cost_function(best_child)
        if best_child_cost > node_cost:
            break
        node = best_child
        node_cost = best_child_cost
    result = {}
    if problem.is_goal(node):
        result['outcome'] = 1
    else:
        result['outcome'] = 0
    result['solution'] = path
    result['problem'] = problem
    return result

def steepest_ascent_using_sideways(problem):
    # Steepest ascent with option of sideway move
    node = problem.start_state
    node_cost = problem.cost_function(node)
    path = []
    max_sideways = 20
    sideways_moves = 0
    while True:
        path.append(node)
        best_child = get_best_child(node, problem)
        best_child_cost = problem.cost_function(best_child)
        if best_child_cost > node_cost:
            break
        elif best_child_cost == node_cost:
            if sideways_moves == max_sideways:
                break
            else:
                sideways_moves += 1
        else:
            sideways_moves = 0
        node = best_child
        node_cost = best_child_cost
    result = {}
    if problem.is_goal(node):
        result['outcome'] = 1
    else:
        result['outcome'] = 0
    result['solution'] = path
    result['problem'] = problem
    return result

def random_restart(randomProblem, noofQueensOnBoard):
    # Random restart using steepest ascent
    path = []
    num_restarts = 20
    for i in range(num_restarts):
        print("\tRestart #{}".format(i+1))
        result = steepest_ascent(randomProblem(noofQueensOnBoard))
        path += result['solution']
        if result['outcome'] == 1:
            break
    result['solution'] = path
    return result
