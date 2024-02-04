from typing import Any
from modules import AssetManager, taxcalc, bitcoingenerator
from enum import Enum
import random

class Levels(Enum): # level, plus amount which is frac of income
    LOW = 0.15
    MED = 0.3
    HIGH = 0.55

class Player:
    def __init__(self) -> None:
        self.assets = AssetManager.AssetManager()
        self.income = 2000 # current monthly income (pounds)
        self.time   = 0 # time passed (in months)
        self.current_level = Levels.LOW # Happiness level (selectable)
        self.avg_happiness = Levels.LOW.value
        self.graphs = [bitcoingenerator.bitcoingenerator()]

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

        #TODO update asset values
        self.assets.updatevalue("sp500", 1.1) # e.g. s+p went up 10%

        old_income = self.income
        # Increase income (job progression)
        pay_raise = ((1.05 ** (1/12))) + (0 if random.randint(1,30) != 1 else (random.randint(10, 20)/100))
        self.income = round(self.income*pay_raise)

        self.time +=1

        return {"balancesheet":
                    {"income": old_income,
                    "tax": -1 * tax_amount,
                    "expenditures": -1 * expenditures
                    },
                "happinesslevel": self.current_level.name,
                "time": self.time,
                "value":self.assets.getTotalValue(),
                "news": {"title": "desc",
                         "title2": "desc2"}
                }

    def GenerateNews(self):

        for g in self.graphs:
            # is self.time in the right range?
            threeMonthChange = g.yval[self.time+3] - g.yval[self.time] if self.time + 3 < len(g.yval) else 0






players = []
players.append(Player())

def getplayer() -> Player:
    return players[0]
