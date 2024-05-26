from datetime import datetime, timedelta

from src.application import StocksGateway


# This class uses an in-memory proxy to cache stock data for 5 minutes, implementing the Proxy Design Pattern.
# By caching data, we reduce unnecessary API requests, improving efficiency.
# In a real-world scenario, a more robust solution like Redis or Memcached could be used for caching.


class InMemoryStocksProxy(StocksGateway):
    def __init__(self, real_gateway):
        self.real_gateway = real_gateway
        self.cache = {}

    def get_stock(self, symbol):
        current_time = datetime.now()
        if symbol in self.cache:
            data, timestamp = self.cache[symbol]
            if current_time - timestamp < timedelta(minutes=5):
                print(f"Returning cached data for {symbol}")
                return data

        print(f"Fetching new data for {symbol}")
        data = self.real_gateway.get_stock(symbol)
        self.cache[symbol] = (data, current_time)
        return data
