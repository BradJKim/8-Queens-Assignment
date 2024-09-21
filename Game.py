import random
from Individual import *

POPULATION_SIZE = 100

class Game(object):
    def __init__(self):
        global POPULATION_SIZE
        self.generation = 1 
        self.population = []
        
        for i in range(POPULATION_SIZE):
            gnome = Individual()
            self.population.append(gnome)

    def reset_game(self):
        global POPULATION_SIZE
        new_population = []

        for i in range(POPULATION_SIZE):
            gnome = Individual()
            new_population.append(gnome)

        self.population = new_population
        self.generation = 1

    def next_gen(self):
        curr_population = self.population

        curr_population = sorted(curr_population, key = lambda x:x.fitness)

        if curr_population[0].fitness <= 0:
            print("Generation: {}\tString: {}\tFitness:  {}".format(self.generation, curr_population[0].board, curr_population[0].fitness))
            return True
            
        new_generation = []

        s = int((20*POPULATION_SIZE)/100)
        new_generation.extend(curr_population[:s])

        s = int((POPULATION_SIZE)/2)
        for i in range(s):
            p1 = random.choice(curr_population[:s])
            p2 = random.choice(curr_population[:s])

            child = p1.mate(p2)
            new_generation.append(child)

        curr_population = new_generation

        print("Generation: {}\tString: {}\tFitness:  {}".format(self.generation, curr_population[0].board, curr_population[0].fitness))

        self.generation += 1
        self.population = curr_population

        return False

    
