
# Best Stocks to Buy Project

## Overview
This project helps you find the best stocks to buy within your investment budget.
- Enter your budget.
- The app fetches real-time stock prices from the internet.
- It calculates key metrics: annual return, volatility, and Sharpe ratio.
- It ranks the stocks using a custom scoring system.
- It recommends the best stocks and how many shares you can buy with your budget.

## Folder Structure
- src/
    - data_loader.py: Fetches real-time stock data.
    - metrics.py: Calculates annual return, volatility, and Sharpe ratio.
    - scoring.py: Custom scoring system for ranking stocks.
    - allocator.py: Allocates budget among recommended stocks.
    - logger.py: Handles logging.

- app/api/main.py: Main orchestrator script.
- requirements.txt: Project dependencies.

## Next Steps
- Fill in the metrics.py, allocator.py, and data_loader.py modules.
- Update main.py to accept user budget and output recommendations.
