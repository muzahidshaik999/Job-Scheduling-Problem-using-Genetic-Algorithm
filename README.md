# Job Scheduling Problem using Genetic Algorithm

## Problem Statement
The Job Scheduling Problem involves assigning a set of jobs to a set of machines to minimize the total completion time. Each job has a processing time, and each machine can process only one job at a time. The objective is to find an optimal schedule that minimizes the maximum completion time across all machines using a Genetic Algorithm (GA).

## Genetic Algorithm Approach
### 1. Chromosome Representation
Each chromosome represents a possible schedule of jobs on machines. The chromosome is represented as an array where:
- Each gene corresponds to a job.
- The value of each gene represents the machine on which the job is scheduled.

### 2. Fitness Function
The fitness function evaluates the quality of the schedule by computing the maximum completion time of all jobs across machines. A lower completion time means a higher fitness score.

### 3. Genetic Operators
#### Selection (Roulette Wheel Selection)
- Selects two parent chromosomes from the population based on their fitness.
- Probability of selection is inversely proportional to the completion time (lower time is better).

#### Crossover (Two-Point Crossover)
- Two crossover points are randomly selected.
- Genes between the two points are swapped between the two parents to create two offspring.

#### Mutation (Random Job Reassignment)
- A randomly selected job is assigned to a new random machine.
- This helps introduce diversity in the population and prevents premature convergence.

### 4. Algorithm Execution
- **Initialization**: Generate an initial population of job schedules.
- **Genetic Operations**: Apply selection, crossover, and mutation to create a new generation.
- **Termination Condition**: The algorithm stops when the maximum number of generations is reached or an optimal schedule is found.

## Implementation Details
- **Number of Jobs**: 6
- **Number of Machines**: 3
- **Population Size**: 10
- **Generations**: 100
- **Crossover Rate**: 0.8
- **Mutation Rate**: 0.2
- **Processing Time**: Randomly generated for each job

## Output
The algorithm outputs:
- The best schedule found.
- The minimum completion time for the jobs.

## Requirements
- Python 3
- NumPy

## Usage
Run the Python script to execute the Genetic Algorithm and find the optimal job scheduling solution.

```sh
python job_scheduling_ga.py
```

## Example Output
```sh
Best Schedule: [1 0 2 1 2 0]
Minimum Completion Time: 12
```
This indicates that each job is assigned to a specific machine, and the optimal schedule minimizes the total completion time to 12 time units.

