# Grammar of Graphics
# R:ggplot2 => Py:ggplot
# https://plotnine.readthedocs.io/en/stable/index.html

'''
Layers approach:
* Theme
* Coordinates
* Statistical Transformation
* Facets
* Geometric Objects
* Aesthetics
* Data
'''

import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from plotnine import *
from plotnine.data import mpg

mpg.shape
mpg.columns
mpg.head()

'''

| manufacturer | model  | displ | year | cyl | trans | drv | cty | hwy | fl |  class  |
---------------------------------------------------------------------------------------
| audi         | A4     | 1.8   | 2002 | 4   | auto  | f   | 18  | 29  | p  | compact |
| volkswagen   | passat | 2.0   | 2004 | 4   | auto  | f   | 16  | 26  | p  | midsize |
...

'''

(ggplot(mpg)                       # Data
 + aes(x='class', fill='fl')       # Aesthetics (variables)
 + geom_bar(size=10))              # Geometric Object


(ggplot(mpg)
 + aes(x='class', fill='drv')    # splitting the bar
 + geom_bar(size=20)
 + coord_flip()                  # flipping the x- and y-axes
 + labs(title='Number of Vehicles per Class',
        x='Vehicle Class',
        y='Number of Vehicles')) # customizing labels


(ggplot(mpg)
 + aes(x='displ', y='hwy', color='class')
 + geom_point()
 + labs(title='Engine Displacement vs. Highway Miles per Gallon',
        x='Engine Displacement, in Litres',
        y='Highway Miles per Gallon'))
