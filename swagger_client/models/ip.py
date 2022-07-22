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

class Ip(object):
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
        'ip': 'str',
        'type': 'str',
        'continent_code': 'str',
        'continent_name': 'str',
        'country_code': 'str',
        'country_name': 'str',
        'is_eu': 'str',
        'geoname_id': 'int',
        'city': 'str',
        'region': 'str',
        'lat': 'float',
        'lon': 'float',
        'tz_id': 'str',
        'localtime_epoch': 'int',
        'localtime': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'type': 'type',
        'continent_code': 'continent_code',
        'continent_name': 'continent_name',
        'country_code': 'country_code',
        'country_name': 'country_name',
        'is_eu': 'is_eu',
        'geoname_id': 'geoname_id',
        'city': 'city',
        'region': 'region',
        'lat': 'lat',
        'lon': 'lon',
        'tz_id': 'tz_id',
        'localtime_epoch': 'localtime_epoch',
        'localtime': 'localtime'
    }

    def __init__(self, ip=None, type=None, continent_code=None, continent_name=None, country_code=None, country_name=None, is_eu=None, geoname_id=None, city=None, region=None, lat=None, lon=None, tz_id=None, localtime_epoch=None, localtime=None):  # noqa: E501
        """Ip - a model defined in Swagger"""  # noqa: E501
        self._ip = None
        self._type = None
        self._continent_code = None
        self._continent_name = None
        self._country_code = None
        self._country_name = None
        self._is_eu = None
        self._geoname_id = None
        self._city = None
        self._region = None
        self._lat = None
        self._lon = None
        self._tz_id = None
        self._localtime_epoch = None
        self._localtime = None
        self.discriminator = None
        if ip is not None:
            self.ip = ip
        if type is not None:
            self.type = type
        if continent_code is not None:
            self.continent_code = continent_code
        if continent_name is not None:
            self.continent_name = continent_name
        if country_code is not None:
            self.country_code = country_code
        if country_name is not None:
            self.country_name = country_name
        if is_eu is not None:
            self.is_eu = is_eu
        if geoname_id is not None:
            self.geoname_id = geoname_id
        if city is not None:
            self.city = city
        if region is not None:
            self.region = region
        if lat is not None:
            self.lat = lat
        if lon is not None:
            self.lon = lon
        if tz_id is not None:
            self.tz_id = tz_id
        if localtime_epoch is not None:
            self.localtime_epoch = localtime_epoch
        if localtime is not None:
            self.localtime = localtime

    @property
    def ip(self):
        """Gets the ip of this Ip.  # noqa: E501


        :return: The ip of this Ip.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Ip.


        :param ip: The ip of this Ip.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def type(self):
        """Gets the type of this Ip.  # noqa: E501


        :return: The type of this Ip.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Ip.


        :param type: The type of this Ip.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def continent_code(self):
        """Gets the continent_code of this Ip.  # noqa: E501


        :return: The continent_code of this Ip.  # noqa: E501
        :rtype: str
        """
        return self._continent_code

    @continent_code.setter
    def continent_code(self, continent_code):
        """Sets the continent_code of this Ip.


        :param continent_code: The continent_code of this Ip.  # noqa: E501
        :type: str
        """

        self._continent_code = continent_code

    @property
    def continent_name(self):
        """Gets the continent_name of this Ip.  # noqa: E501


        :return: The continent_name of this Ip.  # noqa: E501
        :rtype: str
        """
        return self._continent_name

    @continent_name.setter
    def continent_name(self, continent_name):
        """Sets the continent_name of this Ip.


        :param continent_name: The continent_name of this Ip.  # noqa: E501
        :type: str
        """

        self._continent_name = continent_name

    @property
    def country_code(self):
        """Gets the country_code of this Ip.  # noqa: E501


        :return: The country_code of this Ip.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Ip.


        :param country_code: The country_code of this Ip.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def country_name(self):
        """Gets the country_name of this Ip.  # noqa: E501


        :return: The country_name of this Ip.  # noqa: E501
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this Ip.


        :param country_name: The country_name of this Ip.  # noqa: E501
        :type: str
        """

        self._country_name = country_name

    @property
    def is_eu(self):
        """Gets the is_eu of this Ip.  # noqa: E501


        :return: The is_eu of this Ip.  # noqa: E501
        :rtype: str
        """
        return self._is_eu

    @is_eu.setter
    def is_eu(self, is_eu):
        """Sets the is_eu of this Ip.


        :param is_eu: The is_eu of this Ip.  # noqa: E501
        :type: str
        """

        self._is_eu = is_eu

    @property
    def geoname_id(self):
        """Gets the geoname_id of this Ip.  # noqa: E501


        :return: The geoname_id of this Ip.  # noqa: E501
        :rtype: int
        """
        return self._geoname_id

    @geoname_id.setter
    def geoname_id(self, geoname_id):
        """Sets the geoname_id of this Ip.


        :param geoname_id: The geoname_id of this Ip.  # noqa: E501
        :type: int
        """

        self._geoname_id = geoname_id

    @property
    def city(self):
        """Gets the city of this Ip.  # noqa: E501


        :return: The city of this Ip.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Ip.


        :param city: The city of this Ip.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def region(self):
        """Gets the region of this Ip.  # noqa: E501


        :return: The region of this Ip.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Ip.


        :param region: The region of this Ip.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def lat(self):
        """Gets the lat of this Ip.  # noqa: E501


        :return: The lat of this Ip.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this Ip.


        :param lat: The lat of this Ip.  # noqa: E501
        :type: float
        """

        self._lat = lat

    @property
    def lon(self):
        """Gets the lon of this Ip.  # noqa: E501


        :return: The lon of this Ip.  # noqa: E501
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon):
        """Sets the lon of this Ip.


        :param lon: The lon of this Ip.  # noqa: E501
        :type: float
        """

        self._lon = lon

    @property
    def tz_id(self):
        """Gets the tz_id of this Ip.  # noqa: E501


        :return: The tz_id of this Ip.  # noqa: E501
        :rtype: str
        """
        return self._tz_id

    @tz_id.setter
    def tz_id(self, tz_id):
        """Sets the tz_id of this Ip.


        :param tz_id: The tz_id of this Ip.  # noqa: E501
        :type: str
        """

        self._tz_id = tz_id

    @property
    def localtime_epoch(self):
        """Gets the localtime_epoch of this Ip.  # noqa: E501


        :return: The localtime_epoch of this Ip.  # noqa: E501
        :rtype: int
        """
        return self._localtime_epoch

    @localtime_epoch.setter
    def localtime_epoch(self, localtime_epoch):
        """Sets the localtime_epoch of this Ip.


        :param localtime_epoch: The localtime_epoch of this Ip.  # noqa: E501
        :type: int
        """

        self._localtime_epoch = localtime_epoch

    @property
    def localtime(self):
        """Gets the localtime of this Ip.  # noqa: E501


        :return: The localtime of this Ip.  # noqa: E501
        :rtype: str
        """
        return self._localtime

    @localtime.setter
    def localtime(self, localtime):
        """Sets the localtime of this Ip.


        :param localtime: The localtime of this Ip.  # noqa: E501
        :type: str
        """

        self._localtime = localtime

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
        if issubclass(Ip, dict):
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
        if not isinstance(other, Ip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
