from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.application.http import UnprocessableEntity
from src.application.usecases.get_stock import GetStock
from src.application.usecases.purchase_stock import PurchaseStock
from src.infra.cache.in_memory_stocks_proxy import InMemoryStocksProxy
from src.infra.dao.in_memory_stocks_dao import InMemoryStocksDAO
from src.infra.gateways import StocksGatewayAdapter

router = APIRouter()

stocks_gateway = InMemoryStocksProxy(StocksGatewayAdapter())
stocks_dao = InMemoryStocksDAO()


@router.get("/stocks/{symbol}")
async def get_stocks(symbol):

    usecase = GetStock(stocks_gateway, stocks_dao)

    response = usecase.execute(symbol.upper())
    return response


@router.post("/stocks/{symbol}")
async def post_stocks(request: Request, symbol):
    body = await request.json()
    amount = body.get("amount")

    if not amount:
        raise UnprocessableEntity("Amount is required")

    usecase = PurchaseStock(stocks_dao)

    response = usecase.execute(symbol.upper(), amount)
    return JSONResponse(status_code=201, content=response)
