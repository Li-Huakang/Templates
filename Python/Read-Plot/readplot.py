import numpy as np
import matplotlib.pyplot as plt
import csv
import os

plt.style.use(['science', 'ieee', 'no-latex', 'cjk-sc-font'])
# win安装字体名字是 Noto Serif SC
# 但是python找的字体是 Noto Serif CJK SC
plt.rcParams.update({
    "font.family": "serif",   # specify font family here
    "font.serif": ["Noto Serif SC"]})  # specify font here

filename = './data.csv'
header = 5
ender = -1
# load data
file = open(filename)
lines = file.readlines()
rows = len(lines) - header + ender

datamat = np.zeros((rows, 2))

row = 0
for line in lines[header:ender]:
    line = line.strip().split(',')
    datamat[row, :] = line[:2]
    row += 1
# print(datamat)

t = datamat[:, 0]
v = datamat[:, 1]


fig, ax = plt.subplots()
ax.plot(t, v, '--')


ax.set(xlabel='时间 (s)')
ax.set(ylabel='V (V)')

ax.autoscale(tight=True)

# save config
savename = "fig" + ".pdf"
if not os.path.exists("./figures"):
    os.makedirs("./figures")
fig.savefig("./figures/" + savename)
cmd = "SumatraPDF " + "./figures/" + savename
os.system(cmd)
