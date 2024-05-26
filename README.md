
# Stock Management API

This project provides a simple Stock Management API using FastAPI. The API allows users to fetch stock information and purchase stocks. The project includes an in-memory proxy for caching stock data to reduce unnecessary API requests.

## Table of Contents

- [Docker](#docker)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  - [GET /stocks/{symbol}](#get-stocks)
  - [POST /stocks/{symbol}](#post-stocks)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)

## Docker

  ```sh
    docker build -t stocks .
    docker run -p 8000:8000 stocks
  ```

## Usage

1. Run the FastAPI server:
    ```sh
    uvicorn src.main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

## API Endpoints

### GET /stocks/{symbol}

Fetches stock information for a given symbol.

- **URL:** `/stocks/{symbol}`
- **Method:** `GET`
- **Path Parameters:**
  - `symbol` (string): The stock symbol to fetch information for.
- **Response:**
  - `200 OK` on success with the stock information.

### POST /stocks/{symbol}

Purchases stock for a given symbol.

- **URL:** `/stocks/{symbol}`
- **Method:** `POST`
- **Path Parameters:**
  - `symbol` (string): The stock symbol to purchase.
- **Request Body:**
  - `amount` (integer): The amount of stock to purchase.
- **Response:**
  - `201 Created` on success with the purchase information.
  - `422 Unprocessable Entity` if the amount is not provided.


## Running Tests

1 - Run the tests using `pytest`:
    
  ```sh    
  pytest .
  ```

