import json

import pymongo
import requests
from pandas.io.json import json_normalize
import pandas as pd
import os
import config

github_api = "https://api.github.com"
session = requests.Session()
session.auth = (config.GITHUB_USERNAME, config.GITHUB_TOKEN)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.classDB
def pull_Requests(repo, owner, api):
    pullR = []
    next = True
    i = 1
    while next == True:
        url = api + '/repos/{}/{}/pulls?page={}&per_page=100'.format(owner, repo, i)
        pull = session.get(url=url)
        if pull.json() == []:
            break
        for k in pull.json():
            dic = dict(k)
            pullR = pullR + [dic]
        if 'Link' in pull.headers:
            if 'rel="next"' not in pull.headers['Link']:
                next = False
        i = i + 1
        return pullR

pullCal = []
for i in db.repos.find():
    org = i['Org']

for i in db.repos.find():

    try:
        pullR = pull_Requests(i['repo'], org, github_api)
        if pullR == []:
            continue
        pullCal = pullCal + pullR
    except:
        print (i)
        print("Repo is read only. Skipping it")

db.pullR.insert_many((pullCal))






