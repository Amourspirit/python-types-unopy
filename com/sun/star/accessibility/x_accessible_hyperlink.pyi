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
# Namespace: com.sun.star.accessibility
from __future__ import annotations
import typing

from .x_accessible_action import XAccessibleAction as XAccessibleAction_7ccc1114


class XAccessibleHyperlink(XAccessibleAction_7ccc1114):
    """
    Implement this interface to represent a hyperlink or a group of hyperlinks.
    
    Single hyperlinks correspond to simple <a href> tags. Groups of hyperlinks are contained in client side image maps. Linked objects and anchors are implementation dependent. This interface inherits the XAccessibleAction interface. Especially that interface's XAccessibleAction.getActionCount() method is needed to obtain a maximum value for the indices passed to the XAccessibleHyperlink.getAccessibleActionAnchor() and XAccessibleHyperlink.getAccessibleActionObject() methods.
    
    Furthermore, the object that implements this interface has to be connected implicitly or explicitly with an object that implements the XAccessibleText interface. The XAccessibleHyperlink.getStartIndex() and XAccessibleHyperlink.getEndIndex() methods return indices with respect to the text exposed by that interface.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessibleHyperlink <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleHyperlink.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.accessibility.XAccessibleHyperlink'

    def getAccessibleActionAnchor(self, nIndex: int) -> typing.Any:
        """
        Returns an object that represents the link anchor, as appropriate for that link.
        
        For an HTML link for example, this method would return the string enclosed by the &lt&a href> tag.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def getAccessibleActionObject(self, nIndex: int) -> typing.Any:
        """
        Returns an object that represents the link anchor, as appropriate for that link.
        
        For an HTML link for example, this method would return the URL of the &lt&a href> tag.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def getEndIndex(self) -> int:
        """
        Returns the index at which the textual representation of the hyperlink (group) ends.
        
        The returned value relates to the XAccessibleText interface that owns this hyperlink.
        """
        ...
    def getStartIndex(self) -> int:
        """
        Returns the index at which the textual representation of the hyperlink (group) starts.
        
        The returned value relates to the XAccessibleText interface that owns this hyperlink.
        """
        ...
    def isValid(self) -> bool:
        """
        Returns whether the document referenced by this links is still valid.
        
        This is a volatile state that may change without further warning like e.g. sending an appropriate event.
        """
        ...



