from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from photo import Photo
import score


def calculate(*args):

    f = open(filename, 'r')

    photos = []

    lineNumber = 0
    for line in f:
        if (lineNumber != 0):
            photos.append(Photo(lineNumber-1, line))
        lineNumber += 1
    print(photos)
    return photos



root = Tk()

root.title("Google Hashcode 2019 solver")
filename = askopenfilename()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)	

ttk.Label(mainframe, text="Input file path").grid(column=1, row=3, sticky=(W, E))
ttk.Label(mainframe, text=filename).grid(column=1, row=4, sticky=(W, E))

ttk.Button(mainframe, text="Greedy Algorithm", command=calculate).grid(column=4, row=3, sticky=W)
ttk.Button(mainframe, text="Genetic Algorithm", command=calculate).grid(column=4, row=4, sticky=W)
ttk.Button(mainframe, text="Simulated Anneling", command=calculate).grid(column=4, row=5, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()