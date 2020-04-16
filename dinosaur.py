'''
The first file contains statistics about various dinosaurs. The second file contains additional data.
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)

Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
Do not print any other information.
'''

import csv
import math


d = {}
b = {}

with open('dataset2.csv') as ds2:
  csvDataSet2 = csv.reader(ds2)
  for item in csvDataSet2:
    #print(item)
    if item[2] == 'bipedal':
      d[item[1]] = item[0]
print(d)

with open('dataset1.csv') as ds1:
  csvDataSet1 = csv.reader(ds1)
  next(csvDataSet1)
  for item in csvDataSet1:
    #print(item)
    if item[0] in d:
      b[item[1]] = item[0]

print(b)

c = {}
s = []
for key, value in b.items():
  speed = (value/d[key] - 1) * math.sqrt(value * 9.8)
  c[key] = speed
  s.append(speed)

print(c)
print(s)
print(sorted(s, reverse = True))

for speed in s:
  print(d.get(speed))
  





    




