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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.ui.dialogs
from __future__ import annotations
import typing

from .x_executable_dialog import XExecutableDialog as XExecutableDialog_450f0fa1


class XFilePicker(XExecutableDialog_450f0fa1):
    """
    Specifies an interface for a FilePicker.

    See Also:
        `API XFilePicker <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1XFilePicker.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.ui.dialogs.XFilePicker'

    def getDisplayDirectory(self) -> str:
        """
        Returns the directory that the file dialog is currently showing or was last showing before closing the dialog with Ok.
        
        If the user did cancel the dialog, the returned value is undefined.
        """
        ...
    def getFiles(self) -> typing.Tuple[str, ...]:
        """
        Returns a sequence of the selected files including path information in URL format, conforming to Rfc1738.
        
        If the user closed the dialog with cancel an empty sequence will be returned.
        
        If the dialog is in execution mode and a single file is selected the complete URL of this file will be returned.
        
        If the dialog is in execution mode and the selected file name is false or any other error occurs an empty sequence will be returned.
        
        The complete path of the file or directory currently selected in URL format. This always returns only the first entry of the sequence.
        
        Notes for the implementation of a FileSave dialog:If there exists a checkbox \"Automatic File Extension\" which is checked and a valid filter is currently selected the dialog may automatically add an extension to the selected file name.
        """
        ...
    def setDefaultName(self, aName: str) -> None:
        """
        Sets the default string that appears in the file name box of a FilePicker.
        
        Specifies the default file name, displayed when the FilePicker is shown. The implementation may accept any string, and does not have to check for a valid file name or if the file really exists.
        """
        ...
    def setDisplayDirectory(self, aDirectory: str) -> None:
        """
        Sets the directory that the file dialog initially displays.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def setMultiSelectionMode(self, bMode: bool) -> None:
        """
        Enable/disable multi-selection mode.
        
        If the multi-selection mode is enabled, multiple files may be selected by the user else only one file selection at a time is possible
        
        A value of TRUE enables the multi-selection mode.
        
        A value of FALSE disables the multi-selection mode, this is the default.
        """
        ...


