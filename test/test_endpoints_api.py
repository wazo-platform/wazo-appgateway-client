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
from wazo_appgateway_client.api.endpoints_api import EndpointsApi  # noqa: E501
from wazo_appgateway_client.rest import ApiException


class TestEndpointsApi(unittest.TestCase):
    """EndpointsApi unit test stubs"""

    def setUp(self):
        self.api = wazo_appgateway_client.api.endpoints_api.EndpointsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_endpoints_get(self):
        """Test case for endpoints_get

        List all endpoints.  # noqa: E501
        """
        pass

    def test_endpoints_send_message_put(self):
        """Test case for endpoints_send_message_put

        Send a message to some technology URI or endpoint.  # noqa: E501
        """
        pass

    def test_endpoints_tech_get(self):
        """Test case for endpoints_tech_get

        List available endoints for a given endpoint technology.  # noqa: E501
        """
        pass

    def test_endpoints_tech_resource_get(self):
        """Test case for endpoints_tech_resource_get

        Details for an endpoint.  # noqa: E501
        """
        pass

    def test_endpoints_tech_resource_send_message_put(self):
        """Test case for endpoints_tech_resource_send_message_put

        Send a message to some endpoint in a technology.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
