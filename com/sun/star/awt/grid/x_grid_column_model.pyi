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
# Namespace: com.sun.star.awt.grid
from __future__ import annotations
import typing

from ...container.x_container import XContainer as XContainer_d6fb0cc6
from ...lang.x_component import XComponent as XComponent_98dc0ab5
from ...util.x_cloneable import XCloneable as XCloneable_99d00aa3
if typing.TYPE_CHECKING:
    from .x_grid_column import XGridColumn as XGridColumn_d2370c74


class XGridColumnModel(XContainer_d6fb0cc6, XComponent_98dc0ab5, XCloneable_99d00aa3):
    """
    An instance of this interface is used by the UnoControlGrid to retrieve the column structure that is displayed in the actual control.
    
    If you do not need your own model implementation, you can also use the DefaultGridColumnModel.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XGridColumnModel <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1grid_1_1XGridColumnModel.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.awt.grid.XGridColumnModel'

    def addColumn(self, column: XGridColumn_d2370c74) -> int:
        """
        Adds a column to the model.
        
        You should use the createColumn() member to create a new column. This gives implementations of the XGridColumnModel interface the possibility to provide own column implementations which extend the basic GridColumn type.
        
        As soon as the column has been inserted into the model, the model takes ownership of it. This means when the column is removed, or when the column model is disposed, the grid column is disposed as well.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def createColumn(self) -> XGridColumn_d2370c74:
        """
        creates a new column for use with the column model.
        
        The newly created column is not yet inserted into the column container, you need to call addColumn() after you initialized the column object.
        """
        ...
    def getColumn(self, index: int) -> XGridColumn_d2370c74:
        """
        Returns a specific column.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def getColumnCount(self) -> int:
        """
        Returns the number of columns.
        """
        ...
    def getColumns(self) -> typing.Tuple[XGridColumn_d2370c74, ...]:
        """
        Returns all columns of the model.
        """
        ...
    def removeColumn(self, ColumnIndex: int) -> None:
        """
        removes a column from the model
        
        The column object will be disposed upon removal.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def setDefaultColumns(self, elements: int) -> None:
        """
        Fills the model with the given number of default columns.
        
        Existing columns will be removed before adding new columns. Listeners at the column model will be notified one com.sun.star.container.XContainerListener.elementRemoved() event for each removed column, and one com.sun.star.container.XContainerListener.elementInserted() event for each insertion.
        """
        ...



