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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
from typing_extensions import Literal


class ExternalLinkType(object):
    """
    Const

    Constants designating the link type in ExternalLinkInfo, used with FormulaParser.ExternalLinks.
    
    **since**
    
        OOo 3.1

    See Also:
        `API ExternalLinkType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1ExternalLinkType.html>`_
    """
    UNKNOWN: Literal[0]
    """
    Unknown element type.
    """
    DOCUMENT: Literal[1]
    """
    URL of an external document.
    """
    DDE: Literal[2]
    """
    DDE link.
    """
    SELF: Literal[3]
    """
    Reference to the own document.
    """
    SPECIAL: Literal[4]
    """
    For special use cases.
    
    Behaviour is dependent on the implementation of the formula parser.
    """

