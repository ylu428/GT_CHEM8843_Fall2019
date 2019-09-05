## Assignment String processing: Google Flights

### This will be an involved assignment.

Please construct appropriate urls to pull up a website on google flights.
Look at the structure of the URL for different departure and arrival cities for round trips. You will need to specify the IATA airport codes and the departure and return dates. 

Make each of these a list or array that you can cycle through the elements of to construct multiple urls within a loop. As a minimum for Tuesday's class, print out at least 5 urls from a loop that, if pasted into the address bar of your browser, would pull up webpages with flight options in google flights.

Try to learn about the following packages and have them installed by class on Tuesday (pandas, datetime, dateutil, selenium, webdriver-manager). You will need to install selenium either in anaconda using conda install selenium or pip install selenium. Same with webdriver-manager (pip install webdriver-manager, or conda install may also work) Use the following import commands. Check the documentation of these (and sites like stack overflow) to become familiar with usage of these packages. play around a bit if you can.

import pandas as pd  
import datetime
from dateutil import parser
from pandas import ExcelWriter###have to install xlsxwriter in anaconda
from selenium import webdriver### need to install selenium in environment
from webdriver_manager.chrome import ChromeDriverManager###pip install webdriver-manager
import time


You will also need to download chromedriver from: https://chromedriver.chromium.org
and make sure that Google Chrome is installed on your computer (sorry Baijie...). Hopefully this will work withhout too much trouble, but you may not be able to check it until Tuesday, in class.

the unix executable file chromedriver will likely need to be installed in your working directory. 

While you can use jupyter notebooks for this first part, I would also recommend getting accustomed to Spyder (available from within Anaconda navigator as well).

You will work in class on Tuesday in groups, but please come prepared with an idea of how to proceed.

Please work together and ask questions of others. Dom and I are also available, and Baijie is officially a TA, so he can help too, while he is also figuring out some of these issues.

The best way to learn is to have to struggle through projects. The effort will be worth it and all of you can contribute to the group effort, if you come prepared.

See you on Tuesday, if not before.

--Rob


