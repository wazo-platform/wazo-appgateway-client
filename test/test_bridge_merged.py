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
from wazo_appgateway_client.models.bridge_merged import BridgeMerged  # noqa: E501
from wazo_appgateway_client.rest import ApiException

class TestBridgeMerged(unittest.TestCase):
    """BridgeMerged unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BridgeMerged
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = wazo_appgateway_client.models.bridge_merged.BridgeMerged()  # noqa: E501
        if include_optional :
            return BridgeMerged(
                bridge = wazo_appgateway_client.models.bridge.Bridge(
                    bridge_class = '0', 
                    bridge_type = '0', 
                    channels = [
                        '0'
                        ], 
                    creationtime = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    creator = '0', 
                    id = '0', 
                    name = '0', 
                    technology = '0', 
                    video_mode = '0', 
                    video_source_id = '0', ), 
                bridge_from = wazo_appgateway_client.models.bridge.Bridge(
                    bridge_class = '0', 
                    bridge_type = '0', 
                    channels = [
                        '0'
                        ], 
                    creationtime = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    creator = '0', 
                    id = '0', 
                    name = '0', 
                    technology = '0', 
                    video_mode = '0', 
                    video_source_id = '0', )
            )
        else :
            return BridgeMerged(
                bridge = wazo_appgateway_client.models.bridge.Bridge(
                    bridge_class = '0', 
                    bridge_type = '0', 
                    channels = [
                        '0'
                        ], 
                    creationtime = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    creator = '0', 
                    id = '0', 
                    name = '0', 
                    technology = '0', 
                    video_mode = '0', 
                    video_source_id = '0', ),
                bridge_from = wazo_appgateway_client.models.bridge.Bridge(
                    bridge_class = '0', 
                    bridge_type = '0', 
                    channels = [
                        '0'
                        ], 
                    creationtime = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    creator = '0', 
                    id = '0', 
                    name = '0', 
                    technology = '0', 
                    video_mode = '0', 
                    video_source_id = '0', ),
        )

    def testBridgeMerged(self):
        """Test BridgeMerged"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()