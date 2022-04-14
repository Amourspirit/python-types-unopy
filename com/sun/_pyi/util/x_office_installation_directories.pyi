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
# Namespace: com.sun.star.util
from typing_extensions import Literal
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XOfficeInstallationDirectories(XInterface_8f010a43):
    """
    encapsulates access to the current office installation directory and office user data directory, provides functionality to create URLs containing relocatable (not absolute) references to the current office installation directory and user data directory and vice versa.
    
    This functionality is useful when data containing references to the current office installation directory must be made persistent and re-read later. In many cases, storing the reference directly would destroy the relocatability of an office installation.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XOfficeInstallationDirectories <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XOfficeInstallationDirectories.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.util.XOfficeInstallationDirectories']

    def getOfficeInstallationDirectoryURL(self) -> str:
        """
        returns the absolute URL containing the directory of the current office installation (for example \"file:///opt/LibreOffice\")
        """
    def getOfficeUserDataDirectoryURL(self) -> str:
        """
        returns the absolute URL containing the directory where the current office installation expects its user data (for example \"file:///home/kso/.config/libreoffice/4\")
        """
    def makeAbsoluteURL(self, URL: str) -> str:
        """
        the counterpart of makeRelocatableURL.
        
        If the given URL contains a placeholder for an absolute reference to the current office installation directory or for the office user data directory, that was created using makeRelocatableURL, the respective placeholder will be replaced by an absolute reference to the current office installation directory or office user data directory.
        """
    def makeRelocatableURL(self, URL: str) -> str:
        """
        calculates a relocatable URL from the given URL.
        
        If the given URL contains an absolute reference to the current office installation directory or office user data directory, this method will replace the absolute reference by an opaque placeholder string. makeRelocatableURL must be used in order to re-replace the placeholder by an absolute reference.
        """

__all__ = ['XOfficeInstallationDirectories']

