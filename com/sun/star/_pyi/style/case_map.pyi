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
# Namespace: com.sun.star.style
from typing_extensions import Literal


class CaseMap(object):
    """
    Const

    These constants are used to specify a case-related mapping for formatting and displaying characters.

    See Also:
        `API CaseMap <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style_1_1CaseMap.html>`_
    """
    NONE: Literal[0]
    """
    The case of the characters is unchanged.
    """
    UPPERCASE: Literal[1]
    """
    All characters are put in upper case.
    """
    LOWERCASE: Literal[2]
    """
    All characters are put in lower case.
    """
    TITLE: Literal[3]
    """
    The first character of each word is put in upper case.
    """
    SMALLCAPS: Literal[4]
    """
    All characters are put in upper case, but with a smaller font height.
    """

