# coding: utf-8

"""
    localhost:8088

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 5.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import wazo_appgateway_client
from wazo_appgateway_client.api.mailboxes_api import MailboxesApi  # noqa: E501
from wazo_appgateway_client.rest import ApiException


class TestMailboxesApi(unittest.TestCase):
    """MailboxesApi unit test stubs"""

    def setUp(self):
        self.api = wazo_appgateway_client.api.mailboxes_api.MailboxesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_mailboxes_get(self):
        """Test case for mailboxes_get

        List all mailboxes.  # noqa: E501
        """
        pass

    def test_mailboxes_mailbox_name_delete(self):
        """Test case for mailboxes_mailbox_name_delete

        Destroy a mailbox.  # noqa: E501
        """
        pass

    def test_mailboxes_mailbox_name_get(self):
        """Test case for mailboxes_mailbox_name_get

        Retrieve the current state of a mailbox.  # noqa: E501
        """
        pass

    def test_mailboxes_mailbox_name_put(self):
        """Test case for mailboxes_mailbox_name_put

        Change the state of a mailbox. (Note - implicitly creates the mailbox).  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
