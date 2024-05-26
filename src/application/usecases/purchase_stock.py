class PurchaseStock:
    def __init__(self, stocks_repository):
        self.stocks_repository = stocks_repository

    def execute(self, stock_name, amount):
        self.stocks_repository.update(stock_name, amount)
