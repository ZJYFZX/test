"""
This file runs Ising simulation
Created: Dec. 26, 2022
Last Edited: Dec. 28, 2022
By Jinyuan Zhang
"""

import IsingGrid
import Ising
import matplotlib as mpl
import matplotlib.pyplot as plt
from copy import deepcopy
from PIL import Image
import numpy as np
from numpy import random

# Fundamental parameters

size = 28
temperature = 1
steps = 100000
interval = 100
Jfactor = 0.9
'''Jfactor = 0.1 * random.random((size, size))
for i in range(14):
    for j in range(size):
        Jfactor[i][j] += 0.9'''

Hfactor = 0
print(Jfactor)
# Load image

im = Image.open(r"C:\Users\DELL\Pictures\Saved Pictures\FCA6147083BE34446A9661A39A6D5326.jpg")
# im.show()
img = np.array(im)
img.resize((size, size))

# Generate grid

g = Ising.Grid(size, Jfactor, Hfactor, img)
g.randomize()

# Animation parameters

fig, ava = plt.subplots()
data = []

# Simulation

print("开始仿真.")

for step in range(steps):

    # Single/cluster Filp

    clusterSize = g.Flip(temperature)
    #clusterSize = g.clusterFlip(temperature)

    if (step + 1) % interval == 0:
        data.append(deepcopy(g.canvas))

    if (step + 1) % (1 * interval) == 0:
        print("Step ", step + 1, "/", steps, ", Cluster size ", clusterSize, "/", size * size)

print("仿真完成.")

# 画图

print("开始画图.")
LAST = Image.fromarray(img)  # numpy 转 image类
LAST.show()
for frame in range(0, len(data)):
    ava.cla()
    ava.imshow(data[frame], cmap=mpl.cm.winter)
    ava.set_title("Step {}".format(frame * interval))
    plt.pause(0.001)

print("图像完成.")
