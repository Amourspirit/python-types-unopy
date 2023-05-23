# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
import typing


class CharSet:
    """
    Const

    These values are used to specify the characters which are available in a font and their codes.
    
    The currently defined constants of CharSet have the same numerical values as the corresponding enum values of the C/C++ rtl_TextEncoding (from rtl/textenc.h). This correspondence is by design. Since CharSet is deprecated, however, it is not planned to add further constants to keep it in sync with rtl_TextEncoding.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API CharSet <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1CharSet.html>`_
    """
    DONTKNOW: int = ...
    """
    specifies an unknown character set.
    """
    ANSI: int = ...
    """
    specifies the ANSI character set.
    """
    MAC: int = ...
    """
    specifies the Apple Macintosh character set.
    """
    IBMPC_437: int = ...
    """
    specifies the IBM PC character set number 437.
    """
    IBMPC_850: int = ...
    """
    specifies the IBM PC character set number 850.
    """
    IBMPC_860: int = ...
    """
    specifies the IBM PC character set number 860.
    """
    IBMPC_861: int = ...
    """
    specifies the IBM PC character set number 861.
    """
    IBMPC_863: int = ...
    """
    specifies the IBM PC character set number 863.
    """
    IBMPC_865: int = ...
    """
    specifies the IBM PC character set number 865.
    """
    SYSTEM: int = ...
    """
    specifies the system character set.
    """
    SYMBOL: int = ...
    """
    specifies a set of symbols.
    """

