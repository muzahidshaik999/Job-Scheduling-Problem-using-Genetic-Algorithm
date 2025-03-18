import random
import numpy as np # type: ignore

# Parameters
NUM_JOBS = 6  # Number of jobs
NUM_MACHINES = 3  # Number of machines
POP_SIZE = 10  # Population size
NUM_GENERATIONS = 100  # Maximum generations
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2

# Generate random processing times for jobs
processing_times = np.random.randint(1, 10, NUM_JOBS)

# Initialize population
def initialize_population():
    return [np.random.randint(0, NUM_MACHINES, NUM_JOBS) for _ in range(POP_SIZE)]

# Fitness function (minimizing max completion time)
def fitness(chromosome):
    machine_times = np.zeros(NUM_MACHINES)
    for job, machine in enumerate(chromosome):
        machine_times[machine] += processing_times[job]
    return max(machine_times)

# Selection (Roulette Wheel)
def selection(population):
    fitness_values = np.array([1 / (1 + fitness(ch)) for ch in population])  # Inverse to minimize
    probabilities = fitness_values / fitness_values.sum()
    selected_indices = np.random.choice(len(population), size=2, p=probabilities)
    return population[selected_indices[0]], population[selected_indices[1]]

# Crossover (Two-Point Crossover)
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point1, point2 = sorted(random.sample(range(NUM_JOBS), 2))
        child1 = np.concatenate((parent1[:point1], parent2[point1:point2], parent1[point2:]))
        child2 = np.concatenate((parent2[:point1], parent1[point1:point2], parent2[point2:]))
        return child1, child2
    return parent1, parent2

# Mutation (Random Job Reassignment)
def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        job = random.randint(0, NUM_JOBS - 1)
        chromosome[job] = random.randint(0, NUM_MACHINES - 1)
    return chromosome

# Genetic Algorithm Execution
population = initialize_population()
for generation in range(NUM_GENERATIONS):
    new_population = []
    for _ in range(POP_SIZE // 2):
        parent1, parent2 = selection(population)
        child1, child2 = crossover(parent1, parent2)
        new_population.extend([mutate(child1), mutate(child2)])
    population = sorted(new_population, key=fitness)[:POP_SIZE]  # Keep best solutions

# Best schedule found
best_solution = min(population, key=fitness)
best_fitness = fitness(best_solution)
print("Best Schedule:", best_solution)
print("Minimum Completion Time:", best_fitness)