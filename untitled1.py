#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:22:35 2021

@author: dayshiasweet
"""

import requests
import json
import webbrowser

def get_movies_from_tastedive(title):
    baseurl = 'https://tastedive.com/api/similar'
    param = {}
    param['q']= title
    param['type']= 'movies'
    param['limit']= 5
    
    movies = requests.get(baseurl, params= param)
    
    print(movies.url)
    webbrowser.open(movies.url)
    return json.loads(movies.text)
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
move = get_movies_from_tastedive("Bridesmaids")
help= get_movies_from_tastedive("Black Panther")

for dic in move
