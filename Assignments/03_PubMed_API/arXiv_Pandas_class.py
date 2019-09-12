#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:50:01 2019

@author: robertdickson
"""
import pandas as pd
import feedparser##pip install feedparser ## this gives a dictionary.
url = 'http://export.arxiv.org/api/query?search_query=ti:%22single+molecule+microscopy%22&start=0&max_results=10'
tree = feedparser.parse(url)
## Jeff's easier way:
df_out = pd.DataFrame(tree.entries)

### Alex's request: Delete rows with "_detail" in column name:
for col in df_out.columns:
    if "_detail" in col:
        del df_out[col]
        
### My harder way, going through each entry of the feedparser object and pulling out the info I wanted.
## note that the way above is much cleaner and better uses the correspondence between JSON and Python

#results = {"Author":[],
#           "Title":[],
#           "Abstract":[],
#           "DOI":[]}
#for i in range(len(tree.entries)):
#    for key in results:
#        if key == "Author":
#            results[key].append([])
#            for j in range(len(tree.entries[i].authors)):
#                results[key][i].append(tree.entries[i].authors[j]['name'])
#        if key == "Title":
#            results[key].append(tree.entries[i].title)
#        if key == "Abstract":
#            results[key].append(tree.entries[i].summary)
#        if key == "DOI":
#            try:
#                results[key].append(tree.entries[i].arxiv_doi)
#            except:
#                results[key].append("")
