# coding: utf-8

"""
    Monitor API

    An API for an integrator to access the features of DocuSign Monitor  # noqa: E501

    OpenAPI spec version: v2.0
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_monitor.client.configuration import Configuration


class DataSet(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'end_cursor': 'str',
        'data': 'list[object]'
    }

    attribute_map = {
        'end_cursor': 'endCursor',
        'data': 'data'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DataSet - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end_cursor = None
        self._data = None
        self.discriminator = None

        setattr(self, "_{}".format('end_cursor'), kwargs.get('end_cursor', None))
        setattr(self, "_{}".format('data'), kwargs.get('data', None))

    @property
    def end_cursor(self):
        """Gets the end_cursor of this DataSet.  # noqa: E501

          # noqa: E501

        :return: The end_cursor of this DataSet.  # noqa: E501
        :rtype: str
        """
        return self._end_cursor

    @end_cursor.setter
    def end_cursor(self, end_cursor):
        """Sets the end_cursor of this DataSet.

          # noqa: E501

        :param end_cursor: The end_cursor of this DataSet.  # noqa: E501
        :type: str
        """

        self._end_cursor = end_cursor

    @property
    def data(self):
        """Gets the data of this DataSet.  # noqa: E501

          # noqa: E501

        :return: The data of this DataSet.  # noqa: E501
        :rtype: list[object]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DataSet.

          # noqa: E501

        :param data: The data of this DataSet.  # noqa: E501
        :type: list[object]
        """

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DataSet, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DataSet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataSet):
            return True

        return self.to_dict() != other.to_dict()
