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
            ("title", "desc"),
            ("title", "desc")
        ],
        NewsLevels.HIGH : [
            ("title", "desc"),
            ("title", "desc")
        ],


}}