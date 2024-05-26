from src.application.usecases.get_stock import GetStock
from src.infra.gateways import StocksGatewayAdapter
from src.infra.dao.in_memory_stocks_dao import InMemoryStocksDAO

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.application.controllers import router
from src.application.middlewares import HTTPExceptionsMiddleware


@pytest.fixture()
def client():
    app = FastAPI()
    app.add_middleware(HTTPExceptionsMiddleware)
    app.include_router(router)
    yield TestClient(app)

def test_get_stock_from_api_scraping_and_database(client):
    
    response = client.get("/stocks/AAPL")

    assert [
        "status",
        "from",
        "symbol",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "afterHours",
        "preMarket",
        "performance",
        "amount",
    ] == list(response.json().keys())

def test_it_should_get_the_saved_value(client):
    
    amount = 10
    client.post("/stocks/AAPL", json={"amount": amount})
    response = client.get("/stocks/AAPL")

    assert response.json()["amount"] == amount

def test_it_should_return_201_if_amount_is_present(client):
    
    amount = 10
    response = client.post("/stocks/AAPL", json={"amount": amount})

    assert response.status_code == 201

def test_it_should_return_422_if_amount_is_missing(client):
    
    response = client.post("/stocks/AAPL", json={})

    assert response.status_code == 422
    


