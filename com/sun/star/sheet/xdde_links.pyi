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
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing

from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
if typing.TYPE_CHECKING:
    from .xdde_link import XDDELink as XDDELink_8cc609d4
    from com.sun.star.sheet.DDELinkMode import DDELinkModeProto  # type: ignore


class XDDELinks(XNameAccess_e2ab0cf6):
    """
    provides a method to add a DDE link to a spreadsheet.
    
    **since**
    
        OOo 3.0

    See Also:
        `API XDDELinks <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XDDELinks.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sheet.XDDELinks'

    def addDDELink(self, aApplication: str, aTopic: str, aItem: str, nMode: DDELinkModeProto) -> XDDELink_8cc609d4:
        """
        adds a DDE link to the spreadsheet without updating it.
        
        If a DDE link with the specified parameters already exists, the existing DDE link will be returned. Otherwise a new DDE link will be created.
        """
        ...
