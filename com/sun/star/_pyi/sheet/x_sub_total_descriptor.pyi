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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .sub_total_column import SubTotalColumn as SubTotalColumn_d5760cbd

class XSubTotalDescriptor(XInterface_8f010a43):
    """
    provides access to the collection of subtotal fields in a subtotal descriptor.

    See Also:
        `API XSubTotalDescriptor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSubTotalDescriptor.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XSubTotalDescriptor']

    def addNew(self, aSubTotalColumns: 'typing.Tuple[SubTotalColumn_d5760cbd, ...]', nGroupColumn: int) -> None:
        """
        adds a subtotal field definition to the descriptor.
        """
        ...
    def clear(self) -> None:
        """
        removes all subtotal field definitions from the descriptor.
        """
        ...


