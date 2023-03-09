# -*- coding: utf-8 -*-
"""
mar 6 2023

@author: mauspad
"""
print("This script loops over every csv in the data directory. IF YOU GET AN ERROR, CHECK TO SEE IF THE CSV IS BUGGED")

#import packages
import pandas as pd
import glob

#set directory
path = "data/*.csv"
for fname in glob.glob(path):

	# turn csv into dataframe
	df = pd.read_csv(fname)

	# drop practice rows
	df.dropna(subset=["corrans"], inplace=True)

	# make lists and variables
	key_resp = df["run_response.corr"].tolist()
	
	# sum and score
	Score = sum(key_resp)
	perc = Score/len(key_resp)*100
	print(fname)
	print(perc)