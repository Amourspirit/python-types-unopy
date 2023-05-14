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
# Namespace: com.sun.star.frame.status
from typing_extensions import Literal
"""
Const

these constants describe a state of an ItemStatus.

**since**

    OOo 2.0

See Also:
    `API ItemState <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1frame_1_1status_1_1ItemState.html>`_
"""
UNKNOWN: Literal[0]
"""
specifies an unknown state.
"""
DISABLED: Literal[1]
"""
specifies that the property is currently disabled.
"""
READ_ONLY: Literal[2]
"""
specifies that the property is currently read-only.

Deprecated: There is no equivalent in SfxItemState anymore due to not being used, so remove for simplification reasons and to prepare rework of Item/ItemSet/ItemPool stuff.

There are only three usages of com.sun.star.frame.status.ItemState in the code which all set the internal SfxItem to SfxVoidItem when triggered, which is equivalent to state SfxItemState.DISABLED (see e.g. SfxItemSet.GetItemState), so READ_ONLY gets not used in internal handling, even when eventually existing UNO API usages hand it over the office.
"""
DONT_CARE: Literal[16]
"""
specifies that the property is currently in a don't care state.

This is normally used if a selection provides more than one state for a property at the same time.
"""
DEFAULT_VALUE: Literal[32]
"""
specifies that the property is currently in a default state.
"""
SET: Literal[64]
"""
specifies that the property is currently in a set state.
"""

