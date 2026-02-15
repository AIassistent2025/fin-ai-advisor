import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class MarketDataService:
    async def get_historical_data(self, symbol: str, days: int = 30):
        # Simulated data fetching logic
        dates = [datetime.now() - timedelta(days=x) for x in range(days)]
        data = {
            "date": dates,
            "close": np.random.uniform(100, 200, size=days),
            "volume": np.random.randint(1000, 10000, size=days)
        }
        df = pd.DataFrame(data)
        return df

    def calculate_volatility(self, df: pd.DataFrame):
        return df["close"].pct_change().std() * np.sqrt(252)
