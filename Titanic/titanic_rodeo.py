"""
### Titanic
There are several contexts here:
- That of Jupyter notebooks. Kind of a playground. Especially suited for trying
things out *and* documenting what you did. In the area of data science one is
able to bring data, manipulations (code!) and results (visualizations) together
in a kind of labbook or scientific journal.
- The possibilities of (big) data, the computer, and economic and econometric
research: Statistical learning (= machine learning?).
- And of course the disaster of the Titanic itself. We are mainly going to work
with data about passengers, but there are other ways looking at the disaster,
like for example the reconstruction, a computer generated simulation, of the
actual sinking by James Cameron:

<a href="https://www.youtube.com/watch?v=FSGeskFzE0s">James Cameron: How the Titanic sank</a>

"""

"""
### The Titanic: What do we know already?
You probably all have seen the movie Titanic by James Cameron (Kate Winslet and
Leonardo DiCaprio, 1997) which is one of several movies made of the disaster. So,
you probably know the following:
- The disaster took place during the night of April, 14, 1912 when the ship hit
an iceberg on her maiden voyage from Southampton (UK) to New York (US) via
Cherbourg (FR) and Queenstown (IRE).
- The loss of lives was 1501 out of a total 2207 passengers and crew.
- The was a shortage of life-boats.
"""

"""
### What do we want to know?
Whether you have questions in advance (like suppose I was on the ship, what would
have been my chance of survival?) or you want to play around with the data in
order to come up with some questions, both approaches suggest the following
steps:
- Explore the data (load it, look at it)
- Clean the data (missing values, splitting columns, etc.)
- Plot: Try to visualize correlations, insights, etc.
- Assumptions (formulate hypotheses, rinse and repeat)
"""

"""
### Exploring the data
Mind you, we are cheating big time here. We start with well-kept existing datasets
that allow us to quickly load and work with the data. Data scientists in the wild
spend an awfull amount of their time getting data (searching, scraping or using
API's, cleaning, joining, etc.) from various sources.
Before we start, we set up our environment:
"""

import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
%matplotlib inline
matplotlib.style.use('ggplot')

# Let's have a quick look at what we have (using your favourite editor)
!aquamacs /Users/peter/Documents/bootcamps/data/titanic/train.csv

"""
Time spend to get acquainted with the data you are working with is time well
spend. For example: We see that the column containing the names of the passengers
also contains some extras: Titles (Mr., Mrs., Miss., Master, Rev., etc.), Maiden
names of female passengers (Passenger 152 for example: Mrs. Thomas Pearce = Edith 
Wearne). Where we see two column separators next to each other (",,", we know we
are dealing with missing data.
We might be wondering what certain cloumn headers mean: SibSP? (the number of
siblings / spouses aboard) Parch? (Number of parents / children aboard).
"""

# Let's read that file into Pandas as a dataframe
df_train = pd.read_csv("../data/titanic/train.csv", sep = ",")
# And take a quick peek at the first four rows of this dataframe

"""
Once we loaded the csv file as a Pandas dataframe (the object), we can use
one of several so-called methods on that dataframe to get information:
[dataframe].shape: Presents the dimensions of the dataframe as a tuple
[dataframe].head(): Shows the first 4 rows of the dataframe
[dataframe].describe(): Generates descriptive statistics
"""
df_train.shape
df_train.head()
df_train.describe()

"""
Just 38% of the passengers did survive the disaster. 62% chance of dying. Were
we to participate in the Kaggle competition, we could predict 40% overall survival
rate on the test set.
Note that in the Age column we have 177 missing values. We also seem to have pas-
sengers that are quite young: Mean of nearly 30 years and 75% of passengers 38
years of age or younger. Eldest passenger being 80 years of age (passenger 632
"Barkworth, Mr. Algernon Henry Wilson"). However, if we have a look at the bio-
graphy of Mr. Barkworth, we find that he died in 1945 at the age of 80. He was
a survivor of the Titanic disaster. At the time of his voyage he was around 48
years of age. That brings us to the question how things are within the Age column
with the ages of the survivors? 
"""

# So let's have a look at the names of the survivors
df_train[df_train['Survived']==1]['Name']

# And check their age mentioned in our file, against the data of the Titanic website
# The first three all check out ok, so we guess that the Age entry for Mr. Barkworth was a simple mistake
# We correct the mistake in train.csv our csv file
# We load the file again; run describe: Our eldest passenger now is 74. He did
# not survive the disaster: Johan Svensson.

"""
We can use a graph to visualize certain aspects of our (training datatset). For
example: Is the chance surviving the disaster better for women than for men?
"""

"""
Let's use a simple graph to check 
"""