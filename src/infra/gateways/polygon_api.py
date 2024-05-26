import os
import requests
import datetime
from dotenv import load_dotenv

load_dotenv()


class PolygonAPI:

    @staticmethod
    def get_stock(symbol):

        # The challenge said to retrieve today's data, but when attempting to retrieve todays data this is what i receive:
        # {
        # 	"status": "NOT_AUTHORIZED",
        # 	"request_id": "825d7ef471e7126a06358cb8131dfa84",
        # 	"message": "Attempted to request today's data before end of day. Please upgrade your plan at https://polygon.io/pricing"
        # }
        # So I decided to retrieve yesterday's data instead.

        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        yesterday = yesterday.strftime("%Y-%m-%d")
        url = f"https://api.polygon.io/v1/open-close/{symbol}/{yesterday}"

        POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
        querystring = {"apiKey": POLYGON_API_KEY}

        response = requests.request("GET", url, params=querystring)

        if response.status_code == 404:
            return {
                "status": "NOT FOUND",
                "from": yesterday,
                "symbol": symbol,
                "open": None,
                "high": None,
                "low": None,
                "close": None,
                "volume": None,
                "afterHours": None,
                "preMarket": None,
            }

        return response.json()
