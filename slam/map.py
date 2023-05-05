# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:29:13 2023
@author: HUNGTRAN
"""

import pandas
import matplotlib.pyplot as plt
import math    

df = pandas.read_csv('lidar_data_01.csv', names=['angle', 'distance','q'])

plt.cla()
plt.ylim(-2000,3000)
plt.xlim(-4000,2000)

for row  in df.iterrows():
  angle, distance, q = row[1]

  x = distance * math.cos(math.radians(angle))     
  y = distance * math.sin(math.radians(angle))

  plt.plot(x,y,marker='.',color='red')

plt.savefig('lidar_map.png', bbox_inches='tight')
plt.show()