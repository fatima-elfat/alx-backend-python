#!/usr/bin/env python3
"""
Test client.
task 4, 5, 6, 7, 8 and 9.
"""
from client import (
    GithubOrgClient
)
from fixtures import TEST_PAYLOAD
import json
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import (
    Mock,
    PropertyMock,
    patch,
)


class TestGithubOrgClient(unittest.TestCase):
    """
    Test Github Org Client
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org, mock):
        """
        This method should test that
        GithubOrgClient.org returns the correct value.
        Use @patch as a decorator to make sure get_json
        is called once with the expected argument
        but make sure it is not executed.
        """
        org_client = GithubOrgClient(org)
        org_client.org()
        s = "https://api.github.com/orgs/{}".format(org)
        mock.assert_called_once_with(s)

    def test_public_repos_url(self):
        """
        unit-test GithubOrgClient._public_repos_url.
        Use patch as a context manager to
        patch GithubOrgClient.org and make
        it return a known payload.
        Test that the result of _public_repos_url is
        the expected one based on the mocked payload.
        """
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock
        ) as mock:
            mock.return_value = {"repos_url": "testing_url"}
            self.assertEqual(
                GithubOrgClient("testing_repo")._public_repos_url,
                "testing_url"
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test that the list of repos is what you
        expect from the chosen payload.
        Test that the mocked property and the mocked
        get_json was called once.
        Use @patch as a decorator to mock get_json
        and make it return a payload of your choice.
        Use patch as a context manager to mock GihubOrgClient._public_repos_url
        and return a value of your choice.
        """
        test_ = [
            {
                "name": "val1"
                },
            {
                "name": "val2"
                },
            {
                "name": "val3"
                }
            ]
        mock_get_json.return_value = test_
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_public:

            mock_public.return_value = "testing_url"
            l_ = list([val["name"] for val in test_])
            self.assertEqual(
                GithubOrgClient("testing_org").public_repos(),
                l_
            )
            mock_public.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        (
            {"license": {"key": "my_license"}},
            "my_license", True
        ),
        (
            {"license": {"key": "other_license"}},
            "my_license", False
        )
    ])
    def test_has_license(self, repo, key, expected_val):
        """
        unit-test GithubOrgClient.has_license.
        """
        self.assertEqual(
            GithubOrgClient.has_license(repo, key),
            expected_val)


@parameterized_class(
    (
        "org_payload", "repos_payload",
        "expected_repos", "apache2_repos"
    ),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    implement the setUpClass and tearDownClass
    which are part of the unittest.TestCase API.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class.
        """
        setupConf = {
            "return_value.json.side_effect":
                [cls.org_payload, cls.repos_payload,
                 cls.org_payload, cls.repos_payload]
        }
        cls.get_patcher = patch("requests.get", **setupConf)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Teardown method.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        test GithubOrgClient.public_repos.
        Make sure that the method returns
        the expected results based on the fixtures.
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos)
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """
        test the public_repos with the argument
        license="apache-2.0" and make sure the
        result matches the expected value from
        the fixtures.
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos("apache-2.0"),
            self.apache2_repos
        )
        self.mock.assert_called()
