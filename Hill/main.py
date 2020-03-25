
from Load_file import load_file
from algorithms import hill
import time
from new_hill import *


photos = load_file("./Hill/b_lovely_landscapes.txt")

print("Loading file...")
start_time = time.process_time()
cycles = 1000000
score = new_hill(photos, cycles)

time = time.process_time() - start_time
print(time, " seconds of processor time")

with open("./Hill/hill_results.txt", "+a") as f:
    f.write("%i, %i, %f \n" % (cycles, score, time))
