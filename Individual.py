import random

GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP 
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

TARGET = "I love GeeksforGeeks"

class Individual(object):
    def __init__(self, chromosome = None):
        if(chromosome):
            self.chromosome = chromosome 
        else:
            self.chromosome = self.create_gnome()

        self.fitness = self.cal_fitness()

    def mutated_genes(self):
        global GENES
        gene = random.choice(GENES)
        return gene
    
    def create_gnome(self):
        global TARGET
        gnome_len = len(TARGET)
        return [self.mutated_genes() for _ in range(gnome_len)]
    
    def mate(self, par2):
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            prob = random.random()

            if prob < 0.45:
                child_chromosome.append(gp1)
            elif prob < 0.9:
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(self.mutated_genes())
        
        return Individual(child_chromosome)
    
    def cal_fitness(self):
        global TARGET
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET):
            if gs != gt: fitness += 1
        return fitness