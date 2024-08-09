export interface Dividend_payment {
	year: string;
	type: string;
}

export interface XD {
	trade_date: string;
	reference_price: string;
	refill_finish_date: string;
	refill_cost_days: string;
	cash_dividend_payment: string;
}

export interface Cash_dividend {
	surplus: string;
	reserve: string;
	total: string;
}

export interface Stock_dividend {}

export interface Shareholder_dividend {
	cash_dividend: Cash_dividend;
	stock_dividend: Stock_dividend;
	total: string;
}

export interface Info {
	dividend_payment: Dividend_payment;
	XD: XD;
	XR: any;
	shareholder_dividends: Shareholder_dividend;
}

export interface StockData {
    name: string;
    info: Info[];
}


export interface Data {
	's0050': StockData;
	's00878': StockData;
}

export interface RootObject {
	data: Data;
}