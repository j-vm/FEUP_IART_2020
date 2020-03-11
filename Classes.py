class Photo:
      
       def __init__(self, id, info):
              splitInfo = info.split()
              self.id = id
              self.Horizontal = True if splitInfo[0] == "H" else False
              self.tags = set(splitInfo[2::])
              #print(self.tags)

class Slide:
       def __init__(self, photo):
              self.photo1 = photo.id
              self.photo2 = None
              self.tags = photo.tags
              self.points = 0
              self.Horizontal = photo.Horizontal

       def addVertical(self, photo):
              if photo.Horizontal:
                     print("Slide is Full")
                     exit("Tried to add a photo to a slide that was full")
              else:
                     self.photo2 = photo.id
                     self.tags.update(photo.tags)

       def generateOutput(self):
              if self.Horizontal:
                     return str(self.photo1)
              else:
                     return str(self.photo1) + " " + str(self.photo2)


