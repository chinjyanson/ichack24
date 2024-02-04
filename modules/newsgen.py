from enum import Enum

class NewsLevels(Enum):
    LOW = 0.8
    MED = 1
    HIGH = 1.2


news = {
    "sp500":{
        NewsLevels.LOW : [
            ("S&P500 predicted to fall", "desc"),
            ("S&P500 bad", "desc"),
            ("Slight Downturn: S&P 500 Faces Mild Headwinds Amidst Market Shifts, Investors Cautiously Monitor Trends", "desc"),
            ("S&P 500 Faces Sharp Decline: Market Turbulence Sparks Concerns among Investors", "desc")
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
    };

    "gold": {
        NewsLevels.LOW : [
            ("Gold Prices Show Resilience Amidst Market Volatility: Investors Find Comfort in Precious Metal's Stability", "desc"),
            ("Demand for gold slumps", "desc"),
            ("US dollar is predicted to strengthen", "desc"),
        ],
        NewsLevels.MED : [
            ("New massive gold deposit found, supply of gold to greatly increase", "desc"),
            ("Gold Prices Dip Moderately: Market Adjustments Prompt Caution Among Investors","desc")
        ],
        NewsLevels.HIGH : [
            ("Gold Prices Plummet in Face of Strengthening Dollar and Economic Headwinds: Investors Brace for Market Challenges", ""),
            ("Gold Prices Experience Sharp Decline as Economic Recovery Gathers Pace: Investors Shift Focus Amidst Reduced Safe-Haven Appeal", "desc")
        ]
    };

    "bond" {
        NewsLevels.LOW : [
            ("UK government ", "desc"),
            ("Demand for gold slumps", "desc"),
            ("US dollar is predicted to strengthen", "desc"),
        ],
        NewsLevels.MED : [
            ("New massive gold deposit found, supply of gold to greatly increase", "desc"),
            ("Gold Prices Dip Moderately: Market Adjustments Prompt Caution Among Investors","desc")
        ],
        NewsLevels.HIGH : [
            ("Gold Prices Plummet in Face of Strengthening Dollar and Economic Headwinds: Investors Brace for Market Challenges", ""),
            ("Gold Prices Experience Sharp Decline as Economic Recovery Gathers Pace: Investors Shift Focus Amidst Reduced Safe-Haven Appeal", "desc")
        ]
    };

    "crypto" {

    };
}

