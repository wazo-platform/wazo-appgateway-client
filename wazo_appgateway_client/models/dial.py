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


class Dial(object):
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
        'caller': 'Channel',
        'dialstatus': 'str',
        'dialstring': 'str',
        'forward': 'str',
        'forwarded': 'Channel',
        'peer': 'Channel'
    }

    attribute_map = {
        'caller': 'caller',
        'dialstatus': 'dialstatus',
        'dialstring': 'dialstring',
        'forward': 'forward',
        'forwarded': 'forwarded',
        'peer': 'peer'
    }

    def __init__(self, caller=None, dialstatus=None, dialstring=None, forward=None, forwarded=None, peer=None, local_vars_configuration=None):  # noqa: E501
        """Dial - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._caller = None
        self._dialstatus = None
        self._dialstring = None
        self._forward = None
        self._forwarded = None
        self._peer = None
        self.discriminator = None

        if caller is not None:
            self.caller = caller
        self.dialstatus = dialstatus
        if dialstring is not None:
            self.dialstring = dialstring
        if forward is not None:
            self.forward = forward
        if forwarded is not None:
            self.forwarded = forwarded
        self.peer = peer

    @property
    def caller(self):
        """Gets the caller of this Dial.  # noqa: E501


        :return: The caller of this Dial.  # noqa: E501
        :rtype: Channel
        """
        return self._caller

    @caller.setter
    def caller(self, caller):
        """Sets the caller of this Dial.


        :param caller: The caller of this Dial.  # noqa: E501
        :type caller: Channel
        """

        self._caller = caller

    @property
    def dialstatus(self):
        """Gets the dialstatus of this Dial.  # noqa: E501

        Current status of the dialing attempt to the peer.  # noqa: E501

        :return: The dialstatus of this Dial.  # noqa: E501
        :rtype: str
        """
        return self._dialstatus

    @dialstatus.setter
    def dialstatus(self, dialstatus):
        """Sets the dialstatus of this Dial.

        Current status of the dialing attempt to the peer.  # noqa: E501

        :param dialstatus: The dialstatus of this Dial.  # noqa: E501
        :type dialstatus: str
        """
        if self.local_vars_configuration.client_side_validation and dialstatus is None:  # noqa: E501
            raise ValueError("Invalid value for `dialstatus`, must not be `None`")  # noqa: E501

        self._dialstatus = dialstatus

    @property
    def dialstring(self):
        """Gets the dialstring of this Dial.  # noqa: E501

        The dial string for calling the peer channel.  # noqa: E501

        :return: The dialstring of this Dial.  # noqa: E501
        :rtype: str
        """
        return self._dialstring

    @dialstring.setter
    def dialstring(self, dialstring):
        """Sets the dialstring of this Dial.

        The dial string for calling the peer channel.  # noqa: E501

        :param dialstring: The dialstring of this Dial.  # noqa: E501
        :type dialstring: str
        """

        self._dialstring = dialstring

    @property
    def forward(self):
        """Gets the forward of this Dial.  # noqa: E501

        Forwarding target requested by the original dialed channel.  # noqa: E501

        :return: The forward of this Dial.  # noqa: E501
        :rtype: str
        """
        return self._forward

    @forward.setter
    def forward(self, forward):
        """Sets the forward of this Dial.

        Forwarding target requested by the original dialed channel.  # noqa: E501

        :param forward: The forward of this Dial.  # noqa: E501
        :type forward: str
        """

        self._forward = forward

    @property
    def forwarded(self):
        """Gets the forwarded of this Dial.  # noqa: E501


        :return: The forwarded of this Dial.  # noqa: E501
        :rtype: Channel
        """
        return self._forwarded

    @forwarded.setter
    def forwarded(self, forwarded):
        """Sets the forwarded of this Dial.


        :param forwarded: The forwarded of this Dial.  # noqa: E501
        :type forwarded: Channel
        """

        self._forwarded = forwarded

    @property
    def peer(self):
        """Gets the peer of this Dial.  # noqa: E501


        :return: The peer of this Dial.  # noqa: E501
        :rtype: Channel
        """
        return self._peer

    @peer.setter
    def peer(self, peer):
        """Sets the peer of this Dial.


        :param peer: The peer of this Dial.  # noqa: E501
        :type peer: Channel
        """
        if self.local_vars_configuration.client_side_validation and peer is None:  # noqa: E501
            raise ValueError("Invalid value for `peer`, must not be `None`")  # noqa: E501

        self._peer = peer

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
        if not isinstance(other, Dial):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Dial):
            return True

        return self.to_dict() != other.to_dict()