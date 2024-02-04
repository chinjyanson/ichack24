import numpy as np
import matplotlib.pyplot as plt

class StockGenerator:
    def __init__(self, type):
        self.STOCKTIME = 45 * 12 * 10  # number of times stock prices change a month
        self.skew_volatility = self.get_stock_parameters()
        self.x_val, self.y_val = self.waveformGenerator(self.skew_volatility[type][0], self.skew_volatility[type][1])

    def get_stock_parameters(self):
        # Define skew and volatility based on stock type
        skew_volatility = {
            'smp': (1.0002, 5),
            'bitcoin': (1, 300),
            'gold': (1, 50),
            'interestrate': (1.0001, 5)
        }
        return skew_volatility

    def waveformGenerator(self, skew, volatility):
        x_val = np.arange(0, self.STOCKTIME, 1)
        y_val = np.zeros(self.STOCKTIME)
        y_val[0] = np.random.randint(10, 50)
        for i in range(1, self.STOCKTIME):
            y_val[i-1] = skew * y_val[i-1]
            y_val[i] = np.clip(y_val[i-1] + np.random.randint(-volatility, volatility+1), 1, 2000)
        return x_val, y_val

    def saveGraph(self, filename, time):
        plt.plot(self.x_val[:time], self.y_val[:time])  # Limit the plot to the specified time
        plt.savefig(filename, bbox_inches='tight')
        plt.close()  # Close the plot to avoid displaying it again

    def findValue(self, time):
        return self.y_val[time]

    def findPercentage(self, time1, time2):
        return (self.y_val[time2] - self.y_val[time1]) / self.y_val[time1] * 100

# Example usage
stock_gen = StockGenerator("smp")
stock_gen.saveGraph('flaskr/static/smp.png', 1000)  # Viewing the graph up to 1000th time unit
stock_gen.saveGraph('flaskr/static/smp2.png', 2000)  # Viewing the graph up to 2000th time unit
