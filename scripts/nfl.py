# -*- coding: utf-8 -*-

###############################################################################
# "NFL"
###############################################################################
#  Objectives:
#   To learn the basics of data imporing, filtering and ploting in pandas
#       matplotlib and seaborn
#  Source:
#   https://www.kaggle.com/kendallgillies/nflstatistics
#   https://deadspin.com/chart-the-height-and-weight-of-every-nfl-player-by-po-1445608274
###############################################################################
# Instructions and other information
# -----------------------------------------------------------------------------
#   https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
#   https://stackoverflow.com/questions/11927715/how-to-give-a-pandas-matplotlib-bar-graph-custom-colors
#   https://stackoverflow.com/questions/18926031/how-to-extract-a-subset-of-a-colormap-as-a-new-colormap-in-matplotlib
#   https://seaborn.pydata.org/tutorial/color_palettes.html
###############################################################################

# Import the required libraries
import seaborn as sns
from matplotlib import cm
import numpy as np
import pandas as pd
import matplotlib.colors as colors
import matplotlib.pyplot as plt


help(pd.read_csv)
help(pd.read_excel)

# Load the dataset
data = pd.read_csv("../data/extracted/NFL/NFL.csv", sep=",")
data.head(5)
list(data.columns)

# Filtering and Selecting
ageFilterValue = 20
ageFilter = (data["Age"] > ageFilterValue) & (data["Current Status"] == "Active")
aboveAge = data[ageFilter]
len(aboveAge)
aboveAge.head()


type(list(data["Current Status"].unique())[0])
activeFilter = data["Current Status"] == "Active"

aboveAndActive = data[ageFilter & activeFilter]
len(aboveAndActive)

# Plotting
frequencies = aboveAndActive["Position"].value_counts()
frequencies.plot.bar(
    title=(
        f"Active players above  {ageFilterValue} grouped by position"
    )
)

# Plotting with style
color = cm.inferno_r(np.linspace(.4, .8, 30))
frequencies.plot(
    kind="bar",
    title=(
        f"Active NFL players above {ageFilterValue} grouped by position"
    ),
    color=color
)
plt.savefig('./images/nflBar.png', dpi=500)
plt.close()

# Scatter plot
sns.lmplot(
    x="Height (inches)", y="Weight (lbs)", data=aboveAndActive,
    aspect=1.5, fit_reg=False, hue='Position', legend=True,
    palette=sns.color_palette("hls", len(aboveAndActive["Position"].unique()))
)
plt.savefig('./images/nflScatter.png', dpi=500)
