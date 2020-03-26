from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import time
from Classes import Photo, Slide
from objective import ObjectiveFunction
import ntpath



from simulated_annealing import simulated_annealing
from tabu_search import tabu_search
from hill_climbing import hill


def loadFile():
    f = open(filename, 'r')
    global photos
    lineNumber = 0
    for line in f:
        if (lineNumber != 0):
            photos.append(Photo(lineNumber-1, line))
        lineNumber += 1
   

    
    #tabu_search(photos)
   # simulated_annealing(photos)

    #geneticStartup(photos)




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



def solveGreedy(*args):
    
    return 0


def solveHillClimbing(*args):
    hill(args[0], args[1])
    return 0

def solveGeneticAlgorithm(*args):
    return 1

def solveSimulatedAnneling(*args):
    return 1

def fileLoaded(*args):
    ttk.Label(mainframe, text="Choose algorithm!").grid(column=1, row=8, sticky=(W))
    ttk.Button(mainframe, text="Random Solution", command=solveRand).grid(column=1, row=10, sticky=W)
    ttk.Button(mainframe, text="Greedy Algorithm", command=solveGreedy).grid(column=1, row=12, sticky=W)
    ttk.Button(mainframe, text="Genetic Algorithm", command=solveGeneticAlgorithm).grid(column=1, row=14, sticky=W)
    ttk.Button(mainframe, text="Simulated Anneling", command= lambda: solveSimulatedAnneling(photos)).grid(column=1, row=16, sticky=W)
    ttk.Button(mainframe, text="Hill Climbing", command= lambda: solveHillClimbing(photos, 500000)).grid(column=1, row=18, sticky=W)
    ttk.Label(mainframe, text="Cycles: ").grid(column=2, row=18,  sticky=E)

    
    hill_cycles = ttk.Entry(mainframe, width=9)
    hill_cycles.insert(0, '5000000')
    hill_cycles.grid(column=3, row=18,  sticky=W)

root = Tk()

root.title("Google Hashcode 2019 solver")
filename = askopenfilename()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)	

ttk.Label(mainframe, text="Input file path").grid(column=1, row=3, sticky=(W, E))
ttk.Label(mainframe, text=ntpath.basename(filename)).grid(column=1, row=4, sticky=(W, E))


photos = []
ttk.Button(mainframe, text="Load File", command= loadFile).grid(column=2, row=3, sticky=W)
fileLoaded()
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
