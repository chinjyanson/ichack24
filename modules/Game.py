from typing import Any
from modules import AssetManager, taxcalc
from enum import Enum

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

        moneyforsavings = self.income

        # Tax income
        tax_amount = self.income * taxcalc.income_tax_rates(self.income*12) # annualize (not realistic)
        moneyforsavings -= tax_amount

        # expenditure for happiness
        expenditures = moneyforsavings * self.current_level.value
        moneyforsavings -= expenditures
        #TODO update average happiness

        self.assets.increaseSavings(moneyforsavings)

        #TODO update asset values
        self.assets.updatevalue("sp500", 1.1) # e.g. s+p went up 10%

        # Increase income (job progression)
        old_income = self.income
        self.income += 100

        return {"balancesheet":
                    {"income": old_income,
                    "tax": -1 * tax_amount,
                    "expenditures": -1 * expenditures
                    },
                "happinesslevel": self.current_level.name,
                "time": self.time
                }

players = []
players.append(Player())

def getplayer() -> Player:
    return players[0]
