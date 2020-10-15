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


class Module(object):
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
        'description': 'str',
        'name': 'str',
        'status': 'str',
        'support_level': 'str',
        'use_count': 'int'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'status': 'status',
        'support_level': 'support_level',
        'use_count': 'use_count'
    }

    def __init__(self, description=None, name=None, status=None, support_level=None, use_count=None, local_vars_configuration=None):  # noqa: E501
        """Module - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._name = None
        self._status = None
        self._support_level = None
        self._use_count = None
        self.discriminator = None

        self.description = description
        self.name = name
        self.status = status
        self.support_level = support_level
        self.use_count = use_count

    @property
    def description(self):
        """Gets the description of this Module.  # noqa: E501

        The description of this module  # noqa: E501

        :return: The description of this Module.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Module.

        The description of this module  # noqa: E501

        :param description: The description of this Module.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this Module.  # noqa: E501

        The name of this module  # noqa: E501

        :return: The name of this Module.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Module.

        The name of this module  # noqa: E501

        :param name: The name of this Module.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this Module.  # noqa: E501

        The running status of this module  # noqa: E501

        :return: The status of this Module.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Module.

        The running status of this module  # noqa: E501

        :param status: The status of this Module.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def support_level(self):
        """Gets the support_level of this Module.  # noqa: E501

        The support state of this module  # noqa: E501

        :return: The support_level of this Module.  # noqa: E501
        :rtype: str
        """
        return self._support_level

    @support_level.setter
    def support_level(self, support_level):
        """Sets the support_level of this Module.

        The support state of this module  # noqa: E501

        :param support_level: The support_level of this Module.  # noqa: E501
        :type support_level: str
        """
        if self.local_vars_configuration.client_side_validation and support_level is None:  # noqa: E501
            raise ValueError("Invalid value for `support_level`, must not be `None`")  # noqa: E501

        self._support_level = support_level

    @property
    def use_count(self):
        """Gets the use_count of this Module.  # noqa: E501

        The number of times this module is being used  # noqa: E501

        :return: The use_count of this Module.  # noqa: E501
        :rtype: int
        """
        return self._use_count

    @use_count.setter
    def use_count(self, use_count):
        """Sets the use_count of this Module.

        The number of times this module is being used  # noqa: E501

        :param use_count: The use_count of this Module.  # noqa: E501
        :type use_count: int
        """
        if self.local_vars_configuration.client_side_validation and use_count is None:  # noqa: E501
            raise ValueError("Invalid value for `use_count`, must not be `None`")  # noqa: E501

        self._use_count = use_count

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
        if not isinstance(other, Module):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Module):
            return True

        return self.to_dict() != other.to_dict()
