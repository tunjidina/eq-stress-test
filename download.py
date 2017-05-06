"""
Download yahoo or google prices
"""
import os
import pandas_datareader as pdr
from datetime import datetime
from dateutil.relativedelta import relativedelta

from db_utils import get_engine
from db_utils import get_temptable, drop_temp_table,\
                     insert_temp_price_table

TODAY = datetime.today()
TEN_YRS = relativedelta(years=10)
TEN_YRS_AGO = TODAY - TEN_YRS


def download_yahoo_prices(ticker, start_date=TEN_YRS_AGO, end_date=TODAY):
    """
    
    :param ticker: Ticker to download prices for 
    :param start_date: Historical price start dare
    :param end_date: Historical price end date
    :return: Price df or None
    """
    try:
        prices = pdr.get_data_yahoo(symbols=ticker,
                                    start=start_date,
                                    end=end_date)
    except:
        print("Error occured downloading prices for {}".format(ticker))
        return None
    prices.loc[:, "price_date"] = prices["Date"]
    prices.loc[:, "price"] = prices["Adj Close"]
    prices.loc[:, "ticker"] = ticker
    prices.loc[:, "source"] = "yahoo"
    return prices


def insert_prices_to_db(db_engine, price_df, ticker):
    """
    Insert into temp db
    Insert into price db
    Cleanup temp table
    :param db_engine: SQLAlchemy engine 
    :param price_df: 
    :param ticker: str
    :param tablename: str
    :return: 
    """
    temptbl = get_temptable()
    price_db_cols = ["price_date", "ticker", "source", "price"]
    df_to_insert = price_df[price_db_cols]
    try:
        df_to_insert.to_sql(temptbl, db_engine)
    except:
        print("Error loading in prices for {}".format(ticker))

    insert_temp_price_table(db, temptbl, "eq_prices", debug=True)
    drop_temp_table(db, temptbl, debug=True)


def load_prices(db, tickers):
    """
    Download prices and load to tbd
    :param db: 
    :param tickers: 
    :return: 
    """
    for ticker in tickers:
        cur_prices = download_yahoo_prices(ticker)
        insert_prices_to_db(db, cur_prices, ticker)
