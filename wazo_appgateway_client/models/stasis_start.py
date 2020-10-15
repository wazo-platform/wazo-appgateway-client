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


class StasisStart(object):
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
        'args': 'list[str]',
        'channel': 'Channel',
        'replace_channel': 'Channel'
    }

    attribute_map = {
        'args': 'args',
        'channel': 'channel',
        'replace_channel': 'replace_channel'
    }

    def __init__(self, args=None, channel=None, replace_channel=None, local_vars_configuration=None):  # noqa: E501
        """StasisStart - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._args = None
        self._channel = None
        self._replace_channel = None
        self.discriminator = None

        self.args = args
        self.channel = channel
        if replace_channel is not None:
            self.replace_channel = replace_channel

    @property
    def args(self):
        """Gets the args of this StasisStart.  # noqa: E501

        Arguments to the application  # noqa: E501

        :return: The args of this StasisStart.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this StasisStart.

        Arguments to the application  # noqa: E501

        :param args: The args of this StasisStart.  # noqa: E501
        :type args: list[str]
        """
        if self.local_vars_configuration.client_side_validation and args is None:  # noqa: E501
            raise ValueError("Invalid value for `args`, must not be `None`")  # noqa: E501

        self._args = args

    @property
    def channel(self):
        """Gets the channel of this StasisStart.  # noqa: E501


        :return: The channel of this StasisStart.  # noqa: E501
        :rtype: Channel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this StasisStart.


        :param channel: The channel of this StasisStart.  # noqa: E501
        :type channel: Channel
        """
        if self.local_vars_configuration.client_side_validation and channel is None:  # noqa: E501
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def replace_channel(self):
        """Gets the replace_channel of this StasisStart.  # noqa: E501


        :return: The replace_channel of this StasisStart.  # noqa: E501
        :rtype: Channel
        """
        return self._replace_channel

    @replace_channel.setter
    def replace_channel(self, replace_channel):
        """Sets the replace_channel of this StasisStart.


        :param replace_channel: The replace_channel of this StasisStart.  # noqa: E501
        :type replace_channel: Channel
        """

        self._replace_channel = replace_channel

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
        if not isinstance(other, StasisStart):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StasisStart):
            return True

        return self.to_dict() != other.to_dict()
