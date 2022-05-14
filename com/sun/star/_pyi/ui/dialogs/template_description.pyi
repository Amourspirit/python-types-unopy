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
# Libre Office Version: 7.3
# Namespace: com.sun.star.ui.dialogs
from typing_extensions import Literal


class TemplateDescription(object):
    """
    Const

    The implementation of a FilePicker service may support the usage of different templates.
    
    The following constants define the currently specified templates.
    
    **since**
    
        LibreOffice 5.3

    See Also:
        `API TemplateDescription <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1TemplateDescription.html>`_
    """
    FILEOPEN_SIMPLE: Literal[0]
    """
    A FileOpen dialog without any additional controls.
    """
    FILESAVE_SIMPLE: Literal[1]
    """
    A FileSave dialog without any additional controls.
    """
    FILESAVE_AUTOEXTENSION_PASSWORD: Literal[2]
    """
    A FileSave dialog with additional controls.
    """
    FILESAVE_AUTOEXTENSION_PASSWORD_FILTEROPTIONS: Literal[3]
    """
    A FileSave dialog with additional controls.
    """
    FILESAVE_AUTOEXTENSION_SELECTION: Literal[4]
    """
    A FileSave dialog with additional controls.
    """
    FILESAVE_AUTOEXTENSION_TEMPLATE: Literal[5]
    """
    A FileSave dialog with additional controls.
    """
    FILEOPEN_LINK_PREVIEW_IMAGE_TEMPLATE: Literal[6]
    """
    A FileOpen dialog with additional controls.
    """
    FILEOPEN_PLAY: Literal[7]
    """
    A FileOpen dialog with additional controls.
    """
    FILEOPEN_READONLY_VERSION: Literal[8]
    """
    A FileOpen dialog with additional controls.
    """
    FILEOPEN_LINK_PREVIEW: Literal[9]
    """
    A FileOpen dialog with additional controls.
    """
    FILESAVE_AUTOEXTENSION: Literal[10]
    """
    A FileSave dialog with additional controls.
    """
    FILEOPEN_PREVIEW: Literal[11]
    """
    A FileOpen dialog with additional controls.
    
    **since**
    
        LibreOffice 5.3
    """
    FILEOPEN_LINK_PLAY: Literal[12]
    """
    A FileOpen dialog with additional controls.
    
    **since**
    
        LibreOffice 5.3
    """
    FILEOPEN_LINK_PREVIEW_IMAGE_ANCHOR: Literal[13]
    """
    A FileOpen dialog with additional controls.
    
    **since**
    
        LibreOffice 6.1
    """

