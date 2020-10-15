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
from wazo_appgateway_client.models.channel_hold import ChannelHold  # noqa: E501
from wazo_appgateway_client.rest import ApiException

class TestChannelHold(unittest.TestCase):
    """ChannelHold unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ChannelHold
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = wazo_appgateway_client.models.channel_hold.ChannelHold()  # noqa: E501
        if include_optional :
            return ChannelHold(
                channel = wazo_appgateway_client.models.channel.Channel(
                    accountcode = '0', 
                    caller = wazo_appgateway_client.models.caller_id.CallerID(
                        name = '0', 
                        number = '0', ), 
                    channelvars = wazo_appgateway_client.models.channelvars.channelvars(), 
                    connected = wazo_appgateway_client.models.caller_id.CallerID(
                        name = '0', 
                        number = '0', ), 
                    creationtime = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    dialplan = wazo_appgateway_client.models.dialplan_cep.DialplanCEP(
                        app_data = '0', 
                        app_name = '0', 
                        context = '0', 
                        exten = '0', 
                        priority = 56, ), 
                    id = '0', 
                    language = '0', 
                    name = '0', 
                    state = '0', ), 
                musicclass = '0'
            )
        else :
            return ChannelHold(
                channel = wazo_appgateway_client.models.channel.Channel(
                    accountcode = '0', 
                    caller = wazo_appgateway_client.models.caller_id.CallerID(
                        name = '0', 
                        number = '0', ), 
                    channelvars = wazo_appgateway_client.models.channelvars.channelvars(), 
                    connected = wazo_appgateway_client.models.caller_id.CallerID(
                        name = '0', 
                        number = '0', ), 
                    creationtime = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    dialplan = wazo_appgateway_client.models.dialplan_cep.DialplanCEP(
                        app_data = '0', 
                        app_name = '0', 
                        context = '0', 
                        exten = '0', 
                        priority = 56, ), 
                    id = '0', 
                    language = '0', 
                    name = '0', 
                    state = '0', ),
        )

    def testChannelHold(self):
        """Test ChannelHold"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
