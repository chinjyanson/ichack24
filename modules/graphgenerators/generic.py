import numpy as np
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('Agg')
import io
import base64

class StockGenerator:
    def __init__(self, stocktype):
        self.STOCKTIME = 45 * 12 * 10  # number of times stock prices change a month
        self.skew_volatility = self.get_stock_parameters()
        self.type=stocktype
        self.x_val, self.y_val = self.waveformGenerator(self.skew_volatility[stocktype][0], self.skew_volatility[stocktype][1])

    def get_stock_parameters(self):
        # Define skew and volatility based on stock type
        skew_volatility = {
            'snp500': (1.0002, 5),
            'bitcoin': (1, 300),
            'gold': (1, 50),
            'interestrate': (1, 5)
        }
        return skew_volatility

    def waveformGenerator(self, skew, volatility):
        x_val = np.arange(0, self.STOCKTIME, 1)
        y_val = np.zeros(self.STOCKTIME)
        y_val[0] = np.random.randint(10, 50)
        for i in range(1, self.STOCKTIME):
            y_val[i-1] = skew * y_val[i-1]
            y_val[i] = np.clip(y_val[i-1] + (y_val[i-1]* np.random.randint(-volatility, volatility+1)*0.005), 1, 2000)
        return x_val, y_val

    def saveGraph(self, filename, time):
        plt.plot(self.x_val[:time], self.y_val[:time])  # Limit the plot to the specified time
        plt.savefig(filename, bbox_inches='tight')
        plt.close()  # Close the plot to avoid displaying it again

    def b64GraphPNG(self, t_start, t_end):
        s = io.BytesIO()
        plt.plot(self.x_val[t_start:t_end], self.y_val[t_start:t_end])  # Limit the plot to the specified time
        plt.savefig(s, format='png', bbox_inches="tight")
        plt.close()
        s = base64.b64encode(s.getvalue()).decode("utf-8").replace("\n", "")
        return 'data:image/png;base64,%s' % s

    def b64GraphSVG(self, t_start, t_end):
        s = io.BytesIO()
        plt.plot(self.x_val[t_start:t_end], self.y_val[t_start:t_end])  # Limit the plot to the specified time
        plt.savefig(s, format='svg', bbox_inches="tight")
        plt.close()
        s = base64.b64encode(s.getvalue()).decode("utf-8").replace("\n", "")
        return 'data:image/svg+xml;utf-8;base64,%s' % s


    # def saveInterest(self, filename, time):


    def findValue(self, time):
        return self.y_val[time]

    def findPercentage(self, time1, time2):
        return (self.y_val[time2] - self.y_val[time1]) / self.y_val[time1] * 100

# Example usage
if __name__ == "__main__":
    stock_gen = StockGenerator("smp")
    stock_gen.saveGraph('flaskr/static/smp.png', 1000)  # Viewing the graph up to 1000th time unit
    stock_gen = StockGenerator("bitcoin")
    stock_gen.saveGraph('flaskr/static/bitcoin.png', 1000)
    stock_gen = StockGenerator("gold")
    stock_gen.saveGraph('flaskr/static/gold.png', 1000)
    stock_gen = StockGenerator("interestrate")
    stock_gen.saveGraph('flaskr/static/interestrate.png', 1000)
