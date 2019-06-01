# -*- coding: utf-8 -*-

###############################################################################
# "Baseball" example
###############################################################################
#  Objectives:
#  Source:
#   https://www.dataquest.io/blog/pandas-big-data/
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Import required libraries
%matplotlib inline
import pandas as pd

#
gl = pd.read_csv("../data/extracted/baseball/game_logs.csv")
gl.info(memory_usage='deep')
