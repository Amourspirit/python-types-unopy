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

Text conversion options to be used with XTextConversion.

These text conversion options are usually selected by end users. The options can be combined and may be related to TextConversionType.

**since**

    OOo 1.1.2

See Also:
    `API TextConversionOption <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1TextConversionOption.html>`_
"""
NONE: Literal[0]
"""
No option.
"""
CHARACTER_BY_CHARACTER: Literal[1]
"""
Character by character conversion.
"""
IGNORE_POST_POSITIONAL_WORD: Literal[2]
"""
Ignore post-positional word for Hangul to Hanja conversion.
"""
USE_CHARACTER_VARIANTS: Literal[2]
"""
Use Taiwan, HongKong SAR, and Macao SAR character variants for Simplified to Traditional Chinese conversion.

**since**

    OOo 2.0
"""

