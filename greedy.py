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

    #vphotos_paired = pair_vPhotos(vertical_photos)
    sort_vPhotos(vertical_photos)

    #slides.append(vphotos_paired)

    #for s in slides:
    #    print(s.tags)

    #print(ObjectiveFunction(slides))
    return 1

#return slides with possible combination of vertical photos
def pair_vPhotos(vPhotos):
    slides = []
    length = len(vPhotos)

    if length == 0:
        return []
    elif length == 2:
        s = Slide(vPhotos[0])
        s.addVertical(vPhotos[1])
        return s

    elif ((length % 2) == 0):
        for idx in range(length):
               s1 = Slide(vPhotos[idx])
               s1.addVertical(vPhotos[idx+1])
               slides.append(s1)
    else:
        print("One pic will be left out")

    return slides


def byLengthTags(photo):
    return len(photo.tags)

#sort vertical photos by its number of tags
# group the largest with the smallest and the second largest with the second smallest
# -> every slide with the same number of tags
def sort_vPhotos(vPhotos):
    for p in vPhotos:
        print(p.id)
    sorted = vPhotos.sort(byLengthTags)

    for p1 in sorted:
        print(p1.id)

    return sorted