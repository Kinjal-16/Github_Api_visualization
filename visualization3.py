import pandas as pd
import matplotlib.pyplot as pp

pullR = pd.read_csv('data/PRCount.csv',on_bad_lines='skip')
pullR['URL'] = pullR.url
pullR['repo']=pullR['base.repo.name']
pullR['head_repo_size'] = pullR['head.repo.size']
pullR['base_repo_size']=pullR['base.repo.size']

pullR=pullR[['URL','repo','head_repo_size','base_repo_size']]
pullR.to_csv('data/temp.csv')
repos = pd.read_csv('data/repo.csv')
