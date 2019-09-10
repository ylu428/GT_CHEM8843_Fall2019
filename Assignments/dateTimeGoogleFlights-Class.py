#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:40:38 2019

@author: robertdickson
"""
import pandas as pd## need to install pandas in enviroment through anaconda
import datetime
from dateutil import parser
from pandas import ExcelWriter###have to install xlsxwriter in anaconda
from selenium import webdriver### need to install selenium in environment
from webdriver_manager.chrome import ChromeDriverManager###pip install webdriver-manager
import time


deltaT = 2  ## days plus and minus to search from entered dates
plusMinusDays=2*deltaT+1  # total number of days to search (2deltaT+1)
depart = ['ATL']#,'BHM','CHA','GSP']#,'CLT']#,'BHM']#,'JFK','LAX','BOS'] # departure airport codes
dDate=['2020-05-24','2019-11-24']#'2020-04-05']#,'2020-05-27']#,'2019-11-24','2020-06-11']#'2020-05-27']#,'2019-07-28','2019-12-24']#,'2019-07-02']#,'2020-04-04']  ## departure dates
i=0 ## for indexing in date loop below
arrive = ['UIO']#,'CTS']#,'ZRH','BSL']#,'DUB'] # arrival airport codes (could make a list if checking multiple airports)
rDate=['2020-05-31','2019-11-30']#'2020-04-11']#,'2020-06-08']#'2019-11-30',,'2020-06-23']#,'2019-08-04','2020-01-02']#,'2019-07-10']#,'2020-04-12'] # return dates
dDay = ['']*plusMinusDays*len(dDate)    ## create space for date arrays (departure and return)
rDay = ['']*plusMinusDays*len(rDate)

### generate dates for travel, +/- deltaT days on outbound and return
for ddate,rdate in zip(dDate,rDate):
    for timeD in range(plusMinusDays):
        dDay[i+timeD]=(parser.parse(ddate)+datetime.timedelta(days=(timeD-deltaT))).strftime('%Y-%m-%d')
        rDay[i+timeD]=(parser.parse(rdate)+datetime.timedelta(days=(timeD-deltaT))).strftime('%Y-%m-%d')
    i+=plusMinusDays

### call the chrome browser to generate website and scrape data
driver = webdriver.Chrome(ChromeDriverManager().install())