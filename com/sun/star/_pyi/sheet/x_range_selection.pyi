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
# Libre Office Version: 7.3
# Namespace: com.sun.star.sheet
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_range_selection_change_listener import XRangeSelectionChangeListener as XRangeSelectionChangeListener_c0021298
    from .x_range_selection_listener import XRangeSelectionListener as XRangeSelectionListener_57ef1052

class XRangeSelection(XInterface_8f010a43):
    """
    allows to let the user to select a cell range.

    See Also:
        `API XRangeSelection <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XRangeSelection.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XRangeSelection']

    def abortRangeSelection(self) -> None:
        """
        aborts the range selection.
        """
        ...
    def addRangeSelectionChangeListener(self, aListener: 'XRangeSelectionChangeListener_c0021298') -> None:
        """
        adds a listener that is notified when the selected range is changed.
        """
        ...
    def addRangeSelectionListener(self, aListener: 'XRangeSelectionListener_57ef1052') -> None:
        """
        adds a listener that is notified when range selection is completed or aborted.
        """
        ...
    def removeRangeSelectionChangeListener(self, aListener: 'XRangeSelectionChangeListener_c0021298') -> None:
        """
        removes the specified listener.
        """
        ...
    def removeRangeSelectionListener(self, aListener: 'XRangeSelectionListener_57ef1052') -> None:
        """
        removes the specified listener.
        """
        ...
    def startRangeSelection(self, aArguments: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        starts the range selection.
        """
        ...


