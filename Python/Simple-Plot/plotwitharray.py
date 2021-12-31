import matplotlib.pyplot as plt
import os

plt.style.use(['science','ieee'])

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

with plt.style.context(['science','ieee']):
    fig, ax = plt.subplots()
    ax.plot(x,y,label="labelsomthing")
    
    ax.set(xlabel='this is x label')
    ax.set(ylabel='this is y label')
    ax.legend()
    ax.autoscale(tight=True)
    
    ## save config
    savename = "test"+".pdf"
    if not os.path.exists("./figures"):
        os.makedirs("figures")
    fig.savefig("figures/"+savename)
    cmd = "SumatraPDF " + "figures/"+savename
    os.system(cmd)


