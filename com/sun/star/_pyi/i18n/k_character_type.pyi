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
# Namespace: com.sun.star.i18n
from typing_extensions import Literal
"""
Const

Constants to identify the character type.

Returned by XCharacterClassification.getCharacterType() and XCharacterClassification.getStringType()

See Also:
    `API KCharacterType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1KCharacterType.html>`_
"""
DIGIT: Literal[1]
"""
digit
"""
UPPER: Literal[2]
"""
upper case alpha letter
"""
LOWER: Literal[4]
"""
lower case alpha letter
"""
TITLE_CASE: Literal[8]
"""
title case alpha letter
"""
ALPHA: Literal[14]
"""
any alpha, ALPHA = UPPER | LOWER | TITLE_CASE
"""
CONTROL: Literal[16]
"""
control character
"""
PRINTABLE: Literal[32]
"""
printable character
"""
BASE_FORM: Literal[64]
"""
base form
"""
LETTER: Literal[128]
"""
any UnicodeType...._LETTER.

Note that a LETTER must not necessarily be ALPHA
"""

