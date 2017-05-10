"""

"""
import numpy as np
import pandas as pd
from db_utils import get_postgres_engine
from attribution import get_portfolio_returns, get_ticker_returns

# impleme
class StressTest:
    """
    """
    def __init__(self, portfolio, template_path, target_path):
        self.db = get_postgres_engine()
        self.pf = portfolio
        self.benchmark = portfolio.benchmark
        self.mkt_up_down = range(-15,20,5)
        self.scenario_ret = {}

    def get_pf_ret(self):
        # _ get portfolio returns
        pf_ret = get_portfolio_returns(self.pf.portfolio_name, db)
        self.pf_ret = pf_ret.price_ret

    def get_bench_ret(self):
        # _ get benchmark returns
        bench_ret = get_ticker_returns(self.benchmark.ticker, db)

    def merge_frames(self):
        agg_df = pd.concat([self.pf_ret, self.bench_ret], axis=1)
        agg_df.columns = ["pf_ret", "bench_ret"]
        self.agg_df = agg_df.dropna(inplace=True)

    def run_test(self, market_up_down, db):

        self.get_pf_ret()
        self.get_bench_ret()
        agg_df = self.merge_frames()

        # _ get covariance
        cov_matrix = np.cov(agg_df["pf_ret"], agg_df["bench_ret"])
        self.cov_matrix = cov_matrix

        # _ get beta
        beta = cov_matrix[0,1] / cov_matrix[1,1]
        self.beta = beta

        for event in self.mkt_up_down:
            scenario_ret = event * beta
            self.scenario_ret[event] = scenario_ret

    def gen_visuals(self):
        pass

    def render_report(self):
        pass


def calc_cov_matrix(asset_ret, bench_ret):
    return np.cov(asset_ret, bench_ret)


def calc_asset_beta(asset_ret, bench_ret):
    cov_matrix = calc_cov_matrix(asset_ret, bench_ret)
    beta = cov_matrix[0, 1] / cov_matrix[1, 1]
    return beta