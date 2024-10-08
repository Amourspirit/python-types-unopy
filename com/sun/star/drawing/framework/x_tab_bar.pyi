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
# Namespace: com.sun.star.drawing.framework
from __future__ import annotations
import typing

from abc import ABC
if typing.TYPE_CHECKING:
    from .tab_bar_button import TabBarButton as TabBarButton_6ab41098


class XTabBar(ABC):
    """
    UI control for the selection of views in a pane.
    
    Every tab of a tab bar has, besides its localized title and help text, the URL of a view. A possible alternative would be to use a command URL instead of the view URL.
    
    In the current Impress implementation a tab bar is only used for the center pane to switch between views in the center pane. Tab bars can make sense for other panes as well, i.e. for showing either the slide sorter or the outline view in the left pane.
    
    Tab bar buttons are identified by their resource id. Note that because the resource anchors are all the same (the tab bar), it is the resource URL that really identifies a button. There can not be two buttons with the same resource id.
    
    A better place for this interface (in an extended version) would be com.sun.star.awt

    See Also:
        `API XTabBar <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1XTabBar.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.drawing.framework.XTabBar'

    def addTabBarButtonAfter(self, aButton: TabBarButton_6ab41098, aAnchor: TabBarButton_6ab41098) -> None:
        """
        Add a tab bar button to the right of another one.
        """
        ...
    def appendTabBarButton(self, aButton: TabBarButton_6ab41098) -> None:
        """
        Add a tab bar button at the right most position.
        """
        ...
    def getTabBarButtons(self) -> typing.Tuple[TabBarButton_6ab41098, ...]:
        """
        Return a sequence of all the tab bar buttons.
        
        Their order reflects the visible order in the tab bar.
        
        This method can be used when addTabBarButtonAfter() does not provide enough control as to where to insert a new button.
        """
        ...
    def hasTabBarButton(self, aButton: TabBarButton_6ab41098) -> bool:
        """
        Test whether the specified button exists in the tab bar.
        """
        ...
    def removeTabBarButton(self, aButton: TabBarButton_6ab41098) -> None:
        """
        Remove a tab bar button.
        """
        ...


