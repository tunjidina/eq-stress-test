from argparse import ArgumentParser
from returns import Portfolio, StressTest

def parse_args():
    """
    Cmd-line argument parser
    :return: args
    """
    parser = ArgumentParser()
    parser.add_argument("--portfolio_name", default="TEST_PF")
    parser.add_argument("--weights_file", default="./weights.csv")
    parser.add_argument("--report_template_path", default="./template/report_template.html")
    parser.add_argument("--report_target_path", default="./report/report.pdf")
    args = parser.parse_args()
    return args

def run_stress_test():
    args = parse_args()

    weights_path = args.weights_file
    portfolio_name = args.portfolio_name

    pf = Portfolio(portfolio_name, weights_path)

    pf.calc_returns()
    pf.calc_benchmark_returns()
    pf.calc_beta()

    template_path = args.template_path
    target_path = args.report_target_path

    rpt = StressTest(pf, template_path, target_path)
    rpt.run()

if __name__ == "__main__":
    run_stress_test()