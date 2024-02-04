from typing import Any
from modules import AssetManager, taxcalc
from enum import Enum
import random
from modules import newsgen
# from modules.graphgenerators.generic import StockGenerator
from modules.graphgenerators import grapher
from modules.newsgen import *

class Levels(Enum): # level, plus amount which is frac of income
    LOW = 0.35
    MED = 0.50
    HIGH = 0.65

class Player:
    def __init__(self) -> None:
        self.assets = AssetManager.AssetManager()
        self.income = 2000 # current monthly income (pounds)
        self.time   = 0 # time passed (in months)
        self.current_level = Levels.LOW # Happiness level (selectable)
        self.avg_happiness = Levels.LOW.value
        interestgraph = grapher.InterestRate()
        self.graphs = {
            "sp500":grapher.SP500(),
            "gold":grapher.Gold(),
            "crypto":grapher.Bitcoin(),
            "interestrate": interestgraph,
            "savings": grapher.Savings(interestgraph.y)
        }

    def __getattr__(self, name: str) -> Any:
        """pass other stuff through direct to assetmanager"""
        return getattr(self.assets, name)

    def execmonth(self) -> dict[Any]:
        """Called by api to progress to next month"""
        """
            IDEA:
            In each month, a player is allowed to make choices. A player has x amount in their current savings.
            These choices include:
                1. Buying assets if x is enough
                2. Selling assets that are owned

            Once the player has exhausted all options, they should choose to end their turn, then we update all state variables and move to the next month.
            Importantly, we don't allow a player to sell their assets in the current month and expect an increase in their savings. This should only get updated next month. (any objections?)

            Inflow -
                1. Interest earned on assets
                2. Wages
                ( 3. Cash earned by selling )
            Outflow -
                ( 1. Taxes imposed on selling assets )
                ( 2. Taxes on income )
                # 2. Cash lost by buying
                3. Monthly expenditure on essentials
        """

        takeHomePay = taxcalc.calculate_takehome_income(self.income*12)/12
        tax_amount = takeHomePay - self.income

        # expenditure for happiness
        expenditures = takeHomePay * self.current_level.value
        takeHomePay -= expenditures
        #TODO update average happiness

        self.assets.increaseSavings(takeHomePay)


        # update asset valuses
        capital_gains = {}
        for asset in list(self.assets.getAssets()):
            increase = self.graphs[asset].getIncrease(grapher.POINTS_PER_MONTH*(12+self.time), grapher.POINTS_PER_MONTH*(13+self.time))
            capital_gains[asset] = self.assets.updatevalue(asset, increase)


        old_income = self.income
        # Increase income (job progression)
        pay_raise = ((1.05 ** (1/12))) + (0 if random.randint(1,30) != 1 else (random.randint(10, 20)/100))
        self.income = round(self.income*pay_raise)

        self.time +=1

        # Generate news
        asset, articles = random.choice(list(newsgen.news.items()))
        asset_data = self.graphs[asset]
        asset_prediction = asset_data.getIncrease(grapher.POINTS_PER_MONTH*(12+self.time), grapher.POINTS_PER_MONTH*(13+self.time)) - 1
        news_level = 1

        if asset_prediction < 0:
            news_level = 0
        elif asset_prediction > 0:
            news_level = 2
        # news = random.choice(articles[NewsLevels(news_level)])

        news = dict(newsgen.news[asset][NewsLevels(news_level)])

        return {
            "balancesheet":{
                "income": old_income,
                "tax": -1 * tax_amount,
                "expenditures":  expenditures,
                "capitalgains": capital_gains
            },
            "happinesslevel": self.current_level.name,
            "time": self.time,
            "value": self.assets.getTotalValue(),
            "news": news,
            "hint": Hints[random.randint(0,len(Hints)-1)],
            "graphs":
                {item:
                    {
                    "graph": self.graphs[item].b64GraphPNG(0 + grapher.POINTS_PER_MONTH*self.time, grapher.POINTS_PER_MONTH*(12+self.time)),
                    "increasepm": self.graphs[item].getIncrease(grapher.POINTS_PER_MONTH*(11+self.time), grapher.POINTS_PER_MONTH*(12+self.time)),
                    "increasepy": self.graphs[item].getIncrease(grapher.POINTS_PER_MONTH*(0+self.time), grapher.POINTS_PER_MONTH*(12+self.time))
                    }
                 for item in self.graphs
                 }
            }

    def GenerateNews(self):

        for g in self.graphs:
            # is self.time in the right range?
            threeMonthChange = g.yval[self.time+3] - g.yval[self.time] if self.time + 3 < len(g.yval) else 0


players = []
#players.append(Player())
