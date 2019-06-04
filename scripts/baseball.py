# -*- coding: utf-8 -*-

###############################################################################
# "Baseball" example
###############################################################################
#  Objectives:
#   To understand how memory is managed by default by pandas, and how we can
#       optimize it.
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
#   https://www.geeksforgeeks.org/python-pandas-apply/
###############################################################################


###############################################################################
# Import required libraries
import pandas as pd
import numpy as np
import pickle
import pprintpp
import baseballAux as aux

GAME_LOGS_FILE = "../data/extracted/baseball/game_logs.csv"
DICT_SPECS_FILE = "../data/extracted/baseball/keysDict.pickle"


###############################################################################
# Loading the dataset
gl = pd.read_csv(GAME_LOGS_FILE)
gl.info(memory_usage='deep')
gl.head()

###############################################################################
# Exploring memory usage
for dtype in ['float', 'int', 'object']:
    selected_dtype = gl.select_dtypes(include=[dtype])
    mean_usage_b = selected_dtype.memory_usage(deep=True).mean()
    mean_usage_mb = mean_usage_b / 1024 ** 2
    print(
        "Average memory usage for {} columns: {:03.2f}MB".format(
            dtype, mean_usage_mb
        )
    )

###############################################################################
# Exploring types' memory footprint
int_types = ["uint8", "int8", "int16"]
for it in int_types:
    print(np.iinfo(it))
float_types = ["float16", "float32", "float64"]
for it in float_types:
    print(np.finfo(it))


gl_int = gl.select_dtypes(include=['int'])
converted_int = gl_int.apply(pd.to_numeric, downcast='unsigned')
print(aux.stringMemoryComparison(gl_int, converted_int))

gl_float = gl.select_dtypes(include=['float'])
converted_float = gl_float.apply(pd.to_numeric, downcast='float')
print(aux.stringMemoryComparison(gl_float, converted_float))

optimized_gl = gl.copy()
optimized_gl[converted_int.columns] = converted_int
optimized_gl[converted_float.columns] = converted_float
print(aux.stringMemoryComparison(gl, optimized_gl))

###############################################################################
# Optimizing using categoricals
gl_obj = gl.select_dtypes(include=['object']).copy()
gl_obj.describe()

dow = gl_obj.day_of_week
print(dow.head())

dow_cat = dow.astype('category')
print(dow_cat.head())

dow_cat.head().cat.codes
print(aux.stringMemoryComparison(dow, dow_cat))

###############################################################################
# Optimizing using categoricals throughout the dataframe
converted_obj = pd.DataFrame()
for col in gl_obj.columns:
    num_unique_values = len(gl_obj[col].unique())
    num_total_values = len(gl_obj[col])
    if num_unique_values / num_total_values < 0.5:
        converted_obj.loc[:, col] = gl_obj[col].astype('category')
    else:
        converted_obj.loc[:, col] = gl_obj[col]
print(aux.stringMemoryComparison(gl_obj, converted_obj))

converted_obj.head()
optimized_gl[converted_obj.columns] = converted_obj
print(aux.stringMemoryComparison(gl, optimized_gl))

###############################################################################
# Optimizing the date
date = optimized_gl.date
optimized_gl['date'] = pd.to_datetime(date, format='%Y%m%d')
print(aux.stringMemoryComparison(gl, optimized_gl))


###############################################################################
# Dump the dictionary of dataspecs for use in the next exercise
dtypes = optimized_gl.drop('date', axis=1).dtypes
dtypes_col = dtypes.index
dtypes_type = [i.name for i in dtypes.values]
column_types = dict(zip(dtypes_col, dtypes_type))
preview = first2pairs = {
    key: value for key, value in list(column_types.items())[:10]
}
pp = pprintpp.PrettyPrinter(indent=4)
pp.pprint(preview)
with open(DICT_SPECS_FILE, 'wb') as handle:
    pickle.dump(column_types, handle, protocol=pickle.HIGHEST_PROTOCOL)
