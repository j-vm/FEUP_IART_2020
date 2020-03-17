
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
    times = 10
    best_score = 0
    temp_score = 0
    #start random solution
    slides = solveRand(photos)
    length = len(slides)
    temp_solution = slides
    #get the scores of first soluton
    for i in range(0, length -1):
        slides[i].score = objective_function(slides[i], slides[i+1])
        best_score += slides[i].score
    #searches for the optimal solution
    while times>0:
        first_index = random.randint(0, length - 1)
        second_index = random.randint(0, length - 1)
        if first_index == second_index:
            continue
        temp_solution[first_index], temp_solution[second_index] = temp_solution[second_index], temp_solution[first_index]
        for i in range(0, length -1):
            temp_solution[i].score = objective_function(temp_solution[i], temp_solution[i+1])
            temp_score += temp_solution[i].score
        if (temp_score >= best_score):
            slides = temp_solution
            best_score = temp_score
            temp_score = 0
        else:
            temp_score = 0
        times -= 1
        print(times, " seconds")
    print("best score: ", best_score)
    '''
    n = 0
    for i in slides:
        print("slide ", n)
        print("score ", i.score)
        print(i.tags)
        n += 1
    '''
    