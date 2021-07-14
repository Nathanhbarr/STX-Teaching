# -*- coding: utf-8 -*-

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as sg

# Buttons
########
# Sketch linear, exponential, potens, andengrads forskrifter.
# Find forskrift linear, exponential, potens, andengrads.
# Differentiere.
########



##########
# Sketch #
##############################
# Linear Function Forskrift  #
##############################
cLin = np.arange(-5, 5.5, step = 0.5)

a = []
for i in range(20):
    a.append(np.random.choice(cLin, 2))
    
my_df = pd.DataFrame(a)
my_df.to_csv('linear_function.csv', index=False, header=False)
    
##################################
# Exponential Function Forskrift #
##################################
cExp = np.arange(0.5, 5.5, step = 0.5)

b = []
for i in range(20):
    b.append(np.random.choice(cExp,2))



#############################
# Potens Function Forskrift #
#############################
cPot = np.arange(0.5, 5.5, step = 0.5)

c = []
for i in range(20):
    c.append(np.random.choice(cPot,2))


###################################
# Andengrads Polynomial Forskrift #
###################################
cAnden = np.arange (-5, 6, step = 1)

d = []
for i in range(20):
    d.append(np.random.choice(cAnden,3))
