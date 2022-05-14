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
# Libre Office Version: 7.3
# Namespace: com.sun.star.text
from typing_extensions import Literal


class TimeDisplayFormat(object):
    """
    Const

    These constants define how a time field is formatted before it is displayed.
    
    The format may also depend on the system or document locale.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API TimeDisplayFormat <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1TimeDisplayFormat.html>`_
    """
    STANDARD: Literal[0]
    """
    the system standard
    """
    HHMM: Literal[1]
    """
    13:49
    """
    HHMMSS: Literal[2]
    """
    13:49:20
    """
    HHMMSS00: Literal[3]
    """
    13:49:20.30
    """
    HHMMAMPM: Literal[4]
    """
    01:49
    """
    HHMMSSAMPM: Literal[5]
    """
    01:49:20
    """
    HHMMSS00AMPM: Literal[6]
    """
    01:49:20.30
    """

