class StockRecommender:
    def __init__(self, budget, risk_profile, sectors):
        self.budget = budget
        self.risk_profile = risk_profile
        self.sectors = sectors
        # For demonstration, static results
        self.top_stocks = [
            {"ticker": "AAPL", "allocation": 0.4},
            {"ticker": "MSFT", "allocation": 0.3},
            {"ticker": "GOOG", "allocation": 0.2},
            {"ticker": "TSLA", "allocation": 0.1},
            {"ticker": "AMZN", "allocation": 0.0}
        ]
        self.metrics_df = [
            {"ticker": "AAPL", "sharpe": 1.2, "volatility": 0.15},
            {"ticker": "MSFT", "sharpe": 1.1, "volatility": 0.18}
        ]
