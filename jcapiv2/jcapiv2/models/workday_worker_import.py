# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The next version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings. The most recent version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WorkdayWorkerImport(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'username': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'email': 'str',
        'attributes': 'list[object]'
    }

    attribute_map = {
        'username': 'username',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'email': 'email',
        'attributes': 'attributes'
    }

    def __init__(self, username=None, firstname=None, lastname=None, email=None, attributes=None):
        """
        WorkdayWorkerImport - a model defined in Swagger
        """

        self._username = None
        self._firstname = None
        self._lastname = None
        self._email = None
        self._attributes = None

        if username is not None:
          self.username = username
        if firstname is not None:
          self.firstname = firstname
        if lastname is not None:
          self.lastname = lastname
        if email is not None:
          self.email = email
        if attributes is not None:
          self.attributes = attributes

    @property
    def username(self):
        """
        Gets the username of this WorkdayWorkerImport.

        :return: The username of this WorkdayWorkerImport.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this WorkdayWorkerImport.

        :param username: The username of this WorkdayWorkerImport.
        :type: str
        """

        self._username = username

    @property
    def firstname(self):
        """
        Gets the firstname of this WorkdayWorkerImport.

        :return: The firstname of this WorkdayWorkerImport.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this WorkdayWorkerImport.

        :param firstname: The firstname of this WorkdayWorkerImport.
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this WorkdayWorkerImport.

        :return: The lastname of this WorkdayWorkerImport.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this WorkdayWorkerImport.

        :param lastname: The lastname of this WorkdayWorkerImport.
        :type: str
        """

        self._lastname = lastname

    @property
    def email(self):
        """
        Gets the email of this WorkdayWorkerImport.

        :return: The email of this WorkdayWorkerImport.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this WorkdayWorkerImport.

        :param email: The email of this WorkdayWorkerImport.
        :type: str
        """

        self._email = email

    @property
    def attributes(self):
        """
        Gets the attributes of this WorkdayWorkerImport.

        :return: The attributes of this WorkdayWorkerImport.
        :rtype: list[object]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this WorkdayWorkerImport.

        :param attributes: The attributes of this WorkdayWorkerImport.
        :type: list[object]
        """

        self._attributes = attributes

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, WorkdayWorkerImport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other