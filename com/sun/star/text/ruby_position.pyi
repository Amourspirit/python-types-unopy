# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.text
import typing


class RubyPosition:
    """
    Const

    These constants define the position of ruby text.
    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API RubyPosition <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1RubyPosition.html>`_
    """
    ABOVE: int = ...
    """
    ruby text should be above or on the right side of base text.
    """
    BELOW: int = ...
    """
    ruby text should be below or on the left side of base text.
    """
    INTER_CHARACTER: int = ...
    """
    Vertically aligned on right side of the base text in horizontal mode.
    
    This is the same as ABOVE in vertical writing mode.
    """

