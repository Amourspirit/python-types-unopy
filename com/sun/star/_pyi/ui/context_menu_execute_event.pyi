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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ui
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from ..awt.point import Point as Point_5fb2085e
from ..awt.x_window import XWindow as XWindow_713b0924
from ..container.x_index_container import XIndexContainer as XIndexContainer_1c040ebe
from ..view.x_selection_supplier import XSelectionSupplier as XSelectionSupplier_fed20e15


class ContextMenuExecuteEvent(object):
    """
    Struct Class

    contains all information about the requested context menu.

    See Also:
        `API ContextMenuExecuteEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ui_1_1ContextMenuExecuteEvent.html>`_
    """
    typeName: Literal['com.sun.star.ui.ContextMenuExecuteEvent']

    def __init__(self, SourceWindow: typing.Optional[XWindow_713b0924] = ..., ExecutePosition: typing.Optional[Point_5fb2085e] = ..., ActionTriggerContainer: typing.Optional[XIndexContainer_1c040ebe] = ..., Selection: typing.Optional[XSelectionSupplier_fed20e15] = ...) -> None:
        """
        Constructor

        Arguments:
            SourceWindow (XWindow, optional): SourceWindow value.
            ExecutePosition (Point, optional): ExecutePosition value.
            ActionTriggerContainer (XIndexContainer, optional): ActionTriggerContainer value.
            Selection (XSelectionSupplier, optional): Selection value.
        """
        ...


    @property
    def SourceWindow(self) -> XWindow_713b0924:
        """
        contains the window where the context menu has been requested
        """
        ...


    @property
    def ExecutePosition(self) -> Point_5fb2085e:
        """
        contains the position the context menu will be executed at.
        """
        ...


    @property
    def ActionTriggerContainer(self) -> XIndexContainer_1c040ebe:
        """
        enables the access to the menu content.
        
        The implementing object has to support the service com.sun.star.ui.ActionTriggerContainer;
        """
        ...


    @property
    def Selection(self) -> XSelectionSupplier_fed20e15:
        """
        provides the current selection inside the source window.
        """
        ...


