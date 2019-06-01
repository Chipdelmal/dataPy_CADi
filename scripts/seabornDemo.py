# -*- coding: utf-8 -*-

###############################################################################
# "seaborn" example
###############################################################################
#  Objectives:
#   Test the analysis and presentation of relationships between variables
#       in seaborn
#  Source:
#   https://seaborn.pydata.org/tutorial/relational.html
###############################################################################

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Import required libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
%matplotlib inline
sns.set(style="darkgrid")

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Load and examine the dataset
tips = sns.load_dataset("tips")
tips.head()
list(tips.columns.values)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Plot correlations
sns.relplot(
    x="total_bill", y="tip", data=tips
)
sns.relplot(
    x="total_bill", y="tip", hue="smoker", data=tips
)
sns.relplot(
    x="total_bill", y="tip", hue="smoker", style="time", data=tips
)
sns.relplot(
    x="total_bill", y="tip", hue="size", data=tips
)
sns.relplot(
    x="total_bill", y="tip", size="size", hue="size",
    palette="ch:r=-.5,l=.75", data=tips
)
sns.relplot(
    x="total_bill", y="tip", size="size", hue="size",
    palette="ch:r=-.5,l=.85", alpha=.65, sizes=(15, 200), data=tips
)
