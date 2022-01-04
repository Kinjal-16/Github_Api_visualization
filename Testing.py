import requests
from pandas.io.json import json_normalize
from Script1 import branches_of_repo
import unittest
import config

github_api = "https://api.github.com"
gh_session = requests.Session()
gh_session.auth = (config.GITHUB_USERNAME, config.GITHUB_TOKEN)
class Test(unittest.TestCase):
    def test_branch(self):
        print('Enter the name of a repository:\n')
        x = input()
        print('Enter the name of an organization:\n')
        y = input()
        print('Enter the expected number of branches\n')
        r = input()
        self.assertEqual(len(branches_of_repo(x,y,github_api)),int(r))






