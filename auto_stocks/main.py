from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import datetime
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/stock")
def read_root():
    # return {
    #     "data": {
    #         "s00878": {
    #             "name": "國泰永續高股息",
    #             "info": [
    #                 {
    #                     "dividend_payment": {"year": 2024, "type": "2024H1"},
    #                     "XD": {
    #                         "trade_date": datetime.datetime(2024, 1, 17, 0, 0),
    #                         "reference_price": 128.65,
    #                         "refill_finish_date": datetime.datetime(2024, 1, 19, 0, 0),
    #                         "refill_cost_days": 3,
    #                         "dividend_payment_date": datetime.datetime(2024, 2, 21, 0, 0),
    #                     },
    #                     "XR": {
    #                         "trade_date": None,
    #                         "reference_price": None,
    #                         "refill_finish_date": None,
    #                         "refill_cost_days": None,
    #                         "dividend_payment_date": None,
    #                     },
    #                     "shareholder_dividends": {
    #                         "cash_dividend": {"surplus": 3.0, "reserve": 0.0, "total": 3.0},
    #                         "stock_dividend": {"surplus": 0.0, "reserve": 0.0, "total": 0.0},
    #                         "total": 3.0,
    #                     },
    #                 },
    #                 {
    #                     "dividend_payment": {"year": 2023, "type": "2023H2"},
    #                     "XD": {
    #                         "trade_date": datetime.datetime(2023, 7, 18, 0, 0),
    #                         "reference_price": 130.1,
    #                         "refill_finish_date": datetime.datetime(2023, 11, 21, 0, 0),
    #                         "refill_cost_days": 87,
    #                         "dividend_payment_date": datetime.datetime(2023, 8, 11, 0, 0),
    #                     },
    #                     "XR": {
    #                         "trade_date": None,
    #                         "reference_price": None,
    #                         "refill_finish_date": None,
    #                         "refill_cost_days": None,
    #                         "dividend_payment_date": None,
    #                     },
    #                     "shareholder_dividends": {
    #                         "cash_dividend": {"surplus": 1.9, "reserve": 0.0, "total": 1.9},
    #                         "stock_dividend": {"surplus": 0.0, "reserve": 0.0, "total": 0.0},
    #                         "total": 1.9,
    #                     },
    #                 },
    #             ],
    #         },
    #         "s0050": {
    #             "name": "元大台灣50",
    #             "info": [
    #                 {
    #                     "dividend_payment": {"year": 2024, "type": "2024H1"},
    #                     "XD": {
    #                         "trade_date": datetime.datetime(2024, 1, 17, 0, 0),
    #                         "reference_price": 128.65,
    #                         "refill_finish_date": datetime.datetime(2024, 1, 19, 0, 0),
    #                         "refill_cost_days": 3,
    #                         "dividend_payment_date": datetime.datetime(2024, 2, 21, 0, 0),
    #                     },
    #                     "XR": {
    #                         "trade_date": None,
    #                         "reference_price": None,
    #                         "refill_finish_date": None,
    #                         "refill_cost_days": None,
    #                         "dividend_payment_date": None,
    #                     },
    #                     "shareholder_dividends": {
    #                         "cash_dividend": {"surplus": 3.0, "reserve": 0.0, "total": 3.0},
    #                         "stock_dividend": {"surplus": 0.0, "reserve": 0.0, "total": 0.0},
    #                         "total": 3.0,
    #                     },
    #                 },
    #                 {
    #                     "dividend_payment": {"year": 2023, "type": "2023H2"},
    #                     "XD": {
    #                         "trade_date": datetime.datetime(2023, 7, 18, 0, 0),
    #                         "reference_price": 130.1,
    #                         "refill_finish_date": datetime.datetime(2023, 11, 21, 0, 0),
    #                         "refill_cost_days": 87,
    #                         "dividend_payment_date": datetime.datetime(2023, 8, 11, 0, 0),
    #                     },
    #                     "XR": {
    #                         "trade_date": None,
    #                         "reference_price": None,
    #                         "refill_finish_date": None,
    #                         "refill_cost_days": None,
    #                         "dividend_payment_date": None,
    #                     },
    #                     "shareholder_dividends": {
    #                         "cash_dividend": {"surplus": 1.9, "reserve": 0.0, "total": 1.9},
    #                         "stock_dividend": {"surplus": 0.0, "reserve": 0.0, "total": 0.0},
    #                         "total": 1.9,
    #                     },
    #                 },
    #             ],
    #         },
    #     }
    # }
    return {
        "data": {
            "s00878": {
                "name": "國泰永續高股息",
                "info": [
                    {
                        "dividend_payment": {
                            "year": "2024",  # 發放股息年度
                            "type": "Q1",  # 發放股息形式(季配、月配等等)
                        },
                        "XD": {  # 除息
                            "trade_date": "'24/02/27",  #  除息交易日
                            "reference_price": "22.01",  #  除息參考價
                            "refill_finish_date": "'24/03/08",  #  除息填息日期(可能為空值)
                            "refill_cost_days": "8",  #  除息填息花費天數(可能為空值)
                            "cash_dividend_payment": "'24/03/25",  #  除息發放股息日期
                        },
                        "XR": {},  # 除權TODO
                        "shareholder_dividends": {  # 股東股利
                            "cash_dividend": {  # 現金股利
                                "surplus": "0.4",  # 現金股利-盈餘
                                "reserve": "0",  # 現金股利-公積
                                "total": "0.4",  # 現金股利-合計
                            },
                            "stock_dividend": {},  #  股票股利
                            "total": "0.4",  # 股利合計
                        },
                    },
                    {
                        "dividend_payment": {"year": "2023", "type": "Q4"},
                        "XD": {
                            "trade_date": "'23/11/16",
                            "reference_price": "20.34",
                            "refill_finish_date": "'23/11/21",
                            "refill_cost_days": "4",
                            "cash_dividend_payment": "'23/12/12",
                        },
                        "XR": {},
                        "shareholder_dividends": {
                            "cash_dividend": {
                                "surplus": "0.35",
                                "reserve": "0",
                                "total": "0.35",
                            },
                            "stock_dividend": {},
                            "total": "0.35",
                        },
                    },
                ],
            },
            "s0050": {
                "name": "元大台灣50",
                "info": [
                    {
                        "dividend_payment": {
                            "year": "2024",  # 發放股息年度
                            "type": "H1",  # 發放股息形式(季配、月配等等)
                        },
                        "XD": {  # 除息
                            "trade_date": "'24/01/17",  #  除息交易日
                            "reference_price": "128.65",  # 除息參考價
                            "refill_finish_date": "'24/01/19",  # 除息填息日期(可能為空值)
                            "refill_cost_days": "3",  # 除息填息花費天數(可能為空值)
                            "cash_dividend_payment": "'24/02/21",  # 除息發放股息日期
                        },
                        "XR": {},  # 除權TODO
                        "shareholder_dividends": {  # 股東股利
                            "cash_dividend": {  # 現金股利
                                "surplus": "3",  # 現金股利-盈餘
                                "reserve": "0",  # 現金股利-公積
                                "total": "3",  # 現金股利-合計
                            },
                            "stock_dividend": {},  #  股票股利
                            "total": "3",  # 股利合計
                        },
                    },
                    {
                        "dividend_payment": {
                            "year": "2023",
                            "type": "H2",
                        },
                        "XD": {
                            "trade_date": "'23/07/18",
                            "reference_price": "130.1",
                            "refill_finish_date": "'23/11/21",
                            "refill_cost_days": "87",
                            "cash_dividend_payment": "'23/08/11",
                        },
                        "XR": {},
                        "shareholder_dividends": {
                            "cash_dividend": {
                                "surplus": "1.9",
                                "reserve": "0",
                                "total": "1.9",
                            },
                            "stock_dividend": {},
                            "total": "1.9",
                        },
                    },
                ],
            },
        }
    }

@app.get("/tmp_stock/{stock_id}")
def read_root2(stock_id):
    if stock_id == '00878':
        return {
            "data": {
                "00878": {
                    "id":"00878",
                    "name": "國泰永續高股息",
                    "info": [
                        {
                            "dividend_payment": {
                                "year": "2024",  # 發放股息年度
                                "type": "Q1",  # 發放股息形式(季配、月配等等)
                            },
                            "XD": {  # 除息
                                "trade_date": "'24/02/27",  #  除息交易日
                                "reference_price": "22.01",  #  除息參考價
                                "refill_finish_date": "'24/03/08",  #  除息填息日期(可能為空值)
                                "refill_cost_days": "8",  #  除息填息花費天數(可能為空值)
                                "cash_dividend_payment": "'24/03/25",  #  除息發放股息日期
                            },
                            "XR": {},  # 除權TODO
                            "shareholder_dividends": {  # 股東股利
                                "cash_dividend": {  # 現金股利
                                    "surplus": "0.4",  # 現金股利-盈餘
                                    "reserve": "0",  # 現金股利-公積
                                    "total": "0.4",  # 現金股利-合計
                                },
                                "stock_dividend": {},  #  股票股利
                                "total": "0.4",  # 股利合計
                            },
                        },
                        {
                            "dividend_payment": {"year": "2023", "type": "Q4"},
                            "XD": {
                                "trade_date": "'23/11/16",
                                "reference_price": "20.34",
                                "refill_finish_date": "'23/11/21",
                                "refill_cost_days": "4",
                                "cash_dividend_payment": "'23/12/12",
                            },
                            "XR": {},
                            "shareholder_dividends": {
                                "cash_dividend": {
                                    "surplus": "0.35",
                                    "reserve": "0",
                                    "total": "0.35",
                                },
                                "stock_dividend": {},
                                "total": "0.35",
                            },
                        },
                    ],
                },
            }
        }
    elif stock_id == '0050':
        return {
            "data": {
                "0050": {
                    "id":"0050",
                    "name": "元大台灣50",
                    "info": [
                        {
                            "dividend_payment": {
                                "year": "2024",  # 發放股息年度
                                "type": "Q1",  # 發放股息形式(季配、月配等等)
                            },
                            "XD": {  # 除息
                                "trade_date": "'24/02/27",  #  除息交易日
                                "reference_price": "22.01",  #  除息參考價
                                "refill_finish_date": "'24/03/08",  #  除息填息日期(可能為空值)
                                "refill_cost_days": "8",  #  除息填息花費天數(可能為空值)
                                "cash_dividend_payment": "'24/03/25",  #  除息發放股息日期
                            },
                            "XR": {},  # 除權TODO
                            "shareholder_dividends": {  # 股東股利
                                "cash_dividend": {  # 現金股利
                                    "surplus": "0.4",  # 現金股利-盈餘
                                    "reserve": "0",  # 現金股利-公積
                                    "total": "0.4",  # 現金股利-合計
                                },
                                "stock_dividend": {},  #  股票股利
                                "total": "0.4",  # 股利合計
                            },
                        },
                        {
                            "dividend_payment": {"year": "2023", "type": "Q4"},
                            "XD": {
                                "trade_date": "'23/11/16",
                                "reference_price": "20.34",
                                "refill_finish_date": "'23/11/21",
                                "refill_cost_days": "4",
                                "cash_dividend_payment": "'23/12/12",
                            },
                            "XR": {},
                            "shareholder_dividends": {
                                "cash_dividend": {
                                    "surplus": "0.35",
                                    "reserve": "0",
                                    "total": "0.35",
                                },
                                "stock_dividend": {},
                                "total": "0.35",
                            },
                        },
                    ],
                },
            }
        }
        


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8080, reload=True)
# url: http://127.0.0.1:8080/stock

# 啟用server:
# python -m uvicorn main:app --reload
# uvicorn main:app --reload(正常指令)

# 關掉server:
# 點旁邊垃圾桶
# ctrl + C
