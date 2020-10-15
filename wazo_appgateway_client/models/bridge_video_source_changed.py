# coding: utf-8

"""
    localhost:8088

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 5.1.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from wazo_appgateway_client.configuration import Configuration


class BridgeVideoSourceChanged(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'bridge': 'Bridge',
        'old_video_source_id': 'str'
    }

    attribute_map = {
        'bridge': 'bridge',
        'old_video_source_id': 'old_video_source_id'
    }

    def __init__(self, bridge=None, old_video_source_id=None, local_vars_configuration=None):  # noqa: E501
        """BridgeVideoSourceChanged - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bridge = None
        self._old_video_source_id = None
        self.discriminator = None

        self.bridge = bridge
        if old_video_source_id is not None:
            self.old_video_source_id = old_video_source_id

    @property
    def bridge(self):
        """Gets the bridge of this BridgeVideoSourceChanged.  # noqa: E501


        :return: The bridge of this BridgeVideoSourceChanged.  # noqa: E501
        :rtype: Bridge
        """
        return self._bridge

    @bridge.setter
    def bridge(self, bridge):
        """Sets the bridge of this BridgeVideoSourceChanged.


        :param bridge: The bridge of this BridgeVideoSourceChanged.  # noqa: E501
        :type bridge: Bridge
        """
        if self.local_vars_configuration.client_side_validation and bridge is None:  # noqa: E501
            raise ValueError("Invalid value for `bridge`, must not be `None`")  # noqa: E501

        self._bridge = bridge

    @property
    def old_video_source_id(self):
        """Gets the old_video_source_id of this BridgeVideoSourceChanged.  # noqa: E501


        :return: The old_video_source_id of this BridgeVideoSourceChanged.  # noqa: E501
        :rtype: str
        """
        return self._old_video_source_id

    @old_video_source_id.setter
    def old_video_source_id(self, old_video_source_id):
        """Sets the old_video_source_id of this BridgeVideoSourceChanged.


        :param old_video_source_id: The old_video_source_id of this BridgeVideoSourceChanged.  # noqa: E501
        :type old_video_source_id: str
        """

        self._old_video_source_id = old_video_source_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BridgeVideoSourceChanged):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BridgeVideoSourceChanged):
            return True

        return self.to_dict() != other.to_dict()
