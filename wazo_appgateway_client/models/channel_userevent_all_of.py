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


class ChannelUsereventAllOf(object):
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
        'channel': 'Channel',
        'endpoint': 'Endpoint',
        'eventname': 'str',
        'userevent': 'object'
    }

    attribute_map = {
        'bridge': 'bridge',
        'channel': 'channel',
        'endpoint': 'endpoint',
        'eventname': 'eventname',
        'userevent': 'userevent'
    }

    def __init__(self, bridge=None, channel=None, endpoint=None, eventname=None, userevent=None, local_vars_configuration=None):  # noqa: E501
        """ChannelUsereventAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bridge = None
        self._channel = None
        self._endpoint = None
        self._eventname = None
        self._userevent = None
        self.discriminator = None

        if bridge is not None:
            self.bridge = bridge
        if channel is not None:
            self.channel = channel
        if endpoint is not None:
            self.endpoint = endpoint
        self.eventname = eventname
        self.userevent = userevent

    @property
    def bridge(self):
        """Gets the bridge of this ChannelUsereventAllOf.  # noqa: E501


        :return: The bridge of this ChannelUsereventAllOf.  # noqa: E501
        :rtype: Bridge
        """
        return self._bridge

    @bridge.setter
    def bridge(self, bridge):
        """Sets the bridge of this ChannelUsereventAllOf.


        :param bridge: The bridge of this ChannelUsereventAllOf.  # noqa: E501
        :type bridge: Bridge
        """

        self._bridge = bridge

    @property
    def channel(self):
        """Gets the channel of this ChannelUsereventAllOf.  # noqa: E501


        :return: The channel of this ChannelUsereventAllOf.  # noqa: E501
        :rtype: Channel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ChannelUsereventAllOf.


        :param channel: The channel of this ChannelUsereventAllOf.  # noqa: E501
        :type channel: Channel
        """

        self._channel = channel

    @property
    def endpoint(self):
        """Gets the endpoint of this ChannelUsereventAllOf.  # noqa: E501


        :return: The endpoint of this ChannelUsereventAllOf.  # noqa: E501
        :rtype: Endpoint
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this ChannelUsereventAllOf.


        :param endpoint: The endpoint of this ChannelUsereventAllOf.  # noqa: E501
        :type endpoint: Endpoint
        """

        self._endpoint = endpoint

    @property
    def eventname(self):
        """Gets the eventname of this ChannelUsereventAllOf.  # noqa: E501

        The name of the user event.  # noqa: E501

        :return: The eventname of this ChannelUsereventAllOf.  # noqa: E501
        :rtype: str
        """
        return self._eventname

    @eventname.setter
    def eventname(self, eventname):
        """Sets the eventname of this ChannelUsereventAllOf.

        The name of the user event.  # noqa: E501

        :param eventname: The eventname of this ChannelUsereventAllOf.  # noqa: E501
        :type eventname: str
        """
        if self.local_vars_configuration.client_side_validation and eventname is None:  # noqa: E501
            raise ValueError("Invalid value for `eventname`, must not be `None`")  # noqa: E501

        self._eventname = eventname

    @property
    def userevent(self):
        """Gets the userevent of this ChannelUsereventAllOf.  # noqa: E501

        Custom Userevent data  # noqa: E501

        :return: The userevent of this ChannelUsereventAllOf.  # noqa: E501
        :rtype: object
        """
        return self._userevent

    @userevent.setter
    def userevent(self, userevent):
        """Sets the userevent of this ChannelUsereventAllOf.

        Custom Userevent data  # noqa: E501

        :param userevent: The userevent of this ChannelUsereventAllOf.  # noqa: E501
        :type userevent: object
        """
        if self.local_vars_configuration.client_side_validation and userevent is None:  # noqa: E501
            raise ValueError("Invalid value for `userevent`, must not be `None`")  # noqa: E501

        self._userevent = userevent

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
        if not isinstance(other, ChannelUsereventAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChannelUsereventAllOf):
            return True

        return self.to_dict() != other.to_dict()
