import pytest
from src.application.usecases.get_stock import GetStock
from src.application.usecases.purchase_stock import PurchaseStock
from src.infra.cache.in_memory_stocks_proxy import InMemoryStocksProxy
from src.infra.dao.in_memory_stocks_dao import InMemoryStocksDAO
from tests.mocks.stub_stocks_gateway import StubStocksGateway
from datetime import datetime, timedelta


def test_if_amount_is_saved_on_database():
    stocks_repository = InMemoryStocksDAO()
    usecase = PurchaseStock(stocks_repository)

    usecase.execute("AAPL", 10)

    assert stocks_repository.get_by_symbol("AAPL") == 10


def test_if_amount_is_updated_on_database():
    stocks_repository = InMemoryStocksDAO()
    usecase = PurchaseStock(stocks_repository)

    usecase.execute("AAPL", 10)
    usecase.execute("AAPL", 5)

    assert stocks_repository.get_by_symbol("AAPL") == 15


def test_if_stock_is_returned_correctly():
    stocks_gateway = StubStocksGateway()
    stocks_repository = InMemoryStocksDAO()
    stocks_repository.update("AAPL", 10)
    usecase = GetStock(stocks_gateway, stocks_repository)

    response = usecase.execute("AAPL")

    assert response == {
        "status": "OK",
        "from": "2023-01-09",
        "symbol": "AAPL",
        "open": 130.465,
        "high": 133.41,
        "low": 129.89,
        "close": 130.15,
        "volume": 7.0790813e07,
        "afterHours": 129.85,
        "preMarket": 129.6,
        "amount": 10,
        "performance": {"5 Day": "1,42%"},
    }

@pytest.fixture
def proxy_gateway():
    real_gateway = StubStocksGateway()
    return InMemoryStocksProxy(real_gateway)

def test_fetch_new_data(proxy_gateway):
    symbol = "AAPL"
    
    data = proxy_gateway.get_stock(symbol)
    
    assert proxy_gateway.cache[symbol][0] == data
    assert proxy_gateway.cache[symbol][1] != None

def test_return_cached_data(proxy_gateway):
    symbol = "AAPL"
    proxy_gateway.get_stock(symbol) 
    cached_timestamp = proxy_gateway.cache[symbol][1] 
    
    proxy_gateway.get_stock(symbol)  
    
    assert cached_timestamp == proxy_gateway.cache[symbol][1]

def test_cache_expiration(proxy_gateway):
    symbol = "AAPL"
    proxy_gateway.get_stock(symbol)  
    expired_cache = (proxy_gateway.cache[symbol][0], datetime.now() - timedelta(minutes=6))
    proxy_gateway.cache[symbol] = expired_cache
    
    proxy_gateway.get_stock(symbol) 
    
    assert expired_cache != proxy_gateway.cache[symbol]