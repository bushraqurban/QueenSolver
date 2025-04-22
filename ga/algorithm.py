import random
from .utils import fitness, generate_individual, initial_population, selection, crossover, mutate

def genetic_algorithm(n, pop_size=100, generations=1000, mutation_rate=0.05):
    """
    Solves the N-Queens problem using a genetic algorithm.

    Args:
        n (int): Number of queens.
        pop_size (int): Size of the population.
        generations (int): Number of generations to evolve.
        mutation_rate (float): Mutation rate for individuals.

    Returns:
        tuple: (Best individual, Fitness history, Generation found, Solved status)
    """
    population = initial_population(n, pop_size)
    total_pairs = n * (n - 1) // 2
    history = []

    for generation in range(generations):
        fitnesses = [fitness(ind) for ind in population]
        max_fit = max(fitnesses)
        history.append(max_fit)

        if max_fit == total_pairs:
            solution = population[fitnesses.index(max_fit)]
            return solution, history, generation, True

        selected = selection(population, fitnesses)
        next_gen = [max(zip(population, fitnesses), key=lambda x: x[1])[0]]  # Elitism

        while len(next_gen) < pop_size:
            parent1, parent2 = random.sample(selected, 2)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            next_gen.append(child)

        population = next_gen

    best_fit = max(fitnesses)
    best_board = population[fitnesses.index(best_fit)]
    return best_board, history, generations, False
