import pandas as pd
from datetime import date

from etl.core.base_transformer import BaseTransformer


class YahooTransformer(BaseTransformer):
    def __init__(self, symbol: str):
        self.symbol = symbol

    def transform(self, raw_df):
        if raw_df is None or len(raw_df) == 0:
            return []

        records = []
        for _, row in raw_df.iterrows():
            d = row["Date"]
            if isinstance(d, (str,)):
                d = date.fromisoformat(d)

            records.append(
                {
                    "symbol": self.symbol,
                    "date": d.date() if hasattr(d, "date") else d,
                    "open": float(row["Open"]),
                    "high": float(row["High"]),
                    "low": float(row["Low"]),
                    "close": float(row["Close"]),
                    "volume": int(row["Volume"]) if not pd.isna(row["Volume"]) else 0,
                }
            )
        return records
