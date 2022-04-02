import matplotlib.pyplot as plt
import os

plt.style.use(['science','ieee', 'no-latex', 'cjk-sc-font'])
# win安装字体名字是 Noto Serif SC
# 但是python找的字体是 Noto Serif CJK SC
plt.rcParams.update({
    "font.family": "serif",   # specify font family here
    "font.serif": ["Noto Serif SC"]})  # specify font here

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

import numpy as np
from numpy import polyfit, poly1d
# 拟合
coeff = polyfit(x, y, 1)
print(coeff)
xx = np.linspace(1, 5, 10)


fig, ax = plt.subplots()
ax.plot(x, y, 'g.', label = "测试数据")
ax.plot(xx, coeff[0] * xx + coeff[1], '--', label="拟合数据")

ax.set(xlabel='x')
ax.set(ylabel='y')

ax.text(2,3,f"$y = {{{coeff[0]:.0}}}*x+{{{coeff[1]:.0}}}$")
ax.legend()
# ax.autoscale(tight=True)

## save config
savename = "测试"+".tiff"
if not os.path.exists("./figures"):
    os.makedirs("figures")
fig.savefig("figures/"+savename)
cmd = "SumatraPDF " + "figures/"+savename
os.system(cmd)