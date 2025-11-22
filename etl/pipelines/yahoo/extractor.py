import logging
import yfinance as yf

from etl.core.base_extractor import BaseExtractor


class YahooExtractor(BaseExtractor):
    def __init__(self, symbol: str, period: str = "5y", interval: str = "1d"):
        self.symbol = symbol
        self.period = period
        self.interval = interval

    def extract(self):
        logging.info("YahooExtractor: fetching %s history (%s, %s)", self.symbol, self.period, self.interval)
        ticker = yf.Ticker(self.symbol)
        df = ticker.history(period=self.period, interval=self.interval, auto_adjust=False)

        # df.index is DatetimeIndex; we want it as a column
        if df.empty:
            logging.warning("YahooExtractor: no data returned for %s", self.symbol)
            return df

        df = df.reset_index()  # Date becomes a column named 'Date'
        return df
