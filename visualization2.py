import matplotlib.pyplot as pp
import pandas as pd

import pymongo

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

branches = pd.DataFrame(db.branches.find())


branches = branches.sort_values(by = 'No_of_branches')
count = branches.Repository.count()


c=0
x=[]
for i in branches.Repository:
    if(c+40>=count):
        x = x + [i['repo']]
    c=c+1

c=0
y=[]
for i in branches.No_of_branches:
    if(c+40>=count):
        y = y + [i]
    c=c+1


pp.plot(x,y,marker=".", markersize=7)

pp.xticks(rotation=90)
pp.xlabel("Repositories")
pp.ylabel("No. of branches")
fig = pp.gcf()
fig.subplots_adjust(bottom=0.55)
fig.savefig('branches2.png', dpi=150)