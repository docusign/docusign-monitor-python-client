# coding: utf-8

# flake8: noqa

"""
    DocuSign Monitor API - v2

    An API for an integrator to access the features of DocuSign Monitor  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
"""

from __future__ import absolute_import

import base64
import os
import unittest

from docusign_monitor.client.api_client import ApiClient
from docusign_monitor.client.auth.oauth import OAuthToken


class TestConfig(object):
    def __init__(self, user_name=None, client_secret =None, user_id=None, integrator_key=None, host=None, recipient_email=None,
                 recipient_name=None, template_role_name=None, template_id=None, return_url=None, redirect_uri=None):
        self.user_name = user_name if user_name else os.environ.get("USER_NAME")
        self.client_secret = client_secret if client_secret else os.environ.get("CLIENT_SECRET")
        self.integrator_key = integrator_key if integrator_key else os.environ.get("INTEGRATOR_KEY_JWT")
        self.host = host if host else "https://demo.docusign.net/monitorapi"
        self.recipient_email = recipient_email if recipient_email else os.environ.get("USER_NAME")
        self.recipient_name = recipient_name if recipient_name else os.environ.get("USER_NAME")
        self.template_role_name = template_role_name if template_role_name else os.environ.get("USER_NAME")
        self.template_id = template_id if template_id else os.environ.get("TEMPLATE_ID")
        self.return_url = return_url if return_url else os.environ.get("REDIRECT_URI")
        self.user_id = user_id if user_id else os.environ.get("USER_ID")
        self.redirect_uri = redirect_uri if redirect_uri else os.environ.get("REDIRECT_URI")

        self.oauth_host_name = "account-d.docusign.com"
        self.private_key_bytes = base64.b64decode(os.environ.get("PRIVATE_KEY"))
        self.expires_in = 3600


class TestOauth(unittest.TestCase):
    """ AccountBillingPlan unit test stubs """

    def setUp(self):
        self.test_config = TestConfig()
        self.api_client = ApiClient(oauth_host_name=self.test_config.oauth_host_name)
        self.api_client.set_base_path("https://demo.monitor.docusign.com")
        self.api_client.set_oauth_host_name(self.test_config.oauth_host_name)

    def test_oauth_uri(self):
        self.api_client.get_oauth_host_name()
        uri = self.api_client.get_authorization_uri(client_id=self.test_config.integrator_key,
                                                redirect_uri=self.test_config.redirect_uri,
                                                    scopes=["signature", "impersonation",
                                                            "monitor.manage", "monitor.send"],
                                                response_type='code')
        self.assertTrue(isinstance(uri, str))
        self.api_client.rest_client.pool_manager.clear()

    def test_jwt_application(self):
        token_obj = self.api_client.request_jwt_application_token(client_id=self.test_config.integrator_key,
                                                           oauth_host_name=self.test_config.oauth_host_name,
                                                           private_key_bytes=self.test_config.private_key_bytes,
                                                           expires_in=self.test_config.expires_in)
        self.assertTrue(isinstance(token_obj, OAuthToken))
        self.api_client.rest_client.pool_manager.clear()

    def test_jwt_user(self):
        token_obj = self.api_client.request_jwt_user_token(client_id=self.test_config.integrator_key,
                                                           user_id=self.test_config.user_id,
                                                           oauth_host_name=self.api_client.get_oauth_host_name(),
                                                           private_key_bytes=self.test_config.private_key_bytes,
                                                           expires_in=self.test_config.expires_in
                                                           )
        self.assertTrue(isinstance(token_obj, OAuthToken))
        self.api_client.rest_client.pool_manager.clear()

    def test_authorization_code_login(self):
        self.api_client.get_oauth_host_name()
        uri = self.api_client.get_authorization_uri(client_id=self.test_config.integrator_key,
                                                    redirect_uri=self.test_config.redirect_uri,
                                                    scopes=["signature"],
                                                    response_type='code')
        self.assertTrue(isinstance(uri, str))
        self.api_client.rest_client.pool_manager.clear()


if __name__ == '__main__':
    unittest.main()
