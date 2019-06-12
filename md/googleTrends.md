# dataPy: [Google Trends](https://trends.google.com/trends/?geo=US)

[Google Trends](https://trends.google.com/trends/) is a website dedicated to showcase and analyze the tendencies on google queries across the world and over time.

[<img src="./media/googleTrends.png" width="100%">](https://trends.google.com/trends/)


Unfortunately, no official API exists, so there is no built-in support to parsing and doing analysis over these data. This, however, is a minor limitation, as there are some alternatives in [python](https://www.python.org/), such as [pytrends](https://github.com/GeneralMills/pytrends).


##  [PyTrends](https://github.com/GeneralMills/pytrends)

This package is an unofficial [google Trends](https://trends.google.com/trends/) parser, maintained by a community of contributors. It is simple, yet sufficient for most applications.

[<img src="./media/pytrends.png" width="75%">](https://github.com/GeneralMills/pytrends)

### [Exercise 1: Using pytrends](../scripts/pyTrendsDemo.py)

This exercise is an introduction on how to use google trends with the pytrends python package. With it, we will learn how to make requests to the google trends server, and plot their frequencies using matplotlib.

<img src="./media/blockchain.jpg" width="50%">

### [Exercise 2: "How to Breakup"](../scripts/breakup.py)

In this second exercise, we will see how we can extract more "knowledge" on a google trends series by restricting time samples, and ploting at different timescales.

<img src="./media/break.jpg" width="50%">

### [Exercise 3: "CRISPR"](../scripts/trendsCRISPR.py)

The final google trends exercise will show us how to clean and merge dataframes so that we can compare search queries about CRISPR across three geographic scales.

<img src="./media/crispr.png" width="50%">

<hr>

## Other Resources

* https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
