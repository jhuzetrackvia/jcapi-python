# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SystemInsightsSafariExtensions(object):
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
        'author': 'str',
        'collection_time': 'str',
        'description': 'str',
        'developer_id': 'str',
        'identifier': 'str',
        'name': 'str',
        'path': 'str',
        'sdk': 'str',
        'system_id': 'str',
        'uid': 'str',
        'update_url': 'str',
        'version': 'str'
    }

    attribute_map = {
        'author': 'author',
        'collection_time': 'collection_time',
        'description': 'description',
        'developer_id': 'developer_id',
        'identifier': 'identifier',
        'name': 'name',
        'path': 'path',
        'sdk': 'sdk',
        'system_id': 'system_id',
        'uid': 'uid',
        'update_url': 'update_url',
        'version': 'version'
    }

    def __init__(self, author=None, collection_time=None, description=None, developer_id=None, identifier=None, name=None, path=None, sdk=None, system_id=None, uid=None, update_url=None, version=None):  # noqa: E501
        """SystemInsightsSafariExtensions - a model defined in Swagger"""  # noqa: E501

        self._author = None
        self._collection_time = None
        self._description = None
        self._developer_id = None
        self._identifier = None
        self._name = None
        self._path = None
        self._sdk = None
        self._system_id = None
        self._uid = None
        self._update_url = None
        self._version = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if collection_time is not None:
            self.collection_time = collection_time
        if description is not None:
            self.description = description
        if developer_id is not None:
            self.developer_id = developer_id
        if identifier is not None:
            self.identifier = identifier
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if sdk is not None:
            self.sdk = sdk
        if system_id is not None:
            self.system_id = system_id
        if uid is not None:
            self.uid = uid
        if update_url is not None:
            self.update_url = update_url
        if version is not None:
            self.version = version

    @property
    def author(self):
        """Gets the author of this SystemInsightsSafariExtensions.  # noqa: E501


        :return: The author of this SystemInsightsSafariExtensions.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this SystemInsightsSafariExtensions.


        :param author: The author of this SystemInsightsSafariExtensions.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def collection_time(self):
        """Gets the collection_time of this SystemInsightsSafariExtensions.  # noqa: E501


        :return: The collection_time of this SystemInsightsSafariExtensions.  # noqa: E501
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this SystemInsightsSafariExtensions.


        :param collection_time: The collection_time of this SystemInsightsSafariExtensions.  # noqa: E501
        :type: str
        """

        self._collection_time = collection_time

    @property
    def description(self):
        """Gets the description of this SystemInsightsSafariExtensions.  # noqa: E501


        :return: The description of this SystemInsightsSafariExtensions.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SystemInsightsSafariExtensions.


        :param description: The description of this SystemInsightsSafariExtensions.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def developer_id(self):
        """Gets the developer_id of this SystemInsightsSafariExtensions.  # noqa: E501


        :return: The developer_id of this SystemInsightsSafariExtensions.  # noqa: E501
        :rtype: str
        """
        return self._developer_id

    @developer_id.setter
    def developer_id(self, developer_id):
        """Sets the developer_id of this SystemInsightsSafariExtensions.


        :param developer_id: The developer_id of this SystemInsightsSafariExtensions.  # noqa: E501
        :type: str
        """

        self._developer_id = developer_id

    @property
    def identifier(self):
        """Gets the identifier of this SystemInsightsSafariExtensions.  # noqa: E501


        :return: The identifier of this SystemInsightsSafariExtensions.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this SystemInsightsSafariExtensions.


        :param identifier: The identifier of this SystemInsightsSafariExtensions.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this SystemInsightsSafariExtensions.  # noqa: E501


        :return: The name of this SystemInsightsSafariExtensions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemInsightsSafariExtensions.


        :param name: The name of this SystemInsightsSafariExtensions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this SystemInsightsSafariExtensions.  # noqa: E501


        :return: The path of this SystemInsightsSafariExtensions.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SystemInsightsSafariExtensions.


        :param path: The path of this SystemInsightsSafariExtensions.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def sdk(self):
        """Gets the sdk of this SystemInsightsSafariExtensions.  # noqa: E501


        :return: The sdk of this SystemInsightsSafariExtensions.  # noqa: E501
        :rtype: str
        """
        return self._sdk

    @sdk.setter
    def sdk(self, sdk):
        """Sets the sdk of this SystemInsightsSafariExtensions.


        :param sdk: The sdk of this SystemInsightsSafariExtensions.  # noqa: E501
        :type: str
        """

        self._sdk = sdk

    @property
    def system_id(self):
        """Gets the system_id of this SystemInsightsSafariExtensions.  # noqa: E501


        :return: The system_id of this SystemInsightsSafariExtensions.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemInsightsSafariExtensions.


        :param system_id: The system_id of this SystemInsightsSafariExtensions.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def uid(self):
        """Gets the uid of this SystemInsightsSafariExtensions.  # noqa: E501


        :return: The uid of this SystemInsightsSafariExtensions.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this SystemInsightsSafariExtensions.


        :param uid: The uid of this SystemInsightsSafariExtensions.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def update_url(self):
        """Gets the update_url of this SystemInsightsSafariExtensions.  # noqa: E501


        :return: The update_url of this SystemInsightsSafariExtensions.  # noqa: E501
        :rtype: str
        """
        return self._update_url

    @update_url.setter
    def update_url(self, update_url):
        """Sets the update_url of this SystemInsightsSafariExtensions.


        :param update_url: The update_url of this SystemInsightsSafariExtensions.  # noqa: E501
        :type: str
        """

        self._update_url = update_url

    @property
    def version(self):
        """Gets the version of this SystemInsightsSafariExtensions.  # noqa: E501


        :return: The version of this SystemInsightsSafariExtensions.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SystemInsightsSafariExtensions.


        :param version: The version of this SystemInsightsSafariExtensions.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(SystemInsightsSafariExtensions, dict):
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
        if not isinstance(other, SystemInsightsSafariExtensions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
