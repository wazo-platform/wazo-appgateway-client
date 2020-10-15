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


class Channel(object):
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
        'accountcode': 'str',
        'caller': 'CallerID',
        'channelvars': 'object',
        'connected': 'CallerID',
        'creationtime': 'date',
        'dialplan': 'DialplanCEP',
        'id': 'str',
        'language': 'str',
        'name': 'str',
        'state': 'str'
    }

    attribute_map = {
        'accountcode': 'accountcode',
        'caller': 'caller',
        'channelvars': 'channelvars',
        'connected': 'connected',
        'creationtime': 'creationtime',
        'dialplan': 'dialplan',
        'id': 'id',
        'language': 'language',
        'name': 'name',
        'state': 'state'
    }

    def __init__(self, accountcode=None, caller=None, channelvars=None, connected=None, creationtime=None, dialplan=None, id=None, language=None, name=None, state=None, local_vars_configuration=None):  # noqa: E501
        """Channel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._accountcode = None
        self._caller = None
        self._channelvars = None
        self._connected = None
        self._creationtime = None
        self._dialplan = None
        self._id = None
        self._language = None
        self._name = None
        self._state = None
        self.discriminator = None

        self.accountcode = accountcode
        self.caller = caller
        if channelvars is not None:
            self.channelvars = channelvars
        self.connected = connected
        self.creationtime = creationtime
        self.dialplan = dialplan
        self.id = id
        self.language = language
        self.name = name
        self.state = state

    @property
    def accountcode(self):
        """Gets the accountcode of this Channel.  # noqa: E501


        :return: The accountcode of this Channel.  # noqa: E501
        :rtype: str
        """
        return self._accountcode

    @accountcode.setter
    def accountcode(self, accountcode):
        """Sets the accountcode of this Channel.


        :param accountcode: The accountcode of this Channel.  # noqa: E501
        :type accountcode: str
        """
        if self.local_vars_configuration.client_side_validation and accountcode is None:  # noqa: E501
            raise ValueError("Invalid value for `accountcode`, must not be `None`")  # noqa: E501

        self._accountcode = accountcode

    @property
    def caller(self):
        """Gets the caller of this Channel.  # noqa: E501


        :return: The caller of this Channel.  # noqa: E501
        :rtype: CallerID
        """
        return self._caller

    @caller.setter
    def caller(self, caller):
        """Sets the caller of this Channel.


        :param caller: The caller of this Channel.  # noqa: E501
        :type caller: CallerID
        """
        if self.local_vars_configuration.client_side_validation and caller is None:  # noqa: E501
            raise ValueError("Invalid value for `caller`, must not be `None`")  # noqa: E501

        self._caller = caller

    @property
    def channelvars(self):
        """Gets the channelvars of this Channel.  # noqa: E501

        Channel variables  # noqa: E501

        :return: The channelvars of this Channel.  # noqa: E501
        :rtype: object
        """
        return self._channelvars

    @channelvars.setter
    def channelvars(self, channelvars):
        """Sets the channelvars of this Channel.

        Channel variables  # noqa: E501

        :param channelvars: The channelvars of this Channel.  # noqa: E501
        :type channelvars: object
        """

        self._channelvars = channelvars

    @property
    def connected(self):
        """Gets the connected of this Channel.  # noqa: E501


        :return: The connected of this Channel.  # noqa: E501
        :rtype: CallerID
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this Channel.


        :param connected: The connected of this Channel.  # noqa: E501
        :type connected: CallerID
        """
        if self.local_vars_configuration.client_side_validation and connected is None:  # noqa: E501
            raise ValueError("Invalid value for `connected`, must not be `None`")  # noqa: E501

        self._connected = connected

    @property
    def creationtime(self):
        """Gets the creationtime of this Channel.  # noqa: E501

        Timestamp when channel was created  # noqa: E501

        :return: The creationtime of this Channel.  # noqa: E501
        :rtype: date
        """
        return self._creationtime

    @creationtime.setter
    def creationtime(self, creationtime):
        """Sets the creationtime of this Channel.

        Timestamp when channel was created  # noqa: E501

        :param creationtime: The creationtime of this Channel.  # noqa: E501
        :type creationtime: date
        """
        if self.local_vars_configuration.client_side_validation and creationtime is None:  # noqa: E501
            raise ValueError("Invalid value for `creationtime`, must not be `None`")  # noqa: E501

        self._creationtime = creationtime

    @property
    def dialplan(self):
        """Gets the dialplan of this Channel.  # noqa: E501


        :return: The dialplan of this Channel.  # noqa: E501
        :rtype: DialplanCEP
        """
        return self._dialplan

    @dialplan.setter
    def dialplan(self, dialplan):
        """Sets the dialplan of this Channel.


        :param dialplan: The dialplan of this Channel.  # noqa: E501
        :type dialplan: DialplanCEP
        """
        if self.local_vars_configuration.client_side_validation and dialplan is None:  # noqa: E501
            raise ValueError("Invalid value for `dialplan`, must not be `None`")  # noqa: E501

        self._dialplan = dialplan

    @property
    def id(self):
        """Gets the id of this Channel.  # noqa: E501

        Unique identifier of the channel.  This is the same as the Uniqueid field in AMI.  # noqa: E501

        :return: The id of this Channel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Channel.

        Unique identifier of the channel.  This is the same as the Uniqueid field in AMI.  # noqa: E501

        :param id: The id of this Channel.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def language(self):
        """Gets the language of this Channel.  # noqa: E501

        The default spoken language  # noqa: E501

        :return: The language of this Channel.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Channel.

        The default spoken language  # noqa: E501

        :param language: The language of this Channel.  # noqa: E501
        :type language: str
        """
        if self.local_vars_configuration.client_side_validation and language is None:  # noqa: E501
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def name(self):
        """Gets the name of this Channel.  # noqa: E501

        Name of the channel (i.e. SIP/foo-0000a7e3)  # noqa: E501

        :return: The name of this Channel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Channel.

        Name of the channel (i.e. SIP/foo-0000a7e3)  # noqa: E501

        :param name: The name of this Channel.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def state(self):
        """Gets the state of this Channel.  # noqa: E501


        :return: The state of this Channel.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Channel.


        :param state: The state of this Channel.  # noqa: E501
        :type state: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

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
        if not isinstance(other, Channel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Channel):
            return True

        return self.to_dict() != other.to_dict()
