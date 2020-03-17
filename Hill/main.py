
from Load_file import load_file
from algorithms import hill
import time


photos = load_file("./Hill/b_lovely_landscapes.txt")

print("Loading file...")
start_time = time.process_time()

hill(photos)

print(time.process_time() - start_time, "seconds")