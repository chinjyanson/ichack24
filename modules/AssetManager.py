
class Asset:
    def __init__(self, price: int, name: str, id: int, amount: int):
        self.name    = name
        self.value   = value
        self.id      = id 

        def roi() :
            # Asset can generate dividends or is on loan
            # roi to be determined         
            return 
    
class Gold(Asset):
    def __init__(self, value: int, name: str, id: int):
        super().__init__(value, name, id)
        self.name = "Gold"

class SP500(Asset):
    def __init__(self, value: int, name: str, id: int):
        super().__init__(value, name, id)
        self.name = "S&P500"
    
class Bonds(Asset):
    def __init__(self, value: int, name: str, id: int):
        super().__init__(value, name, id)
        self.name = "Bonds"
    
    def roi(interest: int):
        value *= (1 + interest)
class Bitcoin(Asset): 
    def __init__(self, value: int, name: str, id: int):
        super().__init__(value, name, id)
        self.name = "Bitcoin"



class AssetManager:
    def __init__(self):
        self.assets = {"SP500": SP500(), "Gold": Gold(), "Bitcoin": Bitcoin(), "Bonds": Bonds()}
        
    def buy(self, name: str, amount: int):            
        self.assets[name].amount += amount # check

    def sell(self, name: str, amount: int):
        self.assets[name].amount -= amount
    def updateValue(self, name: str, val: int):
        self.assets[name].value = val
    

     
        
     
        

        