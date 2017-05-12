"""

"""
import numpy as np
import pandas as pd
from db_utils import get_postgres_engine
from attribution import get_portfolio_returns, get_ticker_returns
import visuals as vis
from templates.stress_test_rpt import render_report

STRESS_TEST_TEMPLATE = "./templates/stress_test_rpt.html"
STRESS_TEST_RPT_TARGET = "./reports/stress_test_rpt_output.html"

class StressTest:
    """
    """
    def __init__(self, portfolio, template_path=STRESS_TEST_TEMPLATE
                                , target_path=STRESS_TEST_RPT_TARGET):
        self.db = get_postgres_engine()
        self.pf = portfolio
        self.benchmark = portfolio.benchmark
        self.mkt_up_down = range(-15,20,5)
        self.scenario_ret = {}
        self.template_path = template_path
        self.target_path = target_path

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
            self.scenario_ret[event] = [scenario_ret]

        self.scenario_df = DataFrame(self.scenario_ret).T

    def gen_correlations(self, window_size=30):
        # rolling correlations
        self.rolling_corr = agg_df.dropna()\
                                  .rolling(window=window_size)\
                                  .corr(agg_df["pf_ret"], agg_df["bench_ret"])

    def gen_visuals(self):
        self.pos_breakdown_image_url = vis.pos_breakdown(self.pf.weights)
        self.cumulative_returns_image_url = vis.cumulative_returns(self.agg_df)
        self.scenario_returns_image_url = vis.scenario_returns(self.scenario_df, self.beta, self.benchmark.ticker)
        self.correlation_chart_image_url = vis.correlation_chart(self.rolling_corr)

    def render_report(self):
        opts = {
            "pos_breakdown_image_url": self.pos_breakdown_image_url,
            "cumulative_returns_image_url": self.cumulative_returns_image_url,
            "scenario_returns_image_url": self.scenario_returns_image_url,
            "correlation_chart_image_url": self.correlation_chart_image_url
        }
        render_report(self.template_path, self.target_path, opts)

    def run(self):
        self.run_stress_test()
        self.gen_correlations()
        self.gen_visuals()
        self.render_report()


def calc_cov_matrix(asset_ret, bench_ret):
    return np.cov(asset_ret, bench_ret)


def calc_asset_beta(asset_ret, bench_ret):
    cov_matrix = calc_cov_matrix(asset_ret, bench_ret)
    beta = cov_matrix[0, 1] / cov_matrix[1, 1]
    return beta