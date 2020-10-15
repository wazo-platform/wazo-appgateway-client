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


class ChannelDialplanAllOf(object):
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
        'channel': 'Channel',
        'dialplan_app': 'str',
        'dialplan_app_data': 'str'
    }

    attribute_map = {
        'channel': 'channel',
        'dialplan_app': 'dialplan_app',
        'dialplan_app_data': 'dialplan_app_data'
    }

    def __init__(self, channel=None, dialplan_app=None, dialplan_app_data=None, local_vars_configuration=None):  # noqa: E501
        """ChannelDialplanAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._channel = None
        self._dialplan_app = None
        self._dialplan_app_data = None
        self.discriminator = None

        self.channel = channel
        self.dialplan_app = dialplan_app
        self.dialplan_app_data = dialplan_app_data

    @property
    def channel(self):
        """Gets the channel of this ChannelDialplanAllOf.  # noqa: E501


        :return: The channel of this ChannelDialplanAllOf.  # noqa: E501
        :rtype: Channel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ChannelDialplanAllOf.


        :param channel: The channel of this ChannelDialplanAllOf.  # noqa: E501
        :type channel: Channel
        """
        if self.local_vars_configuration.client_side_validation and channel is None:  # noqa: E501
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def dialplan_app(self):
        """Gets the dialplan_app of this ChannelDialplanAllOf.  # noqa: E501

        The application about to be executed.  # noqa: E501

        :return: The dialplan_app of this ChannelDialplanAllOf.  # noqa: E501
        :rtype: str
        """
        return self._dialplan_app

    @dialplan_app.setter
    def dialplan_app(self, dialplan_app):
        """Sets the dialplan_app of this ChannelDialplanAllOf.

        The application about to be executed.  # noqa: E501

        :param dialplan_app: The dialplan_app of this ChannelDialplanAllOf.  # noqa: E501
        :type dialplan_app: str
        """
        if self.local_vars_configuration.client_side_validation and dialplan_app is None:  # noqa: E501
            raise ValueError("Invalid value for `dialplan_app`, must not be `None`")  # noqa: E501

        self._dialplan_app = dialplan_app

    @property
    def dialplan_app_data(self):
        """Gets the dialplan_app_data of this ChannelDialplanAllOf.  # noqa: E501

        The data to be passed to the application.  # noqa: E501

        :return: The dialplan_app_data of this ChannelDialplanAllOf.  # noqa: E501
        :rtype: str
        """
        return self._dialplan_app_data

    @dialplan_app_data.setter
    def dialplan_app_data(self, dialplan_app_data):
        """Sets the dialplan_app_data of this ChannelDialplanAllOf.

        The data to be passed to the application.  # noqa: E501

        :param dialplan_app_data: The dialplan_app_data of this ChannelDialplanAllOf.  # noqa: E501
        :type dialplan_app_data: str
        """
        if self.local_vars_configuration.client_side_validation and dialplan_app_data is None:  # noqa: E501
            raise ValueError("Invalid value for `dialplan_app_data`, must not be `None`")  # noqa: E501

        self._dialplan_app_data = dialplan_app_data

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
        if not isinstance(other, ChannelDialplanAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChannelDialplanAllOf):
            return True

        return self.to_dict() != other.to_dict()
