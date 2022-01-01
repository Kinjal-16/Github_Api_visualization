from github import Github  # github api access
from pandas.io.json import json_normalize

import config

g = Github(config.GITHUB_TOKEN)
val = input("Enter the name of an organization \n")
usr = g.get_organization(val)
pr = usr.get_repos()
repo = []

for item in pr:
    str = item.full_name
    fn = str.index('/')
    diction = [{"repo":str[(fn + 1):],"Org":str[0:fn]}]
    repo = repo + diction
repo = json_normalize(repo)

repo.to_csv('data/repo.csv')