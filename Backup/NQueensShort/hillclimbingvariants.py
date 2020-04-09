import calculationperformer
import problem

def useSteepHillClimbingApproach(noofQueensOnBoard, choiceOfTries):
    # Steepest Ascent without sideway move method
    total = 0
    fail_steps = 0
    sample_sequences = []
    sample_problems = []
    for i in range(choiceOfTries):
        print("Try #{}".format(i+1))
        result = calculationperformer.steepest_ascent(problem.Problem(noofQueensOnBoard))
        total += result['outcome']
        fail_steps += len(result['solution'])
        if result['outcome']:
            if (result['problem'] not in sample_problems) and (len(sample_problems) < 4):
                sample_problems.append(result['problem'])
                sample_sequences.append(result['solution'])
    printFinalResult('Steepest Hill Climbing', sample_sequences, choiceOfTries, total)

def useSteepHillClimbingApporachWithSidewaysMove(noofQueensOnBoard, choiceOfTries):
    # Steepest Ascent with Sideway move up to 100 moves
    total = 0
    fail_steps = 0
    sample_sequences = []
    sample_problems = []
    for _ in range(choiceOfTries):
        result = calculationperformer.steepest_ascent_using_sideways(problem.Problem(noofQueensOnBoard))
        total += result['outcome']
        fail_steps += len(result['solution'])
        if result['outcome']:
            if (result['problem'] not in sample_problems) and (len(sample_problems) < 4):
                sample_problems.append(result['problem'])
                sample_sequences.append(result['solution'])
    printFinalResult('Steepest Hill Climbing with Sideways Move', sample_sequences, choiceOfTries, total)

def useRandomRestartHillClimbingApporach(noofQueensOnBoard, choiceOfTries):
    total = 0
    fail_steps = 0
    sample_sequences = []
    sample_problems = []
    for i in range(choiceOfTries):
        print("Try #{}".format(i+1))
        result = calculationperformer.random_restart(problem.Problem(noofQueensOnBoard).__class__, noofQueensOnBoard)
        total += result['outcome']
        fail_steps += len(result['solution'])
        if result['outcome']:
            if (result['problem'] not in sample_problems) and (len(sample_problems) < 4):
                sample_problems.append(result['problem'])
                sample_sequences.append(result['solution'])
    printFinalResult('Random Restart Hill Climbing', sample_sequences, choiceOfTries, total)

def printFinalResult(localSearchAlgoUsed, sample_sequences, choiceOfTries, total):
    for i, currentState in enumerate(sample_sequences):
        print('Random Initial Configuration #{}.'.format(i + 1))
        print('Initial State :\n{}'.format(currentState[0]))
        print('Final State :\n{}'.format(currentState[-1]))
    print('{} Results :\nSuccess Count : {}\nFailure : {}'.format(localSearchAlgoUsed, total, choiceOfTries - total))