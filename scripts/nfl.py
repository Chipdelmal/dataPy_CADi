###############################################################################
# "NFL"
###############################################################################
#  Objectives:
#
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


%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import pandas as pd
import numpy as np
from matplotlib import cm
import seaborn as sns

data = pd.read_csv("../data/extracted/NFL/NFL.csv")
data.head()
list(data.columns)

ageFilterValue = 30
ageFilter = data["Age"] > ageFilterValue
aboveAge = data[ageFilter]
len(aboveAge)

data["Current Status"].unique()
activeFilter = data["Current Status"] == "Active"

aboveAndActive = data[ageFilter & activeFilter]
len(aboveAndActive)

frequencies = aboveAndActive["Position"].value_counts()
frequencies.plot.bar(title=("Active players above  " + str(ageFilterValue) + "grouped by position"))


color = cm.inferno_r(np.linspace(.4,.8, 30))
frequencies.plot(kind="bar", title=("Active NFL players above " + str(ageFilterValue) + "y grouped by position"), color=color)
plt.savefig('./images/nflBar.png',dpi=500)



sns.lmplot(
    x="Height (inches)", y="Weight (lbs)", data=aboveAndActive,
    aspect=1.5, fit_reg=False, hue='Position', legend=True,
    palette=sns.color_palette("hls", len(aboveAndActive["Position"].unique()))
)
plt.savefig('./images/nflScatter.png',dpi=500)
