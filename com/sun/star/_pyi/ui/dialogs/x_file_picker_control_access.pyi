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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.ui.dialogs
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .x_file_picker import XFilePicker as XFilePicker_ec3e0d2d


class XFilePickerControlAccess(XFilePicker_ec3e0d2d):
    """
    Provides access to the controls of a FilePicker.
    
    A FilePicker may contain additional elements according to the needs of the different applications. These additional elements can be addressed by this interface.

    See Also:
        `API XFilePickerControlAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1XFilePickerControlAccess.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ui.dialogs.XFilePickerControlAccess']

    def enableControl(self, ControlId: int, bEnable: bool) -> None:
        """
        Enables or disables a control.
        
        If TRUE the specified control will be enabled.
        
        If FALSE the specified control will be disabled.
        """
        ...
    def getLabel(self, aControlId: int) -> str:
        """
        Returns the label of the specified element.
        """
        ...
    def getValue(self, aControlId: int, aControlAction: int) -> typing.Any:
        """
        Get the value of an additional element within a FilePicker.
        """
        ...
    def setLabel(self, aControlId: int, aLabel: str) -> None:
        """
        Set the label of the specified element.
        
        If the specified element doesn't support setting a label, this method has no effect.
        """
        ...
    def setValue(self, ControlId: int, aControlAction: int, aValue: typing.Any) -> None:
        """
        Set the value of an additional element within a FilePicker.
        """
        ...


