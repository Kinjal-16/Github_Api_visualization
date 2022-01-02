import pandas as pd
import matplotlib.pyplot as pp

pullR = pd.read_csv('data/PRCount.csv',on_bad_lines='skip')

pullR['URL'] = pullR.url
pullR['repo']=pullR['base.repo.name']
pullR['head_repo_size'] = pullR['head.repo.size']
pullR['base_repo_size']=pullR['base.repo.size']
pullR['PullR_Size']= ((abs(pullR['head_repo_size'] - pullR['base_repo_size']))/pullR['base_repo_size'])*100

pullR=pullR[['URL','repo','head_repo_size','base_repo_size','PullR_Size']]

pullR_g= pullR.groupby(["repo"])[["PullR_Size"]].mean()
pullR_g = pullR_g.rename({'PullR_Size': 'size'})
pullR_g = pullR_g.sort_values(by=['PullR_Size'],ascending=True)
c=30
x=[]
for i in pullR_g.index:
    x=x+[i]
    c=c-1
    if c==0:
        break
c=30
y=[]
for i in pullR_g.PullR_Size:
    y=y+[i]
    c=c-1
    if c==0:
        break


pp.bar(x,y)
pp.xticks(rotation=90)
fig = pp.gcf()
fig.subplots_adjust(bottom=0.50)
pp.xlabel("Repositories")
pp.ylabel("Pull Request Size(in %)")
fig.savefig('PR2.png', dpi=150)
pp.show()

