#!/usr/bin/env python3
""" Parameterize and patch as decorators """
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Test that GithubOrgClient.org returns the correct value """

    @parameterized.expand([
        'google',
        'abc'
    ])
    @patch('client.get_json')
    def test_org(self, org, mock):
        test_git = GithubOrgClient(org)
        test_git.org()
        mock.called_with_once(test_git.ORG_URL.format(org=org))
