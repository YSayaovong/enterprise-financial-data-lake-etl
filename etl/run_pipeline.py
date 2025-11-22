import logging

from etl.pipelines.yahoo.extractor import YahooExtractor
from etl.pipelines.yahoo.transformer import YahooTransformer
from etl.pipelines.yahoo.loader import YahooLoader
from etl.db.models import init_db

logging.basicConfig(level=logging.INFO)


def run_yahoo_pipeline(symbol: str):
    extractor = YahooExtractor(symbol=symbol, period="5y", interval="1d")
    transformer = YahooTransformer(symbol=symbol)
    loader = YahooLoader()

    raw = extractor.extract()
    records = transformer.transform(raw)
    loader.load(records)


if __name__ == "__main__":
    logging.info("Initializing database and creating tables (if needed)...")
    init_db()

    symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA"]

    for s in symbols:
        logging.info("Running Yahoo Finance pipeline for %s", s)
        run_yahoo_pipeline(s)
