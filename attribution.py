from db_utils import read_select, get_temptable,\
                     insert_temp_ret_table, drop_temp_table
from weights import get_portfolio_weights
from pandas import DataFrame

def load_constituent_prices(ticker, db):
    q = """
        SELECT *
        FROM eq_prices
        WHERE ticker = {_ticker}
    """
    p = {"_ticker": ticker}
    prices = read_select(db, q, p, in_df=True)
    return prices


def calc_daily_return(ticker, db):
    existing_returns = get_ticker_returns(ticker, db)
    if existing_returns.shape[0] > 0:
        print("returns already existing for {}".format(ticker))
        return
    # _ get prices
    prices = load_constituent_prices(ticker, db)
    if prices.shape[0] == 0:
        raise RuntimeError("no prices found for {}".format(ticker))

    # _ calculate returns
    prices.index = prices["price_date"]
    returns = prices["price"] / prices["price"].shift(1) - 1
    returns.dropna(inplace=True)

    # _ prepare returns df
    insert_df = DataFrame(returns)
    insert_df = insert_df.reset_index()
    insert_df.columns = ["return_date", "price_ret"]
    insert_df["price_ret"] = insert_df["price_ret"].astype(float)
    insert_df.loc[:, "ticker"] = ticker

    # _ insert returns and clean up
    temptbl = get_temptable()
    try:
        insert_df.to_sql(temptbl, db)
        insert_temp_ret_table(db, temptbl, "daily_constituent_returns")
    except:
        print("Error loading returns for {}".format(ticker))
    drop_temp_table(db, temptbl)


def calc_daily_constituent_returns(tickers, db):
    for ticker in tickers:
        calc_daily_return(ticker, db)


def calc_daily_portfolio_returns(portfolio_name, db):
    # _ get constituent weights
    weights = get_portfolio_weights(portfolio_name, db)

    # _ get constituent returns
    constituent_rets = get_portfolio_returns(portfolio_name, db)

    # _ calculate return contribution for each constituent

    # _ aggregate on the portfolio
    portfolio_returns = []
    return portfolio_returns


def get_ticker_returns(ticker, db):
    q = """
        SELECT * 
        FROM <TBL:daily_constituent_returns> 
        WHERE ticker = {_ticker}
    """
    p = {"_ticker": ticker}
    df = read_select(db, q, p)
    return df


def get_portfolio_returns(portfolio_name, db):
    q = """
        SELECT *
        FROM <TBL:portfolio_returns>
        where portfolio_name = {_portfolio_name}
    """
    p = {"_portfolio_name": portfolio_name}
    portfolio_returns = read_select(db, q, p)
    return portfolio_returns
