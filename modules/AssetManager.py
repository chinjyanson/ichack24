class Asset:
    def __init__(self, value: float):
        # self.name    = name # name of underlying asset
        self.value   = value # value of underlying asset

        # def roi() :
        #     # Asset can generate dividends or is on loan
        #     # roi to be determined
        #     return

class Savings(Asset):
    def __init__(self, value: float = 0):
        super().__init__(value=value)

class Gold(Asset):
    def __init__(self, value: float = 0):
        super().__init__(value=value)

class SP500(Asset):
    def __init__(self, value: float = 0):
        super().__init__(value=value)

# class Bonds(Asset):
#     def __init__(self, value: float = 0):
#         super().__init__(value=value)

#     def roi(interest: int):
#         value *= (1 + interest)

class Bitcoin(Asset):
    def __init__(self, value: float = 0):
        super().__init__(value=value)


class AssetManager:
    def __init__(self):
        self.assets = {"savings": Savings(),"sp500": SP500(), "gold": Gold(), "crypto": Bitcoin(), } # "bonds": Bonds()

    def buy(self, name: str, value: float) -> tuple[bool, str]:
        if value <= 0:
            return (False, "Value must be positive")
        if self.assets["savings"].value < value:
            return (False, f"Not enough savings savings:{self.assets['savings'].value} want:{value}")
        self.assets["savings"].value -= value
        self.assets[name].value += value
        return (True, "Success")

    def sell(self, name: str, value: float) -> tuple[bool, str]:
        if value<=0:
            return (False, "Value must be positive")
        if self.assets[name].value < value:
            return (False, "Selling more than owned")
        self.assets[name].value -= value
        self.assets["savings"].value += value
        return (True, "Success")

    def updatevalue(self, name: str, increase: float):
        """Update the value of an asset, based on the price increase"""
        self.assets[name].value *= increase

    def getAssets(self):
        return self.assets.keys()

    def getValues(self):
        """Gets dict of all assets with values"""
        return {n: self.assets[n].value for n in self.assets}

    def getTotalValue(self):
        """Gets total owned value"""
        return sum([self.assets[n].value for n in self.assets])

    def increaseSavings(self, value:float):
        self.assets["savings"].value += value

