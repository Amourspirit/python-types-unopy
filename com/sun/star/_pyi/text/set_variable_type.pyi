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
# Namespace: com.sun.star.text
from typing_extensions import Literal


class SetVariableType(object):
    """
    Const

    These constants define the type of a variable text field.

    See Also:
        `API SetVariableType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1SetVariableType.html>`_
    """
    VAR: Literal[0]
    """
    specifies a simple variable.
    """
    SEQUENCE: Literal[1]
    """
    specifies a number sequence field.
    """
    FORMULA: Literal[2]
    """
    specifies a formula field.
    """
    STRING: Literal[3]
    """
    specifies a string field.
    """

