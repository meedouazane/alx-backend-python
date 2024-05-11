#!/usr/bin/env python3
""" Parameterize and patch as decorators """
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """ unit-test GithubOrgClient._public_repos_url """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_res:
            payload = {"repos_url": "Answer"}
            mock_res.return_value = payload
            test_git = GithubOrgClient('test')
            self.assertEqual(test_git._public_repos_url, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, json):
        """ unit-test GithubOrgClient.public_repos """
        payloads = [{"name": "google"}, {"name": "abc"}]
        json.return_value = payloads
        with patch('client.GithubOrgClient._public_repos_url') as mock:
            mock.return_value = "Answer"
            test_git = GithubOrgClient('test')
            payload = [item["name"] for item in payloads]
            self.assertEqual(test_git.public_repos(), payload)
            json.called_with_once()
            mock.called_with_once()
