from array import array
import os 
import time
import csv


# 1: get compound names and other data related to compounds
with open('file.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
arr = data[0]
# print(arr)
for x in range(1, len(arr)):
    command = 'python3 attempt2.py '+str(x)
    print(command)
    os.system(command)
    time.sleep(10) # Delay

