
from Classes import Photo, Slide


def load_file(filename):
    f = open(filename, 'r')
    photos = []
    lineNumber = 0
    for line in f:
        if (lineNumber != 0):
            photos.append(Photo(lineNumber-1, line))
        lineNumber += 1
    return photos