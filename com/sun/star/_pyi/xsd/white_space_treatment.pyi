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
# Namespace: com.sun.star.xsd
from typing_extensions import Literal


class WhiteSpaceTreatment(object):
    """
    Const

    specifies possibilities how to treat whitespace in strings

    See Also:
        `API WhiteSpaceTreatment <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1xsd_1_1WhiteSpaceTreatment.html>`_
    """
    Preserve: Literal[0]
    """
    White spaces should be preserved when processing the string.
    """
    Replace: Literal[1]
    """
    White spaces should be replaced with TODO when processing the string.
    """
    Collapse: Literal[2]
    """
    Multiple successive white spaces should be collapsed to a single white space when processing the string.
    """

