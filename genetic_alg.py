import random
from Individual import *

POPULATION_SIZE = 100

def main():
    global POPULATION_SIZE
    generation = 1

    found = False
    population = []

    for i in range(POPULATION_SIZE):
        gnome = Individual()
        gnome.create_gnome()
        population.append(gnome)

    while not found:
        population = sorted(population, key = lambda x:x.fitness)

        if population[0].fitness <= 0:
            print(population[0].chromosome)
            found = True
            break

        new_generation = []

        s = int((10*POPULATION_SIZE)/100)
        new_generation.extend(population[:s])

        s = int((POPULATION_SIZE)/2)
        for i in range(s):
            p1 = random.choice(population[:s])
            p2 = random.choice(population[:s])

            child = p1.mate(p2)
            new_generation.append(child)

        population = new_generation

        print("Generation: {}\tString: {}\tFitness:  {}".format(generation, "".join(population[0].chromosome),population[0].fitness))

        generation += 1

    print("Generation: {}\tString: {}\tFitness: {}".format(generation, "".join(population[0].chromosome), population[0].fitness)) 
  
if __name__ == '__main__': 
    main() 
