# Binance Futures Trading Bot

A Python-based trading bot for Binance Futures Testnet (USDT-M).

## Features

- MARKET Orders
- LIMIT Orders
- STOP Orders
- BUY / SELL Support
- CLI-based User Input
- Input Validation
- Logging and Error Handling
- Structured Project Architecture

## Tech Stack

- Python 3.x
- Binance Futures API
- argparse
- logging
- Streamlit (optional UI)

---

## Project Structure

```bash
Binance_project/
│
├── client.py
├── orders.py
├── main.py
├── README.md
├── requirements.txt
├── trading.log
├── app.py
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run MARKET Order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

## Run LIMIT Order

```bash
python main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 84000
```

---

## Run STOP Order

```bash
python main.py --symbol BTCUSDT --side BUY --type STOP --quantity 0.002 --price 84000 --stopprice 84100
```

---

## Logging

All API requests, responses, and errors are logged in:

```bash
trading.log
```

---

## Optional UI

Run Streamlit UI:

```bash
python -m streamlit run app.py
```