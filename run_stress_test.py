from argparse import ArgumentParser
from returns import Portfolio, StressTest

def parse_args():
    """
    Cmd-line argument parser
    :return: args
    """
    parser = ArgumentParser()
    parser.add_argument("--weights_file")
    parser.add_argument("--lookback_years")
    parser.add_argument("--report_template_path")
    parser.add_argument("--report_target_path")
    parser.add_argument("--db_con_string")
    args = parser.parse_args()
    return args

def run_stress_test():
    args = parse_args()

    weights_path = args.weights_file
    history = args.lookback_years
    # _ in memory db will be used if no db available
    sql_alchemy_con_str = args.db_con_string

    pf = Portfolio(weights_path, history, sql_alchemy_con_str)

    pf.calc_returns()
    pf.calc_benchmark_returns()
    pf.calc_beta()

    template_path = args.template_path
    target_path = args.report_target_path

    rpt = StressTest(pf, template_path, target_path)
    rpt.run()

if __name__ == "__main__":
    run_stress_test()