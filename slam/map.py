# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:29:13 2023

@author: HUNGTRAN
"""

import pandas
import matplotlib.pyplot as plt
import math
import sys    

df = pandas.read_csv('slam/sampling.csv', names=['angle', 'distance','q'])

plt.cla()
plt.ylim(-850,850)
plt.xlim(-850,850)

for row in df.iterrows():
  angle, distance, q = row[1]
  
  x = distance * math.cos(math.radians(float(angle)))     
  y = distance * math.sin(math.radians(float(angle)))

  plt.plot(x,y,marker='.',color='red')

print("saving image ...")
plt.savefig('lidar_map.png', bbox_inches='tight')
sys.exit(0)