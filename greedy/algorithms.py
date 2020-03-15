
import random
import numpy as np

def objective_function(photo1, photo2):
    #common tags
    common = len(set(photo1.tags).intersection(photo2.tags))
    print (common)
    # tags in photo1 but not in 2
    uncommon_photo1 = len(np.setdiff1d(photo1.tags, photo2.tags))
    print(uncommon_photo1)
    # tgs in photo2 but not in 1´
    uncommon_photo2 = len(np.setdiff1d(photo2.tags, photo1.tags))
    print(uncommon_photo2)
    return min(common, uncommon_photo1, uncommon_photo2)


def find_best_match(slide, photos):
    one = 1
    two = 2
    return one, two



def greedy(photos):
    random.shuffle(photos)
   
    vertical_photos = [p for p in photos if p.Horizontal == False]
    horizontal_photos = [p for p in photos if p.Horizontal == True]
    best = 0
    slideshow = []
    
    slideshow.append(horizontal_photos.pop())
    best_match_H, score_H = find_best_match(slideshow[-1], horizontal_photos)
    best_match_V, score_V = find_best_match(slideshow[-1], vertical_photos)
