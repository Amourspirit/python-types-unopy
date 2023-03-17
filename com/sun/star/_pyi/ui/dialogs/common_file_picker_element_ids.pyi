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
# Libre Office Version: 7.4
# Namespace: com.sun.star.ui.dialogs
from typing_extensions import Literal


class CommonFilePickerElementIds(object):
    """
    Const

    These constants are used to specify common controls of a FilePicker dialog.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API CommonFilePickerElementIds <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1CommonFilePickerElementIds.html>`_
    """
    PUSHBUTTON_OK: Literal[1]
    """
    The control id of the OK button.
    """
    PUSHBUTTON_CANCEL: Literal[2]
    """
    The control id of the Cancel button.
    """
    LISTBOX_FILTER: Literal[3]
    """
    The filter listbox of a FilePicker dialog.
    """
    CONTROL_FILEVIEW: Literal[4]
    """
    Is used to refer to the file view of the file picker.
    
    This view shows the list of all files/folders in the currently selected folder.
    """
    EDIT_FILEURL: Literal[5]
    """
    Is used to refer to the edit line where a file or path can be entered by the user.
    """
    LISTBOX_FILTER_LABEL: Literal[6]
    """
    The label of the filter listbox of a FilePicker dialog.
    
    **since**
    
        OOo 1.1.2
    """
    EDIT_FILEURL_LABEL: Literal[7]
    """
    The label of the file name listbox of a FilePicker dialog.
    
    **since**
    
        OOo 1.1.2
    """

