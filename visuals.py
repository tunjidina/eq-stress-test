import os
import seaborn as sns
import matplotlib.pyplot as plt


def pos_breakdown(weight_df, path="./images/pos_breakdown.png"):
    f, (ax1, ax2) = plt.subplots(1, 2)
    weight_df[weight_df.weight > 0]["weight"].sort_values() \
        .plot(kind="pie",
              figsize=(35, 17.5),
              autopct='%.2f',
              ax=ax1,
              colors=sns.color_palette("Blues"),
              fontsize=20)
    ax1.set_title("Longs", fontsize=40)
    (weight_df[weight_df.weight < 0] * -1)["weight"].sort_values() \
        .plot(kind="pie",
              figsize=(35, 17.5),
              autopct='(%.2f)', ax=ax2,
              colors=sns.color_palette("Blues"),
              fontsize=20)
    ax2.set_title("Shorts", fontsize=40)
    f.savefig(path)

    # _ send only the filename
    filename = os.path.basename(path)
    return filename


def cumulative_returns(agg_df, path="./images/cum_returns.png"):
    total_ret = agg_df.cumsum().dropna()

    f, ax = plt.subplots()
    total_ret.plot(figsize=(20, 10), ax=ax)

    ax.set_title("Portfolio vs Benchmark Returns (cumulative)")
    ax.set_ylabel("Returns")

    f.savefig(path)

    # _ send only the filename
    filename = os.path.basename(path)
    return filename


def scenario_returns(scenario_returns_df, pf_beta, bench_name, path="./images/scenario_returns.png"):
    f, ax = plt.subplots()
    scenario_returns_df.plot(kind="bar", figsize=(20, 10), ax=ax)
    ax.set_title('Stress Scenario returns for Mock Portfolio (pf beta: {:.2f} vs SP500)'.format(pf_beta))
    ax.set_xlabel("Scenarios (pct up/down)")
    ax.set_ylabel("Returns")
    f.savefig(path)

    # _ send only the filename
    filename = os.path.basename(path)
    return filename


def correlation_chart(cor_df, path="./images/rolling_corr.png"):
    f, ax = plt.subplots()
    cor_df.plot(ax=ax, figsize=(20, 10))
    ax.set_title("30-day rolling correlation portfolio vs SP500")
    ax.set_ylabel("Correlation")
    f.savefig(path)

    # _ send only the filename
    filename = os.path.basename(path)
    return filename

