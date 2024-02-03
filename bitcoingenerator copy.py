import numpy as np
from matplotlib import pyplot as plt

MONTHS = 45 * 12
STOCKTIME = 45 * 12 * 10 # number of times stock prices change a month

def smpGenerator():

    x_val = np.arange(0,STOCKTIME,1)
    y_val = np.zeros(STOCKTIME)
    y_val[0] = np.random.randint(1, 10)
    for i in range(1, STOCKTIME):
        y_val[i-1] = 1.00015 * y_val[i-1]
        y_val[i] = np.clip(y_val[i-1] + np.random.randint(-5, 6), 1, 2000)

    plt.plot(x_val, y_val)
    plt.show()

    return x_val, y_val

def readGraph(time, xval, yval):
    newx = newy = []
    newx = xval[:time]
    newy = yval[:time]
    plt.plot(newx, newy)
    plt.show()

    return plt


xval, yval = smpGenerator()
plt = readGraph(12, xval, yval)

#plt.savefig('smp.png',  bbox_inches='tight')




