import random
import operator
import numpy as np
from Classes import Photo, Slide 
from objective import ObjectiveFunction

def solveRand(photos):
    
    slides = []
    for photo in photos:

        if len(slides)==0:
            slides.append(Slide(photo))  
        elif not slides[-1].Horizontal and not photo.Horizontal:
            slides[-1].addVertical(photo)
        else:
            slides.append(Slide(photo))

    return slides



def objective_function(slide1, slide2):
    #common tags
    common = len(set(slide1.tags).intersection(slide2.tags))
    # tags in photo1 but not in 2
    uncommon_slide1 = len(slide1.tags) - common
    # tgs in photo2 but not in 1´
    uncommon_slide2 = len(slide2.tags) - common
    return min(common, uncommon_slide1, uncommon_slide2)


def hill(photos):
    cycles = 50000
    best_score = 0
    vizinhanca = []
    tamanhao_vizinhanca = 10 
    #start random solution
    slides = solveRand(photos)
    length = len(slides)

    #get the scores of first soluton
    for i in range(0, length -1):
        slides[i].score = objective_function(slides[i], slides[i+1])
        best_score += slides[i].score

    current_index = 0

    while cycles > 0:
        #get vizinhanca
        for slide in slides:
            if slide 
      #  second_index = random.randint(first_index, first_index + 10)
        if first_index >= length - 2:
            first_index = 1
            continue
        if second_index > (length - 2):
            continue

        current_transitions = sum([objective_function(slides[first_index - 1], slides[first_index]), 
                               objective_function(slides[first_index], slides[first_index + 1]),
                               objective_function(slides[second_index - 1], slides[second_index]), 
                               objective_function(slides[second_index], slides[second_index + 1])])

        #new transitions with slides swaped
        temp_tansitions = sum([objective_function(slides[first_index - 1], slides[second_index]), 
                               objective_function(slides[second_index], slides[first_index + 1]),
                               objective_function(slides[second_index - 1], slides[first_index]), 
                               objective_function(slides[first_index], slides[second_index + 1])])

        if(temp_tansitions > current_transitions):
            #apply new configuration
            slides[first_index], slides[second_index] = slides[second_index], slides[first_index]
            slides[first_index - 1].score = objective_function(slides[first_index - 1], slides[first_index])
            slides[first_index].score = objective_function(slides[first_index], slides[first_index + 1])
            slides[second_index - 1].score = objective_function(slides[second_index - 1], slides[second_index])
            slides[second_index].score = objective_function(slides[second_index], slides[second_index + 1])
            #calculate new score
            best_score += temp_tansitions - current_transitions
            local_maximum = 0

        
       # first_index += 1
        cycles -= 1
        local_maximum += 1
        if local_maximum > 10000:
            print(first_index)
            first_index = random.randint(0, length - 2)
            print(first_index)
            local_maximum = 0
            print("jump")
        if cycles % 1000 == 0:
            print(cycles, " left")
            print(best_score)
    print("best score: ", best_score)