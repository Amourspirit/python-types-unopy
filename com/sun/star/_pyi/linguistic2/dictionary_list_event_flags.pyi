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
# Namespace: com.sun.star.linguistic2
from typing_extensions import Literal


class DictionaryListEventFlags(object):
    """
    Const

    constants representing a single dictionary-list event.
    
    These flags define the possible types for a dictionary-list event.

    See Also:
        `API DictionaryListEventFlags <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1linguistic2_1_1DictionaryListEventFlags.html>`_
    """
    ADD_POS_ENTRY: Literal[1]
    """
    A positive entry was added to a dictionary from the dictionary list.
    """
    DEL_POS_ENTRY: Literal[2]
    """
    A positive entry was deleted from a dictionary of the dictionary-list or a dictionary with positive entries was cleared.
    """
    ADD_NEG_ENTRY: Literal[4]
    """
    A negative entry was added to a dictionary from the dictionary-list.
    """
    DEL_NEG_ENTRY: Literal[8]
    """
    A negative entry was deleted from a dictionary of the dictionary-list or a dictionary with negative entries was cleared.
    """
    ACTIVATE_POS_DIC: Literal[16]
    """
    A dictionary with positive entries was activated or has changed its language.
    """
    DEACTIVATE_POS_DIC: Literal[32]
    """
    A dictionary with positive entries was deactivated or has changed its language.
    """
    ACTIVATE_NEG_DIC: Literal[64]
    """
    A dictionary with negative entries was activated or has changed its language.
    """
    DEACTIVATE_NEG_DIC: Literal[128]
    """
    A dictionary with negative entries was deactivated or has changed its language.
    """

