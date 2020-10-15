# coding: utf-8

"""
    localhost:8088

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 5.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import wazo_appgateway_client
from wazo_appgateway_client.models.text_message_received_all_of import TextMessageReceivedAllOf  # noqa: E501
from wazo_appgateway_client.rest import ApiException

class TestTextMessageReceivedAllOf(unittest.TestCase):
    """TextMessageReceivedAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TextMessageReceivedAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = wazo_appgateway_client.models.text_message_received_all_of.TextMessageReceivedAllOf()  # noqa: E501
        if include_optional :
            return TextMessageReceivedAllOf(
                endpoint = wazo_appgateway_client.models.endpoint.Endpoint(
                    channel_ids = [
                        '0'
                        ], 
                    resource = '0', 
                    state = '0', 
                    technology = '0', ), 
                message = wazo_appgateway_client.models.text_message.TextMessage(
                    body = '0', 
                    from = '0', 
                    to = '0', 
                    variables = wazo_appgateway_client.models.variables.variables(), )
            )
        else :
            return TextMessageReceivedAllOf(
                message = wazo_appgateway_client.models.text_message.TextMessage(
                    body = '0', 
                    from = '0', 
                    to = '0', 
                    variables = wazo_appgateway_client.models.variables.variables(), ),
        )

    def testTextMessageReceivedAllOf(self):
        """Test TextMessageReceivedAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
