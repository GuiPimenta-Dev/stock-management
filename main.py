from fastapi import FastAPI
 
from src.application.controllers import router 
from src.application.middlewares import HTTPExceptionsMiddleware


app = FastAPI()
app.add_middleware(HTTPExceptionsMiddleware)
app.include_router(router)
 
if __name__ == "__main__":
    import uvicorn
 
    uvicorn.run(app, host="0.0.0.0", port=8001)
