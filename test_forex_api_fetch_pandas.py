# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 02:29:01 2024

@author: ALBERTJUNIOR
"""

import tradermade as tm
import pandas as pd
import matplotlib.pyplot as mpl

tm.set_rest_api_key("4DiCH_O7Cr-jSEMvON7c")

tm.live(currency='EURUSD,GBPUSD',fields=["bid", "mid", "ask"]) # returns live data - fields is optional
