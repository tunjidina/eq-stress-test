# eq-stress-test
Long/Short Equity Portfolio Stress Test

This project will read the weights file for constituents (.csv), download historical prices (store them in a [SQLAlchemy Core](http://docs.sqlalchemy.org/en/latest/core/engines.html) powered db) and calculate portfolio and benchmark returns.

Once daily return series are obtained, a [portfolio beta](http://www.investopedia.com/terms/b/beta.asp) is calculated and used for stress testing.

Results are currently outputted to a styled webpage which is then converted to a pdf.

-----

#### Dependencies:

Visuals generated as part of the report depend on matplotlib. Getting matplotlib working in virtual environments is tricky see [Working with Matplotlib in Virtual Environments](http://matplotlib.org/faq/virtualenv_faq.html).

Therefore we are just going to use conda to create the environment.

`conda create -n eq-stress python=3.5.2 matplotlib`

Then install the remaining requirements

`pip install -r requirements.txt`

----

#### How to run

`python run_stress_test.py --weights_file your_weights_file.csv`

Your `weights.csv` should look like this

```
ticker,weight
ticker1,.8
ticker2,.2
```