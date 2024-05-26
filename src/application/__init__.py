from abc import ABC, abstractmethod


class StocksDAO(ABC):
    @abstractmethod
    def update(self, stock: str, amount: int) -> dict:
        pass

    @abstractmethod
    def get_by_symbol(self, stock_id: str) -> list:
        pass


class StocksGateway(ABC):

    @abstractmethod
    def get_stock(self, symbol: str) -> dict:
        pass
