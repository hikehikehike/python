# coding: utf-8

"""
    Weather API

     # Introduction  WeatherAPI.com provides access to weather and geo data via a JSON/XML restful API. It allows developers to create desktop, web and mobile applications using this data very easy.      We provide following data through our API:      - Real-time weather  - 14 day weather forecast  - Astronomy  - Time zone  - Location data  - Search or Autocomplete API  - NEW: Historical weather  - NEW: Future Weather (Upto 300 days ahead)  - Weather Alerts  - Air Quality Data    # Getting Started     You need to [signup](https://www.weatherapi.com/signup.aspx) and then you can find your API key under [your account](https://www.weatherapi.com/login.aspx), and start using API right away!      We have [code libraries](https://www.weatherapi.com/docs/code-libraries.aspx) for different programming languages like PHP, .net, JAVA, etc.  If you find any features missing or have any suggestions, please [contact us](https://www.weatherapi.com/contact.aspx).      # Authentication     API access to the data is protected by an API key. If at anytime, you find the API key has become vulnerable, please regenerate the key using Regenerate button next to the API key.  Authentication to the WeatherAPI.com API is provided by passing your API key as request parameter through an API .        ##  key parameter   key=YOUR_API_KEY   # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Search(object):
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
        'id': 'int',
        'name': 'str',
        'region': 'str',
        'country': 'str',
        'lat': 'float',
        'lon': 'float',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'region': 'region',
        'country': 'country',
        'lat': 'lat',
        'lon': 'lon',
        'url': 'url'
    }

    def __init__(self, id=None, name=None, region=None, country=None, lat=None, lon=None, url=None):  # noqa: E501
        """Search - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._region = None
        self._country = None
        self._lat = None
        self._lon = None
        self._url = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if country is not None:
            self.country = country
        if lat is not None:
            self.lat = lat
        if lon is not None:
            self.lon = lon
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this Search.  # noqa: E501


        :return: The id of this Search.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Search.


        :param id: The id of this Search.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Search.  # noqa: E501


        :return: The name of this Search.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Search.


        :param name: The name of this Search.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def region(self):
        """Gets the region of this Search.  # noqa: E501


        :return: The region of this Search.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Search.


        :param region: The region of this Search.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def country(self):
        """Gets the country of this Search.  # noqa: E501


        :return: The country of this Search.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Search.


        :param country: The country of this Search.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def lat(self):
        """Gets the lat of this Search.  # noqa: E501


        :return: The lat of this Search.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this Search.


        :param lat: The lat of this Search.  # noqa: E501
        :type: float
        """

        self._lat = lat

    @property
    def lon(self):
        """Gets the lon of this Search.  # noqa: E501


        :return: The lon of this Search.  # noqa: E501
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon):
        """Sets the lon of this Search.


        :param lon: The lon of this Search.  # noqa: E501
        :type: float
        """

        self._lon = lon

    @property
    def url(self):
        """Gets the url of this Search.  # noqa: E501


        :return: The url of this Search.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Search.


        :param url: The url of this Search.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(Search, dict):
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
        if not isinstance(other, Search):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
