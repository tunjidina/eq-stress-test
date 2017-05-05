# eq-stress-test
Long/Short Equity Portfolio Stress Test

This project will read the weights file for constituents (.csv), download historical prices (store them in a [SQLAlchemy Core](http://docs.sqlalchemy.org/en/latest/core/engines.html) powered db) and calculate portfolio and benchmark returns.

Once daily return series are obtained, a [portfolio beta](http://www.investopedia.com/terms/b/beta.asp) is calculated and used for stress testing.

Results are currently outputted to a styled webpage which is then converted to a pdf.

-----

#### Dependencies:

`pip install -r requirements.txt`

Download `wkhtmltopdf` from https://wkhtmltopdf.org/downloads.html