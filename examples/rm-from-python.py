# instead of calling python from Rapidminer, call RM from python
# https://github.com/rapidminer/python-rapidminer/blob/master/examples/studio_examples.ipynb

# imports
from ast import operator
from concurrent.futures import process
import os
import rapidminer
import pandas as pd


############################################################### Setup
# the rapidminer install location
# could also be RAPIDMINER_HOME environment variable
rm_home = "/Applications/RapidMiner Studio.app/Contents/Resources/RapidMiner-Studio/"
connector = rapidminer.Studio(rm_home)




############################################################### Example 1 - Save a dataset to Repository
# review the url above, but some testing, especially for repositories
# write a pandas dataframe to a repository
URL = "https://vincentarelbundock.github.io/Rdatasets/csv/ggplot2/diamonds.csv"
dia = pd.read_csv(URL)
connector.write_resource(dia, "//BU/data/diamonds")

### ^^ actually fires up Rapidminer in the background, resource above talks about some optimization code (minimal) is shown in the resource above



############################################################### Example 2 - Run a process front to back
# what does running a process look like coming back in python
# can this be used to evaluate/autograde a process?
hw = connector.run_process("//BU/hw1")

type(hw)
hw.shape

# so we get the output - ExampleSet -> pandas, multiple objects out as a tuple


############################################################### Example 3 - run an operator from a process?
# from the docs, the run process will execute the entire process unless a string for the specific operator is passed, will just run that


# test against above, the aggregate should only be 1 row given how the process is specified
dia2 = dia.loc[dia.cut=='Good', :]

# the Aggregate operator has two ouputs, as such, specifying two output objects
agg, ori = connector.run_process("//BU/hw1", inputs=dia2, operator="Aggregate")
type(agg)
type(ori)
agg.shape
ori.shape
agg
 
# The string is the name shown on top of the operator



##### wishlist

# - inspect a process
# - run the process with logs/inspect after run (did a given operator get an exampleset of size 100,3 (rows/cols))
# - run a segment of the process, not just one operator

