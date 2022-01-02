import pandas as pd
import matplotlib.pyplot as pp
import pymongo

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

branches = pd.DataFrame(db.branches.find())


branches = branches.sort_values(by = 'No_of_branches')
count = []
i=0

c=40
branch = []
x=[]
for i in branches.Repository:
    x = x + [i['repo']]
    if(c==0):
        break
    c=c-1
y=[]
c=40
for i in branches.No_of_branches:
    y = y + [i]
    if(c==0):
        break
    c=c-1
pp.plot(x,y,marker=".", markersize=7)

pp.xticks(rotation=90)
pp.xlabel("Repositories")
pp.ylabel("No. of branches")
fig = pp.gcf()
fig.subplots_adjust(bottom=0.55)
fig.savefig('branches1.png', dpi=150)





