import numpy as np
from matplotlib import pyplot as plt

def stonks(type):
    STOCKTIME = 45 * 12 * 10 # number of times stock prices change a month
    skew, volatility = get_stock_parameters(type)
    x_val, y_val = waveformGenerator(STOCKTIME, skew, volatility)

    if type == 'smp':
        saveGraph(x_val, y_val, 'flaskr/static/smp.png')
    elif type == 'bitcoin':
        saveGraph(x_val, y_val, 'flaskr/static/bitcoin.png')
    elif type == 'gold':
        saveGraph(x_val, y_val, 'flaskr/static/gold.png')
    elif type == 'interestrate':
        saveGraph(x_val, y_val, 'flaskr/static/interest.png')
    else:
        print("Invalid type")

def get_stock_parameters(type):
    # Example: Define skew and volatility based on stock type
    if type == 'smp':
        skew = 1.0002
        volatility = 5
    elif type == 'bitcoin':
        skew = 1
        volatility = 300
    elif type == 'gold':
        skew = 1
        volatility = 50
    elif type == 'interestrate':
        skew = 1.0001
        volatility = 5
    else:
        print("Invalid type")

    return skew, volatility

def waveformGenerator(STOCKTIME, skew, volatility):
    x_val = np.arange(0, STOCKTIME, 1)
    y_val = np.zeros(STOCKTIME)
    y_val[0] = np.random.randint(10, 50)
    for i in range(1, STOCKTIME):
        y_val[i-1] = skew * y_val[i-1]
        y_val[i] = np.clip(y_val[i-1] + np.random.randint(-volatility, volatility+1), 1, 2000)
    return x_val, y_val

def saveGraph(x_val, y_val, filename):
    plt.plot(x_val, y_val)
    plt.savefig(filename, bbox_inches='tight')
    plt.close()  # Close the plot to avoid displaying it again

# Example usage
stonks('smp')




