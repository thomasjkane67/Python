# !/usr/bin/python3.6
# https://newsapi.org/docs

'''
https://newsapi.org/docs/client-libraries/python
'''

import json
import urllib.request

Criteria = input("Enter search criteria: ")
myKey = 'bab2dfb0c9974bf2b30691f0e1ddb1a2'
URL = 'https://newsapi.org/v2/everything?q=' + Criteria + '&apiKey=' + myKey

websource = urllib.request.urlopen(URL)
data = json.loads(websource.read().decode())
Articles = (len(data['articles']))

for Count in range(Articles):
    print()
    print("Source: " + str(data['articles'][Count]['source']['name']))
    print("Author: " + str(data['articles'][Count]['author']))
    print("Title: " + str(data['articles'][Count]['title']))
    print("\t" + str(data['articles'][Count]['content']))
    print("\t" + str(data['articles'][Count]['url']))
