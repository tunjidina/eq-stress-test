# eq-stress-test
Long/Short Equity Portfolio Stress Test

This project will read the weights file for constituents, download historical prices and calculate portfolio and benchmark returns.

Once daily return series are obtained, [portfolio beta](http://www.investopedia.com/terms/b/beta.asp) will be used for stress testing.

Results are currently outputted to a styled webpage which is then converted to a pdf (yes, majority of the investment managers are still relying on pdf)
 
Dependencies:

`pip install -r requirements.txt`

Download `wkhtmltopdf` from https://wkhtmltopdf.org/downloads.html