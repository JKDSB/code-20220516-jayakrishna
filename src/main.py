# -*- coding: utf-8 -*-
"""
Created on Sun May 16 13:15:07 2022

@author: jay
"""

# This is a simple BMI Calculator.

# Sample JSON input

import pandas as pd
from bmicalc import calcBmi
from load import jsonLoad
import argparse

"""
Can give file name in the runtime using pipeline default, for this exercise using the basic approach
"""
parser = argparse.ArgumentParser(description='BMICalc')
parser.add_argument('--json_data', required=False, default="C:/Users/sures/OneDrive/Documents/GitHub/BMICalculator/data.json")
args = vars(parser.parse_args())

data = jsonLoad(args['json_data'])
data = pd.json_normalize(data)

final_df = calcBmi(data)

