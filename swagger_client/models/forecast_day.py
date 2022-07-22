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

class ForecastDay(object):
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
        'maxtemp_c': 'float',
        'maxtemp_f': 'float',
        'mintemp_c': 'float',
        'mintemp_f': 'float',
        'avgtemp_c': 'float',
        'avgtemp_f': 'float',
        'maxwind_mph': 'float',
        'maxwind_kph': 'float',
        'totalprecip_mm': 'int',
        'totalprecip_in': 'int',
        'avgvis_km': 'int',
        'avgvis_miles': 'int',
        'avghumidity': 'int',
        'daily_will_it_rain': 'int',
        'daily_chance_of_rain': 'int',
        'daily_will_it_snow': 'int',
        'daily_chance_of_snow': 'int',
        'condition': 'ForecastDayCondition',
        'uv': 'int'
    }

    attribute_map = {
        'maxtemp_c': 'maxtemp_c',
        'maxtemp_f': 'maxtemp_f',
        'mintemp_c': 'mintemp_c',
        'mintemp_f': 'mintemp_f',
        'avgtemp_c': 'avgtemp_c',
        'avgtemp_f': 'avgtemp_f',
        'maxwind_mph': 'maxwind_mph',
        'maxwind_kph': 'maxwind_kph',
        'totalprecip_mm': 'totalprecip_mm',
        'totalprecip_in': 'totalprecip_in',
        'avgvis_km': 'avgvis_km',
        'avgvis_miles': 'avgvis_miles',
        'avghumidity': 'avghumidity',
        'daily_will_it_rain': 'daily_will_it_rain',
        'daily_chance_of_rain': 'daily_chance_of_rain',
        'daily_will_it_snow': 'daily_will_it_snow',
        'daily_chance_of_snow': 'daily_chance_of_snow',
        'condition': 'condition',
        'uv': 'uv'
    }

    def __init__(self, maxtemp_c=None, maxtemp_f=None, mintemp_c=None, mintemp_f=None, avgtemp_c=None, avgtemp_f=None, maxwind_mph=None, maxwind_kph=None, totalprecip_mm=None, totalprecip_in=None, avgvis_km=None, avgvis_miles=None, avghumidity=None, daily_will_it_rain=None, daily_chance_of_rain=None, daily_will_it_snow=None, daily_chance_of_snow=None, condition=None, uv=None):  # noqa: E501
        """ForecastDay - a model defined in Swagger"""  # noqa: E501
        self._maxtemp_c = None
        self._maxtemp_f = None
        self._mintemp_c = None
        self._mintemp_f = None
        self._avgtemp_c = None
        self._avgtemp_f = None
        self._maxwind_mph = None
        self._maxwind_kph = None
        self._totalprecip_mm = None
        self._totalprecip_in = None
        self._avgvis_km = None
        self._avgvis_miles = None
        self._avghumidity = None
        self._daily_will_it_rain = None
        self._daily_chance_of_rain = None
        self._daily_will_it_snow = None
        self._daily_chance_of_snow = None
        self._condition = None
        self._uv = None
        self.discriminator = None
        if maxtemp_c is not None:
            self.maxtemp_c = maxtemp_c
        if maxtemp_f is not None:
            self.maxtemp_f = maxtemp_f
        if mintemp_c is not None:
            self.mintemp_c = mintemp_c
        if mintemp_f is not None:
            self.mintemp_f = mintemp_f
        if avgtemp_c is not None:
            self.avgtemp_c = avgtemp_c
        if avgtemp_f is not None:
            self.avgtemp_f = avgtemp_f
        if maxwind_mph is not None:
            self.maxwind_mph = maxwind_mph
        if maxwind_kph is not None:
            self.maxwind_kph = maxwind_kph
        if totalprecip_mm is not None:
            self.totalprecip_mm = totalprecip_mm
        if totalprecip_in is not None:
            self.totalprecip_in = totalprecip_in
        if avgvis_km is not None:
            self.avgvis_km = avgvis_km
        if avgvis_miles is not None:
            self.avgvis_miles = avgvis_miles
        if avghumidity is not None:
            self.avghumidity = avghumidity
        if daily_will_it_rain is not None:
            self.daily_will_it_rain = daily_will_it_rain
        if daily_chance_of_rain is not None:
            self.daily_chance_of_rain = daily_chance_of_rain
        if daily_will_it_snow is not None:
            self.daily_will_it_snow = daily_will_it_snow
        if daily_chance_of_snow is not None:
            self.daily_chance_of_snow = daily_chance_of_snow
        if condition is not None:
            self.condition = condition
        if uv is not None:
            self.uv = uv

    @property
    def maxtemp_c(self):
        """Gets the maxtemp_c of this ForecastDay.  # noqa: E501


        :return: The maxtemp_c of this ForecastDay.  # noqa: E501
        :rtype: float
        """
        return self._maxtemp_c

    @maxtemp_c.setter
    def maxtemp_c(self, maxtemp_c):
        """Sets the maxtemp_c of this ForecastDay.


        :param maxtemp_c: The maxtemp_c of this ForecastDay.  # noqa: E501
        :type: float
        """

        self._maxtemp_c = maxtemp_c

    @property
    def maxtemp_f(self):
        """Gets the maxtemp_f of this ForecastDay.  # noqa: E501


        :return: The maxtemp_f of this ForecastDay.  # noqa: E501
        :rtype: float
        """
        return self._maxtemp_f

    @maxtemp_f.setter
    def maxtemp_f(self, maxtemp_f):
        """Sets the maxtemp_f of this ForecastDay.


        :param maxtemp_f: The maxtemp_f of this ForecastDay.  # noqa: E501
        :type: float
        """

        self._maxtemp_f = maxtemp_f

    @property
    def mintemp_c(self):
        """Gets the mintemp_c of this ForecastDay.  # noqa: E501


        :return: The mintemp_c of this ForecastDay.  # noqa: E501
        :rtype: float
        """
        return self._mintemp_c

    @mintemp_c.setter
    def mintemp_c(self, mintemp_c):
        """Sets the mintemp_c of this ForecastDay.


        :param mintemp_c: The mintemp_c of this ForecastDay.  # noqa: E501
        :type: float
        """

        self._mintemp_c = mintemp_c

    @property
    def mintemp_f(self):
        """Gets the mintemp_f of this ForecastDay.  # noqa: E501


        :return: The mintemp_f of this ForecastDay.  # noqa: E501
        :rtype: float
        """
        return self._mintemp_f

    @mintemp_f.setter
    def mintemp_f(self, mintemp_f):
        """Sets the mintemp_f of this ForecastDay.


        :param mintemp_f: The mintemp_f of this ForecastDay.  # noqa: E501
        :type: float
        """

        self._mintemp_f = mintemp_f

    @property
    def avgtemp_c(self):
        """Gets the avgtemp_c of this ForecastDay.  # noqa: E501


        :return: The avgtemp_c of this ForecastDay.  # noqa: E501
        :rtype: float
        """
        return self._avgtemp_c

    @avgtemp_c.setter
    def avgtemp_c(self, avgtemp_c):
        """Sets the avgtemp_c of this ForecastDay.


        :param avgtemp_c: The avgtemp_c of this ForecastDay.  # noqa: E501
        :type: float
        """

        self._avgtemp_c = avgtemp_c

    @property
    def avgtemp_f(self):
        """Gets the avgtemp_f of this ForecastDay.  # noqa: E501


        :return: The avgtemp_f of this ForecastDay.  # noqa: E501
        :rtype: float
        """
        return self._avgtemp_f

    @avgtemp_f.setter
    def avgtemp_f(self, avgtemp_f):
        """Sets the avgtemp_f of this ForecastDay.


        :param avgtemp_f: The avgtemp_f of this ForecastDay.  # noqa: E501
        :type: float
        """

        self._avgtemp_f = avgtemp_f

    @property
    def maxwind_mph(self):
        """Gets the maxwind_mph of this ForecastDay.  # noqa: E501


        :return: The maxwind_mph of this ForecastDay.  # noqa: E501
        :rtype: float
        """
        return self._maxwind_mph

    @maxwind_mph.setter
    def maxwind_mph(self, maxwind_mph):
        """Sets the maxwind_mph of this ForecastDay.


        :param maxwind_mph: The maxwind_mph of this ForecastDay.  # noqa: E501
        :type: float
        """

        self._maxwind_mph = maxwind_mph

    @property
    def maxwind_kph(self):
        """Gets the maxwind_kph of this ForecastDay.  # noqa: E501


        :return: The maxwind_kph of this ForecastDay.  # noqa: E501
        :rtype: float
        """
        return self._maxwind_kph

    @maxwind_kph.setter
    def maxwind_kph(self, maxwind_kph):
        """Sets the maxwind_kph of this ForecastDay.


        :param maxwind_kph: The maxwind_kph of this ForecastDay.  # noqa: E501
        :type: float
        """

        self._maxwind_kph = maxwind_kph

    @property
    def totalprecip_mm(self):
        """Gets the totalprecip_mm of this ForecastDay.  # noqa: E501


        :return: The totalprecip_mm of this ForecastDay.  # noqa: E501
        :rtype: int
        """
        return self._totalprecip_mm

    @totalprecip_mm.setter
    def totalprecip_mm(self, totalprecip_mm):
        """Sets the totalprecip_mm of this ForecastDay.


        :param totalprecip_mm: The totalprecip_mm of this ForecastDay.  # noqa: E501
        :type: int
        """

        self._totalprecip_mm = totalprecip_mm

    @property
    def totalprecip_in(self):
        """Gets the totalprecip_in of this ForecastDay.  # noqa: E501


        :return: The totalprecip_in of this ForecastDay.  # noqa: E501
        :rtype: int
        """
        return self._totalprecip_in

    @totalprecip_in.setter
    def totalprecip_in(self, totalprecip_in):
        """Sets the totalprecip_in of this ForecastDay.


        :param totalprecip_in: The totalprecip_in of this ForecastDay.  # noqa: E501
        :type: int
        """

        self._totalprecip_in = totalprecip_in

    @property
    def avgvis_km(self):
        """Gets the avgvis_km of this ForecastDay.  # noqa: E501


        :return: The avgvis_km of this ForecastDay.  # noqa: E501
        :rtype: int
        """
        return self._avgvis_km

    @avgvis_km.setter
    def avgvis_km(self, avgvis_km):
        """Sets the avgvis_km of this ForecastDay.


        :param avgvis_km: The avgvis_km of this ForecastDay.  # noqa: E501
        :type: int
        """

        self._avgvis_km = avgvis_km

    @property
    def avgvis_miles(self):
        """Gets the avgvis_miles of this ForecastDay.  # noqa: E501


        :return: The avgvis_miles of this ForecastDay.  # noqa: E501
        :rtype: int
        """
        return self._avgvis_miles

    @avgvis_miles.setter
    def avgvis_miles(self, avgvis_miles):
        """Sets the avgvis_miles of this ForecastDay.


        :param avgvis_miles: The avgvis_miles of this ForecastDay.  # noqa: E501
        :type: int
        """

        self._avgvis_miles = avgvis_miles

    @property
    def avghumidity(self):
        """Gets the avghumidity of this ForecastDay.  # noqa: E501


        :return: The avghumidity of this ForecastDay.  # noqa: E501
        :rtype: int
        """
        return self._avghumidity

    @avghumidity.setter
    def avghumidity(self, avghumidity):
        """Sets the avghumidity of this ForecastDay.


        :param avghumidity: The avghumidity of this ForecastDay.  # noqa: E501
        :type: int
        """

        self._avghumidity = avghumidity

    @property
    def daily_will_it_rain(self):
        """Gets the daily_will_it_rain of this ForecastDay.  # noqa: E501


        :return: The daily_will_it_rain of this ForecastDay.  # noqa: E501
        :rtype: int
        """
        return self._daily_will_it_rain

    @daily_will_it_rain.setter
    def daily_will_it_rain(self, daily_will_it_rain):
        """Sets the daily_will_it_rain of this ForecastDay.


        :param daily_will_it_rain: The daily_will_it_rain of this ForecastDay.  # noqa: E501
        :type: int
        """

        self._daily_will_it_rain = daily_will_it_rain

    @property
    def daily_chance_of_rain(self):
        """Gets the daily_chance_of_rain of this ForecastDay.  # noqa: E501


        :return: The daily_chance_of_rain of this ForecastDay.  # noqa: E501
        :rtype: int
        """
        return self._daily_chance_of_rain

    @daily_chance_of_rain.setter
    def daily_chance_of_rain(self, daily_chance_of_rain):
        """Sets the daily_chance_of_rain of this ForecastDay.


        :param daily_chance_of_rain: The daily_chance_of_rain of this ForecastDay.  # noqa: E501
        :type: int
        """

        self._daily_chance_of_rain = daily_chance_of_rain

    @property
    def daily_will_it_snow(self):
        """Gets the daily_will_it_snow of this ForecastDay.  # noqa: E501


        :return: The daily_will_it_snow of this ForecastDay.  # noqa: E501
        :rtype: int
        """
        return self._daily_will_it_snow

    @daily_will_it_snow.setter
    def daily_will_it_snow(self, daily_will_it_snow):
        """Sets the daily_will_it_snow of this ForecastDay.


        :param daily_will_it_snow: The daily_will_it_snow of this ForecastDay.  # noqa: E501
        :type: int
        """

        self._daily_will_it_snow = daily_will_it_snow

    @property
    def daily_chance_of_snow(self):
        """Gets the daily_chance_of_snow of this ForecastDay.  # noqa: E501


        :return: The daily_chance_of_snow of this ForecastDay.  # noqa: E501
        :rtype: int
        """
        return self._daily_chance_of_snow

    @daily_chance_of_snow.setter
    def daily_chance_of_snow(self, daily_chance_of_snow):
        """Sets the daily_chance_of_snow of this ForecastDay.


        :param daily_chance_of_snow: The daily_chance_of_snow of this ForecastDay.  # noqa: E501
        :type: int
        """

        self._daily_chance_of_snow = daily_chance_of_snow

    @property
    def condition(self):
        """Gets the condition of this ForecastDay.  # noqa: E501


        :return: The condition of this ForecastDay.  # noqa: E501
        :rtype: ForecastDayCondition
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this ForecastDay.


        :param condition: The condition of this ForecastDay.  # noqa: E501
        :type: ForecastDayCondition
        """

        self._condition = condition

    @property
    def uv(self):
        """Gets the uv of this ForecastDay.  # noqa: E501


        :return: The uv of this ForecastDay.  # noqa: E501
        :rtype: int
        """
        return self._uv

    @uv.setter
    def uv(self, uv):
        """Sets the uv of this ForecastDay.


        :param uv: The uv of this ForecastDay.  # noqa: E501
        :type: int
        """

        self._uv = uv

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
        if issubclass(ForecastDay, dict):
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
        if not isinstance(other, ForecastDay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
