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
# Namespace: com.sun.star.sdbc
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XResultSetUpdate(XInterface_8f010a43):
    """
    provides the possibility to write changes made on a result set back to database.

    See Also:
        `API XResultSetUpdate <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XResultSetUpdate.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sdbc.XResultSetUpdate'

    def cancelRowUpdates(self) -> None:
        """
        cancels the updates made to a row.
        
        This method may be called after calling an updateXXX method(s) and before calling com.sun.star.sdbc.XResultSetUpdate.updateRow() to rollback the updates made to a row. If no updates have been made or updateRow has already been called, then this method has no effect.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def deleteRow(self) -> None:
        """
        deletes the current row from the result set and the underlying database.
        
        Cannot be called when on the insert row.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def insertRow(self) -> None:
        """
        inserts the contents of the insert row into the result set and the database.
        
        Must be on the insert row when this method is called.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def moveToCurrentRow(self) -> None:
        """
        moves the cursor to the remembered cursor position, usually the current row.
        
        This method has no effect if the cursor is not on the insert row.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def moveToInsertRow(self) -> None:
        """
        moves the cursor to the insert row.
        
        The current cursor position is remembered while the cursor is positioned on the insert row.
        
        The insert row is a special row associated with an updatable result set. It is essentially a buffer where a new row may be constructed by calling the updateXXX methods prior to inserting the row into the result set.
        
        Only the updateXXX , getXXX , and com.sun.star.sdbc.XResultSetUpdate.insertRow() methods may be called when the cursor is on the insert row. All of the columns in a result set must be given a value each time this method is called before calling insertRow . The method updateXXX must be called before a getXXX method can be called on a column value.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def updateRow(self) -> None:
        """
        updates the underlying database with the new contents of the current row.
        
        Cannot be called when on the insert row.

        Raises:
            SQLException: ``SQLException``
        """
        ...


