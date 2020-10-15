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


class ContactStatusChange(object):
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
        'contact_info': 'ContactInfo',
        'endpoint': 'Endpoint'
    }

    attribute_map = {
        'contact_info': 'contact_info',
        'endpoint': 'endpoint'
    }

    def __init__(self, contact_info=None, endpoint=None, local_vars_configuration=None):  # noqa: E501
        """ContactStatusChange - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._contact_info = None
        self._endpoint = None
        self.discriminator = None

        self.contact_info = contact_info
        self.endpoint = endpoint

    @property
    def contact_info(self):
        """Gets the contact_info of this ContactStatusChange.  # noqa: E501


        :return: The contact_info of this ContactStatusChange.  # noqa: E501
        :rtype: ContactInfo
        """
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        """Sets the contact_info of this ContactStatusChange.


        :param contact_info: The contact_info of this ContactStatusChange.  # noqa: E501
        :type contact_info: ContactInfo
        """
        if self.local_vars_configuration.client_side_validation and contact_info is None:  # noqa: E501
            raise ValueError("Invalid value for `contact_info`, must not be `None`")  # noqa: E501

        self._contact_info = contact_info

    @property
    def endpoint(self):
        """Gets the endpoint of this ContactStatusChange.  # noqa: E501


        :return: The endpoint of this ContactStatusChange.  # noqa: E501
        :rtype: Endpoint
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this ContactStatusChange.


        :param endpoint: The endpoint of this ContactStatusChange.  # noqa: E501
        :type endpoint: Endpoint
        """
        if self.local_vars_configuration.client_side_validation and endpoint is None:  # noqa: E501
            raise ValueError("Invalid value for `endpoint`, must not be `None`")  # noqa: E501

        self._endpoint = endpoint

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
        if not isinstance(other, ContactStatusChange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContactStatusChange):
            return True

        return self.to_dict() != other.to_dict()
