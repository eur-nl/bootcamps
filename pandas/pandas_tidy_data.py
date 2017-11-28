#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:45:43 2017

@author: peter
"""
import pandas as pd

df = pd.read_csv("../data/cash.csv")

"""
If we run df on the commandline we get an overview of the (already) tidy
data:
    
- columns are variables and contain values
- rows are observations (sometimes called records)
- datapoints are or observational units are values: date, string for a name,
  amount

Tidy data is in the long format and often values will be repeated, because
we concentrate on "one observation per row.
"""

"""
How do things get messy?

- Life is messy, so many datasets out there are simply messy. Estimates about
  the amount of time spend by data scientists on cleaning data vary wildly
  but somewhere between 50 and 80% seems realistic *and* that is time spend
  when you *have* the data. Often getting the data is an equally big hurdle.
  
- Often data are made messy for presentation purposes.
"""

"""
An example of a messy dataset:
"""

df_treatment = pd.read_csv("../data/treatment_messy.csv")

"""
- We have an unnamed column with values of observations
- We have values as headers of columns
"""

# Let's tidy things up!
# First we add a column name for personal names, using our preferred editor
df_treatment_tidy = pd.melt(df_treatment,
                            ["Name"],
                            var_name = "Treatment",
                            value_name = "Result")
