from src.application import StocksGateway


class StubStocksGateway(StocksGateway):

    def get_stock(self, symbol):
        return {
            "status": "OK",
            "from": "2023-01-09",
            "symbol": symbol,
            "open": 130.465,
            "high": 133.41,
            "low": 129.89,
            "close": 130.15,
            "volume": 7.0790813e07,
            "afterHours": 129.85,
            "preMarket": 129.6,
            "performance": {"5 Day": "1,42%"},
        }
