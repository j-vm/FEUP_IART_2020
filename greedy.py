from Classes import Photo, Slide
from objective import ObjectiveFunction


def getTags(photos): #useful to get the tags of a slide
    tags = []
    for photo in photos:
        for tag in photo.tags:
            if not tag in tags:
                tags.append(tag)

    return (tags)

def generate_slides(photos):
    slides = []
    vertical_photos = []
    for photo in photos:
        if photo.Horizontal:
            slides.append(Slide(photo))
        else:
            vertical_photos.append(photo)

    sortedvPhotos = sort_vertical_photos(vertical_photos)

    vertical_slides = pair_vPhotos(sortedvPhotos)

    for vs in vertical_slides:
        slides.append(vs)


    print("Pontos:" , ObjectiveFunction(slides))

    return slides

#return slides with possible combination of vertical photos
def pair_vPhotos(vPhotos):
    slides = []
    length = len(vPhotos)

    if length == 0:
        return []
    elif length == 2:
        s = Slide(vPhotos[0])
        s.addVertical(vPhotos[1])
        return [s]
    elif ((length % 2) == 0):
        l = length//2
        for idx in range(l): #match primeiro com o ultimo
               s1 = Slide(vPhotos[idx])
               s1.addVertical(vPhotos[length-idx-1])
               slides.append(s1)
    else: #eliminar a foto que esta exatamente no meio; match primeiro com o ultimo
        print("One pic will be left out.")
    return slides



def sort_vertical_photos(vPhotos):
    v_sorted = sorted(vPhotos, key=lambda x: x.nr_tags, reverse=False) #ordenar por ordem crescente de nr de tags
    return v_sorted


