class Photo:
      
       def __init__(self, id, info):
              splitInfo = info.split()
              self.id = id
              self.Vertical = True if splitInfo[0] == "V" else False
              self.tags = set(splitInfo[2::])
              print(self.tags)

