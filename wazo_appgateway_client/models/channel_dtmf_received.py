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


class ChannelDtmfReceived(object):
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
        'digit': 'str',
        'duration_ms': 'int'
    }

    attribute_map = {
        'channel': 'channel',
        'digit': 'digit',
        'duration_ms': 'duration_ms'
    }

    def __init__(self, channel=None, digit=None, duration_ms=None, local_vars_configuration=None):  # noqa: E501
        """ChannelDtmfReceived - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._channel = None
        self._digit = None
        self._duration_ms = None
        self.discriminator = None

        self.channel = channel
        self.digit = digit
        self.duration_ms = duration_ms

    @property
    def channel(self):
        """Gets the channel of this ChannelDtmfReceived.  # noqa: E501


        :return: The channel of this ChannelDtmfReceived.  # noqa: E501
        :rtype: Channel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ChannelDtmfReceived.


        :param channel: The channel of this ChannelDtmfReceived.  # noqa: E501
        :type channel: Channel
        """
        if self.local_vars_configuration.client_side_validation and channel is None:  # noqa: E501
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def digit(self):
        """Gets the digit of this ChannelDtmfReceived.  # noqa: E501

        DTMF digit received (0-9, A-E, # or *)  # noqa: E501

        :return: The digit of this ChannelDtmfReceived.  # noqa: E501
        :rtype: str
        """
        return self._digit

    @digit.setter
    def digit(self, digit):
        """Sets the digit of this ChannelDtmfReceived.

        DTMF digit received (0-9, A-E, # or *)  # noqa: E501

        :param digit: The digit of this ChannelDtmfReceived.  # noqa: E501
        :type digit: str
        """
        if self.local_vars_configuration.client_side_validation and digit is None:  # noqa: E501
            raise ValueError("Invalid value for `digit`, must not be `None`")  # noqa: E501

        self._digit = digit

    @property
    def duration_ms(self):
        """Gets the duration_ms of this ChannelDtmfReceived.  # noqa: E501

        Number of milliseconds DTMF was received  # noqa: E501

        :return: The duration_ms of this ChannelDtmfReceived.  # noqa: E501
        :rtype: int
        """
        return self._duration_ms

    @duration_ms.setter
    def duration_ms(self, duration_ms):
        """Sets the duration_ms of this ChannelDtmfReceived.

        Number of milliseconds DTMF was received  # noqa: E501

        :param duration_ms: The duration_ms of this ChannelDtmfReceived.  # noqa: E501
        :type duration_ms: int
        """
        if self.local_vars_configuration.client_side_validation and duration_ms is None:  # noqa: E501
            raise ValueError("Invalid value for `duration_ms`, must not be `None`")  # noqa: E501

        self._duration_ms = duration_ms

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
        if not isinstance(other, ChannelDtmfReceived):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChannelDtmfReceived):
            return True

        return self.to_dict() != other.to_dict()
