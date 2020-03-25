import math
import random

from FEUP_IART_2020.objective import *
from FEUP_IART_2020.utils import *


def simulated_annealing(photos):
    s = generate_slides(photos) #generate slides, sorted by horizontal and then vertical
    solution = organize_slides(s)
    score = ObjectiveFunction(solution)

    temp = 100
    temp_min = 1
    cooling_rate = 5
    itPerTemp = 100

    while temp > temp_min:
        it = 0

        while it < itPerTemp:
            new_solution = addOperator(solution)
            new_score = ObjectiveFunction(new_solution) #para dar positivo
            #print(new_score, " VS ", score)
            if new_score >= score: #so > diminui mt o nr de pontos,
                solution = new_solution
                score = new_score
            else:
                accProbability = acceptanceProbability(score, new_score, temp)
                if accProbability > random.random():
                    solution = new_solution
                    score = new_score

            it = it + 1

        temp = temp-cooling_rate

    print(score)
    return new_solution


def acceptanceProbability(score, new_score, temp):
    loss = abs(score-new_score)
    return math.exp(-(loss/temp))


def addRandomOperator(slides):
    #For example, in the travelling salesman problem each state is typically defined as a
    # permutation of the cities to be visited, and its neighbours are the set of permutations
    # produced by reversing the order of any two successive cities.
    # A new solution is generated by inverting the "place" of two successive images
    length = len(slides)-1-1 #[0,length-1] -> nao seleciona o ultimo
    idx = random.randrange(0, length)
    swapPositions(slides, idx, idx+1)

    return slides

def addOperator(slides):
    copy = slides.copy()

    length = len(copy)-1-1 #para nao apanhar o ultimo >>> por causa do swap
    idx = random.randrange(0, length)

    s = copy[idx]
    score = 0

    i = len(copy)-1

    for s1 in reversed(copy):
        new_score = s.interest(s1)
        if new_score > score:
            new_i = i
        score = new_score
        i = i-1

    #print(new_score, s.tags, copy[new_i].tags, new_s1.tags)
    swapPositions(copy, new_i, idx+1)
    return copy


def swapPositions(slides, pos1, pos2):
    slides[pos1], slides[pos2] = slides[pos2], slides[pos1]
    return slides


def organize_slides(slides):
    sol = sorted(slides, key=lambda x: x.getNrTags(), reverse=True) #ordenar por ordem crescente de nr de tags
    return sol