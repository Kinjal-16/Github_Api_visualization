import json

import pymongo
import requests
from pandas.io.json import json_normalize

import pandas as pd
import config

github_api = "https://api.github.com"
gh_session = requests.Session()
gh_session.auth = (config.GITHUB_USERNAME, config.GITHUB_TOKEN)


flag = 0
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

def branches_of_repo(repo, owner, api):
    branches = []
    next = True
    i = 1
    while next == True:
        url = api + '/repos/{}/{}/branches?page={}&per_page=100'.format(owner, repo, i)
        branch_pg = gh_session.get(url = url)
        if(branch_pg.json()==[]):
            flag=1
            break
        for item in branch_pg.json():

            branch_pg_list = [dict(item)]
            branches = branches + branch_pg_list
        if 'Link' in branch_pg.headers:
            if 'rel="next"' not in branch_pg.headers['Link']:
                next = False
        i = i + 1
    return branches

branchCount = []
for i in db.repos.find():
    org = i['Org']
for i in db.repos.find():

        branches = (branches_of_repo(i['repo'], org, github_api))
        if(flag == 0):
            bC = {"Repository": i, "No_of_branches": len(branches)}
            branchCount = branchCount + [bC]


db.branches.insert_many(branchCount)




