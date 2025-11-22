from sqlalchemy.orm import Session

from etl.core.base_loader import BaseLoader
from etl.db.models import SessionLocal, Instrument, DailyPrice


class YahooLoader(BaseLoader):
    def __init__(self):
        self.db: Session = SessionLocal()

    def load(self, records):
        if not records:
            return

        symbol = records[0]["symbol"]

        instrument = (
            self.db.query(Instrument).filter_by(symbol=symbol).one_or_none()
        )
        if instrument is None:
            instrument = Instrument(
                symbol=symbol,
                name=symbol,
                type="equity",
                currency="USD",
            )
            self.db.add(instrument)
            self.db.commit()
            self.db.refresh(instrument)

        for r in records:
            existing = (
                self.db.query(DailyPrice)
                .filter_by(instrument_id=instrument.id, date=r["date"])
                .one_or_none()
            )
            if existing:
                continue

            dp = DailyPrice(
                instrument_id=instrument.id,
                date=r["date"],
                open=r["open"],
                high=r["high"],
                low=r["low"],
                close=r["close"],
                volume=r["volume"],
            )
            self.db.add(dp)

        self.db.commit()
