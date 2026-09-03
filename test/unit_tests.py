# coding: utf-8

from __future__ import absolute_import, print_function
from docusign_monitor import DocuMonitorApi, ApiException

import base64
import os
import unittest
import docusign_monitor as docusign

Username = os.environ.get("USER_NAME")
IntegratorKey = os.environ.get("INTEGRATOR_KEY_JWT")
BaseUrl = "https://api-d.docusign.com"
OauthHostName = "account-d.docusign.com"
SignTest1File = "{}/docs/SignTest1.pdf".format(os.path.dirname(os.path.abspath(__file__)))
TemplateId = os.environ.get("TEMPLATE_ID")
UserId = os.environ.get("USER_ID")
PrivateKeyBytes = base64.b64decode(os.environ.get("PRIVATE_KEY"))
accountId = os.environ.get("ACCOUNT_ID")


class SdkUnitTests(unittest.TestCase):

    def setUp(self):
        self.api_client = docusign.ApiClient(base_path=BaseUrl, oauth_host_name=OauthHostName)
        self.api_client.rest_client.pool_manager.clear()

        docusign.configuration.api_client = self.api_client
        self.user_info = None
        try:
            self.api_client.host = BaseUrl
            token = (self.api_client.request_jwt_user_token(client_id=IntegratorKey,
                                                            user_id=UserId,
                                                            oauth_host_name=OauthHostName,
                                                            private_key_bytes=PrivateKeyBytes,
                                                            expires_in=3600,
                                                            scopes=["signature" ]))
            self.user_info = self.api_client.get_user_info(token.access_token)
            self.api_client.rest_client.pool_manager.clear()
            docusign.configuration.api_client = self.api_client

            self.organization_id = None
            for account in self.user_info.accounts:
                if account.organization:
                    self.organization_id = account.organization.organization_id
                    break

        except ApiException as e:
            print("\nException when setting up DocuSign Monitor API: %s" % e)
        self.api_client.rest_client.pool_manager.clear()

    def tearDown(self):
        self.api_client.rest_client.pool_manager.clear()

    def testStream(self):
        try:
            self.assertIsNotNone(self.user_info)
            self.assertTrue(len(self.user_info.accounts) > 0)
            self.assertIsNotNone(self.user_info.accounts[0].account_id)
            self.assertIsNotNone(self.organization_id)

            api = DocuMonitorApi()

            stream_response = api.stream(self.organization_id, cursor=None, limit=100)

            self.assertIsNotNone(stream_response)
            self.assertIsNotNone(stream_response.end_cursor)

        except ApiException as e:
            print("\nException when setting up DocuSign Monitor API: %s" % e)
        self.api_client.rest_client.pool_manager.clear()


if __name__ == '__main__':
    unittest.main()
