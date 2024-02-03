from enum import Enum

class NewsLevels(Enum):
    LOW = 0.8
    MED = 1
    HIGH = 1.2


news = {
    "sp500":{
        NewsLevels.LOW : [
            ("SP500 predicted to fall", "desc"),
            ("sp500 bad", "desc")
        ],
        NewsLevels.MED : [
            ("Federal Reserve Increases Interest Rates to 5%", "desc"),
            ("", "desc")
        ],
        NewsLevels.HIGH : [
            ("Global Markets Reeling as War Erupts in Ukraine", ""),
            ("Housing Markets Plummet After Big Banks 'Fail'", "desc"),
            ("Earthquake Hits Japan Once More", "desc")
        ],


}}