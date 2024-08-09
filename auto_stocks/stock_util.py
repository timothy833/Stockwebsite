import enum


class StockTerminology(enum.Enum):
    # trade_date='除息交易日'
    TRADE_DATE = "除息交易日"
    REFERENCE_PRICE = "除息參考價"
    REFILL_FINISH_DATE = "填息完成日"
    REFILL_COST_DAYS = "填息花費日數"
    CASH_DIVIDEND_PAYMENT = "現金股利發放日"
    DIVIDEND_PAYMENT_YEAR = "股利發放年度"
    DIVIDEND_PAYMENT_TYPE = "股利所屬盈餘期間"
    CASH_DIVIDENDS_SURPLUS = "現金股利盈餘"
    CASH_DIVIDENDS_RESERVE = "現金股利公積"
    CASH_DIVIDENDS_TOTAL = "現金股利合計"
    STOCK_DIVIDENDS_SURPLUS = "股票股利盈餘"
    STOCK_DIVIDENDS_RESERVE = "股票股利公積"
    STOCK_DIVIDENDS_TOTAL = "股票股利合計"
    ALL_DIVIDENDS_TOTAL = "股利合計股利合計"

    def __str__(self):
        return self.name.lower()

    @property
    def lower_name(self):
        return self.name.lower()
