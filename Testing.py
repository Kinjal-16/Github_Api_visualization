import requests
from pandas.io.json import json_normalize
from Script1 import branches_of_repo
from Script2 import pull_Requests
import unittest
import config

github_api = "https://api.github.com"
gh_session = requests.Session()
gh_session.auth = (config.GITHUB_USERNAME, config.GITHUB_TOKEN)
class Test(unittest.TestCase):
    def test_branch(self):
        self.assertEqual(len(branches_of_repo('clay','uber',github_api)),27)
        self.assertEqual(len(branches_of_repo('kraken', 'uber', github_api)), 39)
        self.assertEqual(len(branches_of_repo('piranha', 'uber', github_api)), 5)
        self.assertEqual(len(branches_of_repo('zanzibar', 'uber', github_api)), 43)
        self.assertEqual(len(branches_of_repo('NullAway', 'uber', github_api)), 17)





