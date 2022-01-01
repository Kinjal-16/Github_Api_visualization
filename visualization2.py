import matplotlib.pyplot as pp
import pandas as pd

branches = pd.read_csv('data/branchCount.csv')


branches = branches.sort_values(by = 'No_of_branches')
count = branches.Repository.count()


c=0
x=[]
for i in branches.Repository:
    if(c+40>=count):
        x = x + [i]
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