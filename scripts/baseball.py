# -*- coding: utf-8 -*-

###############################################################################
# "Baseball" example
###############################################################################
#  Objectives:
#  Source:
#   https://www.dataquest.io/blog/pandas-big-data/
#   https://towardsdatascience.com/why-and-how-to-use-pandas-with-large-data-9594dda2ea4c
#   https://data.world/dataquest/mlb-game-logs/workspace/data-dictionary
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.select_dtypes.html
#   https://docs.scipy.org/doc/numpy/reference/generated/numpy.iinfo.html
#   https://docs.scipy.org/doc/numpy/reference/generated/numpy.finfo.html
#   https://www.programiz.com/python-programming/methods/built-in/isinstance
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_numeric.html
#   https://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Import required libraries
import pandas as pd
import numpy as np
%matplotlib inline


###############################################################################
# Loading the dataset
gl = pd.read_csv("../data/extracted/baseball/game_logs.csv")
gl.info(memory_usage='deep')
gl.head()

###############################################################################
# Exploring memory usage
for dtype in ['float', 'int', 'object']:
    selected_dtype = gl.select_dtypes(include=[dtype])
    mean_usage_b = selected_dtype.memory_usage(deep=True).mean()
    mean_usage_mb = mean_usage_b / 1024 ** 2
    print("Average memory usage for {} columns: {:03.2f}MB".format(
        dtype, mean_usage_mb))


int_types = ["uint8", "int8", "int16"]
for it in int_types:
    print(np.iinfo(it))


float_types = ["float16", "float32", "float64"]
for it in float_types:
    print(np.finfo(it))


###############################################################################
# Downcasting numeric types
def mem_usage(pandas_obj):
    if isinstance(pandas_obj, pd.DataFrame):
        usage_b = pandas_obj.memory_usage(deep=True).sum()
    else:  # we assume if not a df it's a series
        usage_b = pandas_obj.memory_usage(deep=True)
    usage_mb = usage_b / 1024 ** 2  # convert bytes to megabytes
    return "{:03.2f} MB".format(usage_mb)


gl_int = gl.select_dtypes(include=['int'])
converted_int = gl_int.apply(pd.to_numeric, downcast='unsigned')
print(mem_usage(gl_int))
print(mem_usage(converted_int))
compare_ints = pd.concat([gl_int.dtypes, converted_int.dtypes], axis=1)
compare_ints.columns = ['before', 'after']
compare_ints.apply(pd.Series.value_counts)


gl_float = gl.select_dtypes(include=['float'])
converted_float = gl_float.apply(pd.to_numeric,downcast='float')
print(mem_usage(gl_float))
print(mem_usage(converted_float))
compare_floats = pd.concat([gl_float.dtypes,converted_float.dtypes],axis=1)
compare_floats.columns = ['before','after']
compare_floats.apply(pd.Series.value_counts)


optimized_gl = gl.copy()
optimized_gl[converted_int.columns] = converted_int
optimized_gl[converted_float.columns] = converted_float
print(mem_usage(gl))
print(mem_usage(optimized_gl))


###############################################################################
# Optimizing using categoricals
gl_obj = gl.select_dtypes(include=['object']).copy()
gl_obj.describe()

dow = gl_obj.day_of_week
print(dow.head())
dow_cat = dow.astype('category')
print(dow_cat.head())

dow_cat.head().cat.codes

print(mem_usage(dow))
print(mem_usage(dow_cat))


converted_obj = pd.DataFrame()
for col in gl_obj.columns:
    num_unique_values = len(gl_obj[col].unique())
    num_total_values = len(gl_obj[col])
    if num_unique_values / num_total_values < 0.5:
        converted_obj.loc[:,col] = gl_obj[col].astype('category')
    else:
        converted_obj.loc[:,col] = gl_obj[col]

print(mem_usage(gl_obj))
print(mem_usage(converted_obj))
compare_obj = pd.concat([gl_obj.dtypes,converted_obj.dtypes],axis=1)
compare_obj.columns = ['before','after']
compare_obj.apply(pd.Series.value_counts)


optimized_gl[converted_obj.columns] = converted_obj
mem_usage(optimized_gl)


optimized_gl[converted_obj.columns] = converted_obj
mem_usage(optimized_gl)

date = optimized_gl.date
print(mem_usage(date))
date.head()
