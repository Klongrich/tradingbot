class coindata:

    def __init__(self, ticker, polo):
        self.ticker = ticker
        self.data = polo.api_query('returnTicker');

    def bid(self):
        return (self.data[self.ticker]['highestBid']);

    def ask(self):
        return (self.data[self.ticker]['lowestAsk']);

    def ask(self):
        return (self.data[self.ticker]['lowestAsk']);

    def volume(self):
        return (self.data[self.ticker]['quoteVolume']);

    def price(self):
        return (self.data[self.ticker]['last']);

    def dayhigh(self):
        return (self.data[self.ticker]['high24hr']);

    def percentchange(self):
        return (self.data[self.ticker]['percentChange']);

    def basevolume(self):
        return (self.data[self.ticker]['baseVolume']);

    def currentBalance(self):
        return (self.data[self.ticker]['returnBalances'])