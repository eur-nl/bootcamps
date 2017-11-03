# -*- coding: utf-8 -*-
# PART 0 Import libraries, etc.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from sklearn import datasets, svm, cross_validation, tree, preprocessing, metrics
import sklearn.ensemble as ske
# PART 1 INTRODUCTION 
# Import the datafiles
df_train = pd.read_csv("~/Documents/bootcamps/data/titanic/train.csv", sep=",")
df_test = pd.read_csv("~/Documents/bootcamps/data/titanic/test.csv", sep=",")
# Have a quick look at the contents of the df_train dataframe
print(df_train.head())
# We 
survival_chance = df_train['Survived'].mean()
print(survival_chance) # 38% survival chance
# Since a lot of people (almost 62%) died, we can predict that in the test set
# The majority of people will not survive the disaster
# Of course our test file did not contain a column "Survived", because we were
# going to predict that from df_train
# S, we add that column, "Survived" to our test dataframe