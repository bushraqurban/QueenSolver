import random

def fitness(board):
    """
    Calculates the fitness of an individual based on non-attacking queen pairs.

    Args:
        board (list): A board configuration.

    Returns:
        int: Fitness score (higher is better).
    """
    n = len(board)
    non_attacking = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) != abs(i - j):
                non_attacking += 1
    return non_attacking

def generate_individual(n):
    """
    Generates a random individual (a permutation of queen positions).

    Args:
        n (int): Number of queens.

    Returns:
        list: A permutation representing queen positions on the board.
    """
    individual = list(range(n))
    random.shuffle(individual)
    return individual

def initial_population(n, size):
    """
    Creates the initial population of individuals.

    Args:
        n (int): Number of queens.
        size (int): Number of individuals in the population.

    Returns:
        list: List of individuals (board configurations).
    """
    return [generate_individual(n) for _ in range(size)]

def selection(population, fitnesses):
    """
    Selects the top 50% individuals based on fitness.

    Args:
        population (list): List of individuals.
        fitnesses (list): Corresponding fitness scores.

    Returns:
        list: Selected individuals for crossover.
    """
    sorted_pop = sorted(zip(population, fitnesses), key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_pop[:len(population)//2]]

def crossover(parent1, parent2):
    """
    Performs ordered crossover between two parents.

    Args:
        parent1 (list): First parent.
        parent2 (list): Second parent.

    Returns:
        list: Child individual.
    """
    point = random.randint(0, len(parent1) - 1)
    return parent1[:point] + [x for x in parent2 if x not in parent1[:point]]

def mutate(individual, mutation_rate=0.05):
    """
    Randomly swaps two positions in the individual with a given probability.

    Args:
        individual (list): Individual to mutate.
        mutation_rate (float): Probability of mutation.
    """
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(individual)), 2)
        individual[i], individual[j] = individual[j], individual[i]
