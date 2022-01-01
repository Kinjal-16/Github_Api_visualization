import json

import requests
from pandas.io.json import json_normalize

import pandas as pd
import config

github_api = "https://api.github.com"
gh_session = requests.Session()
gh_session.auth = (config.GITHUB_USERNAME, config.GITHUB_TOKEN)

url = github_api + '/repos/apache/spark/commits'
commits = gh_session.get(url=url)
commits_json = commits.json()
flag = 0

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
repos = pd.read_csv('data/repo.csv')
for i in repos['Org']:
    org = i
for i in repos['repo']:

        branches = (branches_of_repo(i, org, github_api))
        if(flag == 0):
            bC = {"Repository": i, "No_of_branches": len(branches)}
            print(bC)
            branchCount = branchCount + [bC]

branchCount = json_normalize(branchCount)

branchCount.to_csv('data/branchCount.csv')




