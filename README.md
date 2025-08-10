# TradingView to OKX Webhook Service

This project provides a service to forward TradingView webhook alerts to OKX for automated trading. It's designed to run on Google Cloud Run and uses Docker for containerization.

## Features

- Receives webhook alerts from TradingView.
- Processes the alerts and translates them into OKX API-compatible orders.
- Secure and lightweight, suitable for serverless deployment.

## Prerequisites

- Python 3.10 or later
- Docker installed locally for containerization
- Google Cloud account for deploying the service

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/tjsums/tv2okx.git
    cd tv2okx
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Build the Docker image:
    ```bash
    docker build -t tv2okx-service .
    ```

2. Run the service locally:
    ```bash
    docker run -p 8080:8080 tv2okx-service
    ```

3. Deploy to Google Cloud Run:
    - Push the Docker image to a container registry.
    - Deploy the service to Google Cloud Run with the required environment variables.

## Environment Variables

- `OKX_API_KEY`: Your OKX API key.
- `OKX_API_SECRET`: Your OKX API secret.
- `OKX_PASS`: The passphrase for your OKX account.
- `TRADINGVIEW_SECRET`: A secret key to validate incoming webhook requests from TradingView.

## License

This project is licensed under the MIT License.