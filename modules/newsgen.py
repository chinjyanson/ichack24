from enum import Enum

class NewsLevels(Enum):
    LOW = 0.8
    MED = 1
    HIGH = 1.2


news = {
    "sp500":{
        NewsLevels.LOW : [
            ("Layoffs in the tech sector", "Microsoft Leads Another Busy Week Of Tech Layoffs That Sees More Cuts From Google, Salesforce And Flexport"),
            ("SMiddle East war could spark global recession, say Wall Street experts", "A global recession could be set in motion by the conflict in the Middle East as the humanitarian crisis compounds the challenges facing an already precarious world economy, two of Wall Street’s biggest names have warned."),
            ("If Interest Rates Continue To Rise, What Happens To Stock Prices?", "With interest rates at their highest levels in decades, the stock market doing so well this year has been a head-scratcher.")
        ],
        NewsLevels.MED : [
            ("Florida Man Trapped in Unlocked Closet For Two Days", "John Arwood, 31, and Amber Campbell, 25, were found in a janitor’s closet on the Daytona State College campus."),
            ("‘My mind had been shattered into a million pieces’: inside the Scientology-linked UK rehab centre", "‘My mind had been shattered into a million pieces’: inside the Scientology-linked UK rehab centreIt’s listed on the NHS website and claims to be a ‘world leader’ in tackling substance abuse. But there is a shocking side to the Narconon addiction facility – as our nine-month investigation reveals")
            ("Mac Jones Reveals He Called Tom Brady To Discuss Never Calling Tom Brady Again","FOXBOROUGH, MA—Sharing details about a recent conversation with the former New England field general, Patriots quarterback Mac Jones revealed this week that he called Tom Brady to discuss never calling Tom Brady again.")
        ],
        NewsLevels.HIGH : [
            ("Covid global health emergency is over, WHO says", "The World Health Organization (WHO) has declared that Covid-19 no longer represents a 'global health emergency'. "),
            ("Treasury decreases interest rates, signalling a strengthening economy", "The US central bank has signalled it could start cutting interest rates soon if inflation continues to fall."),
            ("Nvidia smashes records as company's value rises by £232bn in a month - but bad news for Tesla", "Tesla's market cap shrank by £151.6bn - 24% - after Elon Musk warned growth in 2024 will be 'notably lower' than previous years.")
        ],
    },

    "gold": {
        NewsLevels.LOW : [
            ("New Gold Reserves Found In Scandinavia", "New rare earth deposits descovered in norway reduces europes dependance on foreign imports"),
        ],
        NewsLevels.MED : [
            ("Florida Man Arrested for Crashing Car into Mall; Says He Was Trying to Time Travel", "This Florida Man thought he had everything he needed to travel through time if only he could duplicate the way they did it in Back to the Future."),
            ("Police Say Florida Man with No Arms and No Legs Is Armed and on the Run","Sean Petrozzino, who lost both his legs and hands – as well as parts of his arm – to bacterial meningitis is wanted by police to answer questions about the murder of his parents."),
            ("Florida woman tries to kill husband over postcard from ex-girlfriend from six decades ago: Police", "NORTH MIAMIA BEACH, Fla. - A Florida man told police his wife of more than 50 years tried to kill him when he received a postcard from an ex-girlfriend."),
            ("A Giant Bird Killed Its Owner. Now It Could Be Yours.", "Florida Man attacked and killed by pet Cassowaries. Becomes first human killed by the species since 1926.")
        ],
        NewsLevels.HIGH : [
            ("Is gold the solution to toughing out the current rough economic situation?", "Investors can invest in gold through exchange-traded funds (ETFs), buying stock in gold miners and associated companies, and purchasing a physical product such as coins or bullion."),
        ]
    },

    "bond": {
        NewsLevels.LOW : [
            ("Gold Prices Plummet in Face of Strengthening Dollar and Economic Headwinds: Investors Brace for Market Challenges", "desc"),
            ("Gold Prices Experience Sharp Decline as Economic Recovery Gathers Pace: Investors Shift Focus Amidst Reduced Safe-Haven Appeal", "desc"),
            ("Gold prices struggle before inflation", "desc"),
        ],
        NewsLevels.MED : [
            ("Top 5 gold rings to buy for your loved ones", "desc"),
            ("Distinguishing between Fool's gold and real gold","Real gold weights more than fool's gold which shares a deceptively similar golden lustre")
        ],
        NewsLevels.HIGH : [
            ("Gold shines as US Economy slows", ""),
            ("", "desc")
        ]
    },

    "crypto" : {
        NewsLevels.LOW : [
            ("Bitcoin founder jailed", "desc"),
            ("Elon musk slams newest cryptocurrency dodocoin, 'its a scam'", "desc"),
            ("Etherium prices hit a new low , speculators fear more to come", "desc"),
        ],
        NewsLevels.MED : [
            ("", "desc"),
            ("Gold Prices Dip Moderately: Market Adjustments Prompt Caution Among Investors","desc")
        ],
        NewsLevels.HIGH : [
            ("'To the moon!!', reddit users rave at the recent metoric rise of notascamcoin", ""),
            ("Sam Bankman-'freed': Sam is out of jail", "Sam Bankman Fried has been released on parole and announced that he will be creating a new company, FTY")
        ]
    }
}

Hints = [
    'An index mutual fund or ETF (exchange-traded fund) tracks the performance of a specific market benchmark—or "index," like the popular S&P 500 Index—as closely as possible. That`s why you may hear people refer to indexing as a "passive" investment strategy.',
    'contrary '
]