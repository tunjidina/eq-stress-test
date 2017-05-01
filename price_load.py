import os
import glob
import time
from datetime import datetime

import pandas as pd
import pandas_datareader as pdr

FIVE_MINUTES = 60 * 5

class PriceLoad:
  
  def __init__(self):
    self.start_date = datetime(2010,1,1)
    self.end_date = datetime.today()
    self.root_ticker_path = '/Users/frank/Desktop/job search/2017/april/artisan partners/dev'
    self.price_files_path = os.path.join(self.root_ticker_path, "prices")
    self.all_tickers = self.load_manifest()

  def load_manifest(self):
    print("Loading ticker manifest")
    with open(os.path.join(self.root_ticker_path, "tickers"), "r") as ticker_file:
      all_tickers = ticker_file.readlines()
    all_tickers = [i.strip() for i in all_tickers]
    return all_tickers

  def get_ticker_universe(self):
    print("Looking for exsiting tickers")
    self.existing_tickers = glob.glob(os.path.join(self.root_ticker_path, "prices", "*"))
    self.existing_tickers = [os.path.split(i)[1].replace(".xlsx", "") for i in self.existing_tickers]
    self.tickers_to_load = [i for i in self.all_tickers if i not in self.existing_tickers]


  def load_ticker(self, ticker, loader_type="yahoo", rejected=False):
    _now = datetime.today().strftime("%H:%m:%S")
    # _ try to get the prices
    if loader_type == "yahoo":
      print("Attempting to get prices from yahoo for {} at {}".format(ticker, _now))
      try:
        cur_prices = pdr.get_data_yahoo(symbols=ticker,
                                    start=self.start_date,
                                    end=datetime.today())
      except:
        # _ if error try to sleep and try again
        if rejected:
          print("About to sleep for {} mins until yahoo allows scraping again".format(FIVE_MINUTES / 60))
          time.sleep(FIVE_MINUTES)
          self.load_ticker(ticker)
        else:
          self.load_ticker(ticker, "google")
    else:
      print("Attempting to get prices from google for {} at {}".format(ticker, _now))
      try:
        cur_prices = pdr.get_data_google(symbols=ticker,
                                    start=self.start_date,
                                    end=datetime.today())
      except:
        print("Rejected from GOOG")
        self.load_ticker(ticker, rejected=True)
    
    # _ if successful save the file 
    try:
      filename = os.path.join(self.price_files_path, ticker + ".xlsx")
      cur_prices.to_excel(filename)
      print("Prices for ticker: {} is saved".format(ticker))
    except:
      print("Trouble saving prices for ticker: {}".format(ticker))
    # _ pop ticker from tickers to load

  def load_prices(self):
    print("Starting to load prices: {}".format(datetime.today().strftime("%H:%m:%S")))
    for ticker in self.tickers_to_load:
      self.load_ticker(ticker)

  def run(self):
    self.get_ticker_universe()
    self.load_prices()


def run():
  p = PriceLoad()
  p.run()
  # get the list of ticker to load prices for
  # _ find out what's left to load
  # _ load

if __name__ == "__main__":
  run()
