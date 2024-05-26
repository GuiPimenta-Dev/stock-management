from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from src.application.http import HttpException


class HTTPExceptionsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response

        except HttpException as e:
            return JSONResponse(status_code=e.status_code, content={"error": e.message})

        except Exception as e:
            error_message = str(e)
            return JSONResponse(status_code=500, content={"error": error_message})
