#!/usr/bin/env python3
""" Parameterize and patch as decorators """
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Test that GithubOrgClient.org returns the correct value
    """

    @parameterized.expand([
        'google',
        'abc'
    ])
    @patch('client.get_json')
    def test_org(self, org, mock):
        """ unittest for org """
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
            expected = [item["name"] for item in payloads]
            self.assertEqual(test_git.public_repos(), expected)
            json.called_with_once()
            mock.called_with_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expected):
        """ unit-test GithubOrgClient.has_license """
        self.assertEqual(GithubOrgClient.has_license(repo, key), expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test Integration GithubOrgClient """

    repos_payload = None
    org_payload = None

    @classmethod
    def setUpClass(cls):
        """ setUpClass """
        payloads = {"return_value.json.side_effect": [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]}

        cls.get_patcher = patch('requests.get', **payloads)
        cls.mock = cls.get_patcher.start()

    def test_public_repo(self):
        """ test GithubOrgClient.public_repos """
        test = GithubOrgClient('Github')

        self.assertEqual(test.org, self.org_payload)
        self.assertEqual(test.repos_payload, self.repos_payload)
        self.assertEqual(test.public_repos(), self.expected_repos)
        self.assertEqual(test.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ test the public_repos with the argument license="apache-2.0" """
        test = GithubOrgClient("Github")

        self.assertEqual(test.public_repos(), self.expected_repos)
        self.assertEqual(test.public_repos("XLICENSE"), [])
        self.assertEqual(test.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """ tearDownClass """
        cls.get_patcher.stop()
