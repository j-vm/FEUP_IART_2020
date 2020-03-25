import math
import random
import numpy as np
from objective import ObjectiveFunction
from Classes import *

#Dependencies: Numpy 

#To Avoid repetition we will use:
#For the crossover -> Ordered Crossover (OX1)
#For the mutation -> Reverse Sequence Mutation (RSM).

def genInitialPop(arrayLen, nSol):
       gen1 = []
       for i in range (0,nSol):
              individual = list(range(0, arrayLen-1))
              random.shuffle(individual)
              gen1.append(individual)
       return gen1

def geneticStartup(photos):
       nGen = int(input("How many generations?"))
       nSol = int(input("How many solutions pre generation?"))
       mutProb = float(input("What is the mutation probability from 0 to 1?"))

       for i in range(0,nGen):
              if i is 0:
                     population = genInitialPop(len(photos), nSol)
              else:
                     population = reproduce(population, fitness)
                     population = mutate(population, mutProb)
              fitness = calculateFitness(population, photos)
              print("(" + str(i) +"," + str(max(fitness))+")")


def calculateFitness(population, photos):
    fitness = []           
    for individual in population:
       slides = []
       for photo in individual:
        if len(slides)==0:
            slides.append(Slide(photos[photo]))  
        elif not slides[-1].Horizontal and not photos[photo].Horizontal:
            slides[-1].addVertical(photos[photo])
        else:
            slides.append(Slide(photos[photo]))
       fitness.append(ObjectiveFunction(slides))

    return fitness


def reproduce(population, fitness):
       newPopulation = []
       minFitness = min(fitness) 
       probability = [i - (minFitness - 1) for i in fitness] #Avoiding getting stuck in an "all soutions have fitness = 0" situation
       #also subtracting the min fitness to avoid all probabilities being very similar when solution values are high and close 
       probability = [float(i)/sum(probability) for i in probability] # Normalizing porbability for random.choice
       print(probability)
       solutionLength = len(population[0])
       for i in range(0, len(population)):
              child = []
              parents = np.random.choice(len(population), 2, replace=False, p=probability)
              parent1 = population[parents[0]]
              parent2 = population[parents[1]]
              crossoverPoint = np.random.choice(solutionLength)
              for i in range(crossoverPoint, crossoverPoint + int(solutionLength//2)):
                     if i < solutionLength:
                            child.append(parent1[i])
                     else:
                            child.append(parent1[i-solutionLength])
              for photo in parent2:
                     if photo not in child:
                            child.append(photo)
              newPopulation.append(child)
       return newPopulation

       
def mutate(population, mutProb):

       return population