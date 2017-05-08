"""

"""
import numpy as np
from db_utils import get_postgres_engine
from attribution import get_portfolio_returns, get_ticker_returns

# implement
class StressTest:
    def __init__(self, portfolio, benchmark, template_path, target_path):
        self.db = get_postgres_engine()
        self.pf = portfolio
        self.benchmark = benchmark
        self.mkt_up_down = range(-15,20,5)
        self.scenario_ret = {}

    def run_test(self, market_up_down, db):
        # _ get portfolio returns
        pf_ret = get_portfolio_returns(self.pf.portfolio_name, db)

        # _ get benchmark returns
        bench_ret = get_ticker_returns(self.benchmark.ticker, db)

        # _ get covariance
        cov_matrix = np.cov(pf_ret, bench_ret)

        # _ get beta
        beta = cov_matrix[0,1] / covmat[1,1]

        for event in self.mkt_up_down:
            scenario_ret = event * beta
            self.scenario_ret[event] = scenario_ret