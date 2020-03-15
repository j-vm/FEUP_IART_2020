
from load_file import load_file
from algorithms import *
import time


photos = load_file("./a_example.txt")

start_time = time.process_time()

greedy(photos)

print(time.process_time() - start_time, "seconds")