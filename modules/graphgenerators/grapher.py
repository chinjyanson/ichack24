import random
from attr import dataclass
import numpy as np
import io
import base64
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('Agg')

@dataclass
class GenParams:
    monthmean: float = 1.013
    monthvar: float = 0.002

    # lat: float = 0.0

POINTS_PER_MONTH = 50
YEARS_TO_GEN = 20

class Generator:
    def __init__(self, params: GenParams) -> None:
        self.params = params
        self.y = np.full(1, 100)

        for _ in range(12*YEARS_TO_GEN):
            month = self.genMonth(self.y[-1] , POINTS_PER_MONTH)
            self.y = np.append(self.y, month)


    def genMonth(self, startval: float, count: int) -> list[int]:
        increase = np.random.normal(self.params.monthmean, self.params.monthvar)
        lf =  np.linspace(startval, startval*increase, count)
        hf = np.zeros(count)
        num = 0
        for i in range(len(hf)):
            num += random.randint(-2,2)
            hf[i] +=  num
        return lf + hf

    def getIncrease(self, idx_start, idx_end):
        return self.y[idx_end]/self.y[idx_start]


    def b64GraphPNG(self, idx_start, idx_end):
        s = io.BytesIO()
        rg = self.y[idx_start: idx_end]
        plt.plot(rg)  # Limit the plot to the specified time
        plt.axvline(x = len(rg)-POINTS_PER_MONTH, color = 'b', label = 'axvline - full height', linestyle="--")
        plt.savefig(s, format='png', bbox_inches="tight")
        plt.close()
        s = base64.b64encode(s.getvalue()).decode("utf-8").replace("\n", "")
        return 'data:image/png;base64,%s' % s


# Average yearly increase,
class SP500(Generator):
    def __init__(self) -> None:
        super().__init__(params=GenParams())


