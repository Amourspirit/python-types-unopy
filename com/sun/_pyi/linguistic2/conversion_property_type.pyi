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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.linguistic2
from typing_extensions import Literal


class ConversionPropertyType:
    """
    Const Class

    specifies the property type of an entry in a conversion dictionary.
    
    **since**
    
        OOo 2.0

    See Also:
        `API ConversionPropertyType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1linguistic2_1_1ConversionPropertyType.html>`_
    """
    NOT_DEFINED: Literal[0]
    """
    There is no property type defined or available.
    """
    OTHER: Literal[1]
    """
    Any word that does not fit into any of the other properties.
    """
    FOREIGN: Literal[2]
    """
    A word or term that is transliterated or used from a non-Chinese language.
    """
    FIRST_NAME: Literal[3]
    """
    The first name (given name) of a person.
    """
    LAST_NAME: Literal[4]
    """
    The last name (family name) of a person.
    """
    TITLE: Literal[5]
    """
    The academic or social title of a person.
    """
    STATUS: Literal[6]
    """
    The status of a situation.
    """
    PLACE_NAME: Literal[7]
    """
    The name of a location or place.
    """
    BUSINESS: Literal[8]
    """
    The description of a business.
    """
    ADJECTIVE: Literal[9]
    """
    An adjective.
    """
    IDIOM: Literal[10]
    """
    A term that is used to literally describe a circumstance.
    """
    ABBREVIATION: Literal[11]
    """
    An abbreviation.
    """
    NUMERICAL: Literal[12]
    """
    A numeric word.
    """
    NOUN: Literal[13]
    """
    A noun.
    """
    VERB: Literal[14]
    """
    A verb.
    """
    BRAND_NAME: Literal[15]
    """
    The name of a product or a company.
    """

__all__ = ['ConversionPropertyType']
