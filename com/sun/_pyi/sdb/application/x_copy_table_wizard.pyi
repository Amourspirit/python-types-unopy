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
# Namespace: com.sun.star.sdb.application
from typing_extensions import Literal
import typing
from ...ui.dialogs.x_executable_dialog import XExecutableDialog as XExecutableDialog_450f0fa1
if typing.TYPE_CHECKING:
    from .x_copy_table_listener import XCopyTableListener as XCopyTableListener_ad581224

class XCopyTableWizard(XExecutableDialog_450f0fa1):
    """
    describes a wizard which can be used to copy table like data from one database to another.
    
    Copying table data between databases can be a complex task. Especially when it comes to matching field types in the source and in the target database, some heuristics, and sometimes support from the user doing the operation, are required.
    
    The copy table wizard described by this interfaces cares for those, and other, settings.
    
    **since**
    
        OOo 2.4

    See Also:
        `API XCopyTableWizard <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1application_1_1XCopyTableWizard.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sdb.application.XCopyTableWizard']

    def addCopyTableListener(self, Listener: 'XCopyTableListener_ad581224') -> None:
        """
        adds a listener which is to be notified of progress in the copy operation
        """
    def removeCopyTableListener(self, Listener: 'XCopyTableListener_ad581224') -> None:
        """
        removes a listener
        """
    @property
    def CreatePrimaryKey(self) -> object:
        """
        specifies that a new primary key is to be created in the target database
        
        At initialization time, you can specify the initial settings for the primary key in the UI.
        
        You cannot use this attribute to determine the primary key, possibly created by the wizard, after it finished. The reason is that during the wizard run, the user can define an arbitrarily complex primary key, e.g. including multiple columns, which cannot be represented in this simple attribute anymore.
        
        This attribute is ignored if Operation is CopyTableOperation.AppendData.
        
        Changing this attribute while the dialog is running is not supported, the result of such an attempt is undefined.
        
        When a primary key is to be created by the wizard, it will be an auto-increment column, if possible.
        """

    @property
    def DestinationTableName(self) -> str:
        """
        specifies the name of the table in the destination database.
        
        At initialization time, you can use this attribute to control the initial table name as suggested to the user.
        
        After the wizard has finished, you can use this attribute to determine what table was actually created resp. to which existing table the source table's data was appended.
        
        Changing this attribute while the dialog is running is not supported, the result of such an attempt is undefined.
        """

    @property
    def Operation(self) -> int:
        """
        specifies the basic operation for the wizard to execute.
        
        This must be one of the CopyTableOperation constants.
        
        At initialization time, you can use this attribute to control the initial operation in the wizard.
        
        After the wizard has finished, you can use this attribute to determine what operation was actually executed.
        
        Changing this attribute while the dialog is running is not supported, the result of such an attempt is undefined.
        """

    @property
    def UseHeaderLineAsColumnNames(self) -> bool:
        """
        specifies that the first row should be used to identify column names.
        
        This attribute is ignored when the source defines the column names which isn't the case when only a part of a table should be copied e.g. in the RTF format or in the HTML format.
        """


__all__ = ['XCopyTableWizard']

