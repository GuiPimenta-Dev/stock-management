from src.application import StocksGateway
from src.infra.gateways.marketwatch_scraper import MarketWatchScraper
from src.infra.gateways.polygon_api import PolygonAPI

# The StocksGatewayAdapter class integrates the Polygon API and MarketWatchScraper for maximum decoupling.
# By using the Adapter Design Pattern, this class adapts the StocksGateway interface to work
# seamlessly with both the Polygon API and MarketWatchScraper.


class StocksGatewayAdapter(StocksGateway):
    def __init__(self):
        self.polygon_stocks_api = PolygonAPI()
        self.marketwatch_scraper = MarketWatchScraper()

    def get_stock(self, symbol):
        stocks = self.polygon_stocks_api.get_stock(symbol)
        performance = self.marketwatch_scraper.get_performance(symbol)
        return {**stocks, "performance": performance}
