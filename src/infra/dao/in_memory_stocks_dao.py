from src.application import StocksDAO

# This class provides an in-memory implementation of the StocksRepository for simplicity.
# By adhering to good practices, we use the StocksRepository interface to define the required methods.
# This class simulates a database, but it can be easily extended to use a real database such as SQLite, MySQL, or PostgreSQL.
# To switch to a real database, simply implement the methods defined in the StocksRepository interface.


class InMemoryStocksDAO(StocksDAO):
    def __init__(self):
        self.stocks = {}

    def update(self, stock, amount):
        if stock in self.stocks:
            self.stocks[stock] += amount
        else:
            self.stocks[stock] = amount

    def get_by_symbol(self, stock_id):
        return self.stocks.get(stock_id, 0)
