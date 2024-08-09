import requests
import pandas as pd
from pandas import DataFrame
from bs4 import BeautifulSoup
import typing as T
import dataclasses
import stock_util as util
from stock_util import StockTerminology
import time
import datetime

# class PaymentType(enum.Enum) # TODO: 全年配/半年配/季配/月配


@dataclasses.dataclass  # TODO:除權息資料架構
class EXDividendRight:
    trade_date: datetime
    reference_price: float
    refill_finish_date: datetime
    refill_cost_days: str
    cash_dividend_payment: datetime


# class MainManager:
#     def __init__():
#         self._db_manager
#         self._stock_manager
#         self._成分股

# data_frame = self._stock_manager.get_stock_dividend_info('00878')
# self._db_manager.DividendsToDB(dbdata_frame)

# class DBManager:

#     def DividendsToDB

# class 成分股:


class StockDividendManager:
    def __init__(self) -> None:
        pass

    def get_all_stock_dividends_info(self, stock_ids: list[str]) -> None:
        for id in stock_ids:
            self.get_stock_dividend_info(id)
            time.sleep(20)

    def get_stock_dividend_info(self, stock_id: str) -> None:
        df_res = self.send_request_to_goodinfo(stock_id)
        df_res = df_res.rename(columns=lambda x: x.replace(" ", "").replace("\xa0", ""))
        ex_dividends_date_node = self.get_ex_dividends_date_dataframe(df_res)
        payment_year_node = self.get_payment_year_dataframe(df_res)
        shareholders_dividend_node = self.get_shareholders_dividend_dataframe(df_res)
        total_node = pd.concat(
            [ex_dividends_date_node, payment_year_node, shareholders_dividend_node],
            axis=1,
        )
        total_node.rename(
            columns={data.value: data.lower_name for data in StockTerminology},
            inplace=True,
        )
        print(total_node)
        print("-" * 20)
        print(total_node.to_dict("records"))
        # {'除息交易日': "'24/01/17", -> trade_date (datetime type )
        #  '除息參考價': '128.65',  -> reference_price
        #  '填息完成日': "'24/01/19",  -> refill_finish_date
        #  '填息花費日數': '3',  -> refill_cost_days
        #  '現金股利發放日': "'24/02/21", ->cash_dividend_payment
        #  '股利發放年度': '2024', dividend_payment_year
        #  '股利所屬盈餘期間': '2024上半年', dividend_payment_type
        #  '現金股利盈餘': '3', -> cash_dividend_surplus
        #  '現金股利公積': '0', -> cash_dividend_reserve
        #  '現金股利合計': '3'} -> cash_dividend_total

    def send_request_to_goodinfo(self, stock_id: str) -> DataFrame:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }
        res = requests.get(
            f"https://goodinfo.tw/tw/StockDividendSchedule.asp?STOCK_ID={stock_id}",
            headers=headers,
        )
        res.encoding = "utf-8"
        bs = BeautifulSoup(res.text, "html.parser")
        data = bs.select_one("#tblDetail")
        if data is None:
            raise RuntimeError()
        dfs = pd.read_html(data.prettify())
        return dfs[0]

    def get_ex_dividends_date_dataframe(self, source_node: DataFrame) -> DataFrame:
        print("-" * 10 + "除息日程" + "-" * 10)
        result_node = source_node[["除息日程"]]
        result_node.columns = result_node.columns.get_level_values(1)
        print(result_node.to_dict("records"))
        return result_node

    # {'除息交易日': "'24/01/17",
    #  '除息參考價': '128.65',
    #  '填息完成日': "'24/01/19",
    #  '填息花費日數': '3',
    #  '現金股利發放日': "'24/02/21"}

    def get_payment_year_dataframe(self, source_node: DataFrame) -> DataFrame:
        print("-" * 10 + "股利發放年度" + "-" * 10)
        result_node = source_node[["股利發放年度", "股利所屬盈餘期間"]]
        result_node.columns = result_node.columns.get_level_values(2)
        print(result_node.to_dict("records"))
        return result_node

    # {'股利發放年度': '2024',
    #  '股利所屬盈餘期間': '2024上半年'}

    def get_shareholders_dividend_dataframe(self, source_node: DataFrame) -> DataFrame:
        print("-" * 10 + "現金股利" + "-" * 10)
        result_node = source_node["股東股利(元/股)"]
        result_node.columns = ["".join(col) for col in result_node.columns.values]
        print(DataFrame(result_node).to_dict("records"))
        return DataFrame(result_node)

    # {'盈餘': '3',
    #  '公積': '0',
    #  '合計': '3'}


if __name__ == "__main__":
    stock_dividend_manager = StockDividendManager()
    stock_dividend_manager.get_stock_dividend_info("0050")
