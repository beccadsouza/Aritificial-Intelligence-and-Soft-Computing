import random as rd
import numpy as np
import sys

sys.setrecursionlimit(10000)


K = 50
iterations = 0
print("Boolean Equation is ((x1 AND x2) OR (x2 AND x3) OR (x3 AND x1))")


def fitness_function(chromosomes):
    ans = []
    for chromosome in chromosomes:
        x1, x2, x3 = chromosome[0], chromosome[1], chromosome[2]
        boolean_result = (x1 and x2) or (x2 and x3) or (x3 and x1)
        if boolean_result:
            ans = chromosome
            break
    return ans


# creation of chromosomes
c1 = []
c2 = []
for i in range(0, 3):
    c1.append(rd.randint(0, 1))
    c2.append(rd.randint(0, 1))
if c1 == c2:
    np.random.shuffle(c1)
print("Population Intialisation - ")
print("Chromosome 1 - ", c1)
print("Chromosome 2 - ", c2)

# fitness function evaluation
chromosome = fitness_function([c1, c2])

while len(chromosome) == 0:
    iterations += 1
    print("All chromosomes failed fitness test. Next iteration")

    # crossover of chromosomes - single point crossover
    c1 = c1[:2] + [c2[2]]
    c2 = c2[:2] + [c1[2]]
    print("Crossover - ")
    print("Chromosome 1 - ", c1)
    print("Chromosome 2 - ", c2)

    # mutation of chromosomes - interchanging mutation
    pos = rd.randint(0, 2)
    c1[pos] = int(not c1[pos])
    c2[pos] = int(not c2[pos])
    print("Mutation - ")
    print("Chromosome 1 - ", c1)
    print("Chromosome 2 - ", c2)

    chromosome = fitness_function([c1, c2])

    if iterations > K and len(chromosome)==0:
        print("Max iterations reached. Solution not found.")
        exit()

print("Chromosome passed the fitness test - ", chromosome)

"""
 OUTPUT
 
runfile('/home/beckss/Desktop/AISC/Genetic Algorithm/code.py', wdir='/home/beckss/Desktop/AISC/Genetic Algorithm')
Boolean Equation is ((x1 AND x2) OR (x2 AND x3) OR (x3 AND x1))
Population Intialisation - 
Chromosome 1 -  [0, 1, 0]
Chromosome 2 -  [0, 0, 1]
All chromosomes failed fitness test. Next iteration
Crossover - 
Chromosome 1 -  [0, 1, 1]
Chromosome 2 -  [0, 0, 1]
Mutation - 
Chromosome 1 -  [0, 1, 0]
Chromosome 2 -  [0, 0, 0]
All chromosomes failed fitness test. Next iteration
Crossover - 
Chromosome 1 -  [0, 1, 0]
Chromosome 2 -  [0, 0, 0]
Mutation - 
Chromosome 1 -  [0, 0, 0]
Chromosome 2 -  [0, 1, 0]
All chromosomes failed fitness test. Next iteration
Crossover - 
Chromosome 1 -  [0, 0, 0]
Chromosome 2 -  [0, 1, 0]
Mutation - 
Chromosome 1 -  [0, 0, 1]
Chromosome 2 -  [0, 1, 1]
Chromosome passed the fitness test -  [0, 1, 1]

"""