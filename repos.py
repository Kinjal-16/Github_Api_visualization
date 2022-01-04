from github import Github  # github api access
from pandas.io.json import json_normalize
import pymongo
import config

g = Github(config.GITHUB_TOKEN)
val = input("Enter the name of an organization (like uber)\n")
usr = g.get_organization(val)
pr = usr.get_repos()
repo = []

for item in pr:
    str = item.full_name
    fn = str.index('/')
    diction = [{"repo":str[(fn + 1):],"Org":str[0:fn]}]
    repo = repo + diction

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

db.repos.insert_many(repo)
