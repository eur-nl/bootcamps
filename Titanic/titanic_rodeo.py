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
