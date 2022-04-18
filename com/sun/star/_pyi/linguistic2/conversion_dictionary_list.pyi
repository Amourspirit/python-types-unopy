# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.linguistic2
from .x_conversion_dictionary_list import XConversionDictionaryList as XConversionDictionaryList_ec3713a5

class ConversionDictionaryList(XConversionDictionaryList_ec3713a5):
    """
    Service Class

    represents a list of available conversion dictionaries.
    
    There will be only one list that may hold different types of conversion dictionaries. That is e.g. it may hold dictionaries for Korean Hangul/Hanja conversion along with ones for Chinese traditional/simplified conversion or conversion between different Indic script types.
    
    The list will be used by the text conversion service to check for user supplied text conversions.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API ConversionDictionaryList <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1linguistic2_1_1ConversionDictionaryList.html>`_
    """

