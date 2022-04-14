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
# Namespace: com.sun.star.text
from typing_extensions import Literal


class CharacterCompressionType:
    """
    Const Class

    These constants define character compression in Asian text.

    See Also:
        `API CharacterCompressionType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1CharacterCompressionType.html>`_
    """
    NONE: Literal[0]
    """
    the characters are uncompressed.
    """
    PUNCTUATION_ONLY: Literal[1]
    """
    only punctuation is compressed.
    """
    PUNCTUATION_AND_KANA: Literal[2]
    """
    punctuation and Japanese Kana are compressed.
    """

__all__ = ['CharacterCompressionType']
