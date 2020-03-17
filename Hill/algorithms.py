
import random
import numpy as np
from Classes import Photo, Slide 

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
    uncommon_slide1 = len(np.setdiff1d(slide1.tags, slide2.tags))
    # tgs in photo2 but not in 1´
    uncommon_slide2 = len(np.setdiff1d(slide2.tags, slide1.tags))
    return min(common, uncommon_slide1, uncommon_slide2)


def hill(photos):
    times = 10000
    best_score = 0
    temp_score = 0
    #start random solution
    slides = solveRand(photos)
    length = len(slides)
    temp_solution = slides
    temp_slide1 = slides[0]
    temp_slide2 = slides[1]
    #get the scores of first soluton
    for i in range(0, length -1):
        slides[i].score = objective_function(slides[i], slides[i+1])
        best_score += slides[i].score
    #searches for the optimal solution
    while times>0:
        first_index = random.randint(0, length - 2)
        second_index = random.randint(0, length - 2)
        
        if first_index == second_index or first_index == 0 or second_index == 0:
            continue

        temp_slide1 = slides[first_index]
        temp_slide2 = slides[second_index]

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
            #calculate new score
            best_score += temp_tansitions - current_transitions
        times -= 1
        if times % 100 == 0:
            print(times, " cicles left")
    print("best score: ", best_score)

    