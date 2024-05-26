from src.application import StocksGateway, StocksDAO


class GetStock:
    def __init__(self, stocks_gateway: StocksGateway, stocks_repository: StocksDAO):
        self.stocks_gateway = stocks_gateway
        self.stocks_repository = stocks_repository

    def execute(self, symbol):
        stock = self.stocks_gateway.get_stock(symbol)
        amount = self.stocks_repository.get_by_symbol(symbol)
        return {**stock, "amount": amount}
