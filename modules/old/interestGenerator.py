import numpy as np
import matplotlib.pyplot as plt

def smpGenerator():
    xrandom = np.arange(0, 1000, 100)
    x_val = np.sort(xrandom)
    y_val = np.zeros(10)
    y_val[0] = np.random.randint(0, 50)
    for i in range(1, 10):
        y_val[i] = np.clip(y_val[i-1] + np.random.randint(-1, 1 + 1), 0, 50)

    plt.step(x_val, y_val)
    # plt.show()
#
    return x_val, y_val

def readGraph(time, xval, yval):
    length = len(xval)
    newx = newy = []
    newx = xval[:time]
    newy = yval[:time]
    plt.step(newx, newy)
    # plt.show()


xval, yval = smpGenerator()
readGraph(500, xval, yval)




