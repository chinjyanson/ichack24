import numpy as np
import matplotlib.pyplot as plt

def smpGenerator():
    
    xrandom = np.random.randint(0,300,1000)
    x_val = np.sort(xrandom)
    y_val = np.zeros(1000)
    y_val[0] = np.random.randint(1, 200)
    for i in range(1, 1000):
        y_val[i] = np.clip(y_val[i-1] + np.random.randint(-5, 5 + 1), 1, 200)
    
    plt.plot(x_val, y_val)
    plt.show()

    return x_val, y_val

def readGraph(time, xval, yval):
    length = len(xval)
    newx = newy = []
    newx = xval[:time]
    newy = yval[:time]
    plt.plot(newx, newy)
    plt.show()


xval, yval = smpGenerator()
readGraph(500, xval, yval)


    

