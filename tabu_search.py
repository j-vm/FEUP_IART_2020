

def tabu_search(photos):
    slides = generate_slides(photos)

    last = []
    solution = []
    current = slides.pop()
    solution.append(current)

    #neighborhood = getCandidates(current, slides, solution)
    #print("end")
    it = 0
    while it < len(slides):
        #find list of candidate moves
        neighborhood = getCandidates(current, slides, solution)

        #select the best solution
        bestMatch = selectSolution(current, neighborhood)

        if bestMatch == -1: #current nao tem tags em comum com nada, fica para ultimo
            last.append(current)

        else: #update tabu memory and make the move
            solution.append(bestMatch)
            current = bestMatch

        it = it + 1

    solution = solution + last
    print(ObjectiveFunction(solution))
    return 0


def selectSolution(comparable, neighborhood):
   '''score = 0
    to_return = -1

    for s in neighborhood:
        new_score = comparable.interest(s)

        if new_score > score:
            score = new_score
            to_return = s'''
   maxPoints = 0
   selected = -1

   for s in neighborhood:
       if len(s.tags) > 2*maxPoints:
           points = s.interest(comparable)

           if points > maxPoints :
               maxPoints = points
               selected = s

   return selected


def getCandidates(slide, slides, cantMatch):
    candidates = []

    canSearch = list(set(slides) ^ set(cantMatch))
    for s in canSearch:
        if len(slide.tags.intersection(s.tags)) > 0: #slides com tags em comum
            candidates.append(s)

    return candidates
