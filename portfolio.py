# -*- coding: utf-8 -*-
"""

Long/Short Equity Portfolio

"""

import pandas as pd
from db_utils import get_postgres_engine
from download import load_prices
from attribution import calc_daily_constituent_returns,\
                        calc_daily_portfolio_returns
from risk import stress_test

class Benchmark:
    def __init__(self, ticker):
        self.ticker
        self.load()

    def load(self):
        load_prices(self.ticker)
        calc_daily_constituent_returns(self.ticker)


class Portfolio:
    """
    """
    def __init__(self, portfolio_name, benchmark_name, weights_path):
        self.db = get_postgres_engine()
        self.weights_path = weights_path
        self.benchmark = Benchmark(benchmark_name)

    def load_weights(self):
        weights = pd.read_csv(self.weights_path)
        self.weights = weights
        self.constituents = weights.ticker.tolist()

    def load_prices(self):
        load_prices(self.constituents)

    def calc_returns(self):
        self.constituent_returns = calc_daily_constituent_returns(self.constituents)
        self.portfolio_returns = calc_daily_portfolio_returns(self.constituents, self.weights)

    def calc_portfolio_beta(self):
        pass

    def generate_report(self):
        stress_test()

    def run(self):
        self.load_weights()
        self.load_prices()
        self.calc_returns()
        self.calc_portfolio_beta()
