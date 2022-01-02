import json
import requests
from pandas.io.json import json_normalize
import pandas as pd
import os
import config

github_api = "https://api.github.com"
session = requests.Session()
session.auth = (config.GITHUB_USERNAME, config.GITHUB_TOKEN)


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
repos = pd.read_csv('data/repo.csv')
for i in repos['Org']:
    org = i
if os.path.exists('data/PRCount.csv'):
    os.remove('data/PRCount.csv')
for i in repos['repo']:
    pullR = pull_Requests(i, org, github_api)
    if pullR == []:
        continue
    try:
        pullR = pull_Requests(i, org, github_api)
        pullCal = pullCal + pullR
    except:
        print("Repo is read only. It's now deleted.")

        repos_with_index = repos.set_index("repo")

        repos2 = repos_with_index.drop(i, axis=0)
        repos2.to_csv('data/repo.csv')
json_normalize(pullCal).to_csv('data/PRCount.csv')






