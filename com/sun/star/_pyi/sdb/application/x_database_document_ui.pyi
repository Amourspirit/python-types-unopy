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
from abc import ABC
if typing.TYPE_CHECKING:
    from ...awt.x_window import XWindow as XWindow_713b0924
    from ...beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ...lang.x_component import XComponent as XComponent_98dc0ab5
    from ...sdbc.x_connection import XConnection as XConnection_a36a0b0c
    from ...sdbc.x_data_source import XDataSource as XDataSource_a2990ae7

class XDatabaseDocumentUI(ABC):
    """
    provides access to the user interface of a database document
    
    This interface is available when a database document has been loaded into a frame, at the controller of this frame.
    
    **since**
    
        OOo 2.2

    See Also:
        `API XDatabaseDocumentUI <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1application_1_1XDatabaseDocumentUI.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sdb.application.XDatabaseDocumentUI']

    def closeSubComponents(self) -> bool:
        """
        closes all sub components of the database document.
        
        During working with the database, the user might open different sub components: forms, reports, tables, queries. If you need to close all those documents, use closeSubComponents, which will gracefully do this.
        
        In a first step, the sub components will be suspended (com.sun.star.frame.XController.suspend()). There are basically two reasons why suspending a single sub component can fail: The user might veto it (she's asked if the document is currently modified), and the component might be uncloseable currently, e.g. due to an open modal dialog, or a long-lasting operation running currently (e.g. printing).
        
        Once all sub components have been suspended, they will, in a second step, be closed. Again, closing might be vetoed by other instances, e.g. by a close listener registered at the component.
        
        **since**
        
            OOo 3.0
        """
        ...
    def connect(self) -> None:
        """
        lets the application connect to the database
        
        If the application is already connected, nothing happens. If it is not connected, the application will try to establish a connection by using com.sun.star.sdbc.XDataSource.getConnection() with the current settings, as specified in the com.sun.star.sdb.DataSource.Settings member.
        
        If the connection cannot be established, the respective error message is shown in the application window.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def createComponent(self, ObjectType: int, DocumentDefinition: 'XComponent_98dc0ab5') -> 'XComponent_98dc0ab5':
        """
        creates a new sub component of the given type

        * ``DocumentDefinition`` is an out direction argument.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def createComponentWithArguments(self, ObjectType: int, Arguments: 'typing.Tuple[PropertyValue_c9610c73, ...]', DocumentDefinition: 'XComponent_98dc0ab5') -> 'XComponent_98dc0ab5':
        """
        creates a new sub component of the given type
        
        In opposite to createComponent(), this method allows you to specify additional arguments which are passed to the to-be-loaded component.

        * ``DocumentDefinition`` is an out direction argument.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def identifySubComponent(self, SubComponent: 'XComponent_98dc0ab5') -> 'typing.Tuple[int, str]':
        """
        identifies the given sub component

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def isConnected(self) -> bool:
        """
        determines whether the application is currently connected to the database
        """
        ...
    def loadComponent(self, ObjectType: int, ObjectName: str, ForEditing: bool) -> 'XComponent_98dc0ab5':
        """
        loads the given sub component of the database document
        
        This method allows programmatic access to the functionality which is present in the UI: it allows opening a table, query, form, or report for either editing or viewing.
        
        This method is a convenience wrapper for API which is also available otherwise. For instance, for loading forms and reports, you could use the com.sun.star.frame.XComponentLoader interface of the com.sun.star.sdb.Forms resp. com.sun.star.sdb.Reports collections.
        
        Note there must exist a connection to the database before you can call this method.
        
        If an error occurs opening the given object, then this is reported to the user via an error dialog.
        
        For the different object types, this means the following

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def loadComponentWithArguments(self, ObjectType: int, ObjectName: str, ForEditing: bool, Arguments: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> 'XComponent_98dc0ab5':
        """
        loads the given sub component of the database document
        
        In opposite to loadComponent(), this method allows you to specify additional arguments which are passed to the to-be-loaded component.
        
        The meaning of the arguments is defined at the service which is effectively created. See the above table for a list of those services.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...

    @property
    def SubComponents(self) -> 'typing.Tuple[XComponent_98dc0ab5, ...]':
        """
        contains all sub components of the database document
        
        During working with the database, the user might open different sub components: forms, reports, tables, queries. Those components are tracked by the application, and provided in this attribute.
        
        The components here might either be documents (com.sun.star.frame.XModel), controllers (com.sun.star.frame.XController), or frames (com.sun.star.frame.XFrame).
        
        **since**
        
            OOo 3.0
        """
        ...

    @property
    def ActiveConnection(self) -> 'XConnection_a36a0b0c':
        """
        provides access to the current connection of the application
        
        Note that the connection returned here is really the working connection of the application. Clients should not misuse it, in particular, closing the connection can yield unexpected results and should definitely be avoided. If you need a separate connection to the data source, use com.sun.star.sdbc.XDataSource.getConnection().
        """
        ...

    @property
    def ApplicationMainWindow(self) -> 'XWindow_713b0924':
        """
        provides access to the application's main window
        
        Note that reading this attribute is equivalent to querying the component for the com.sun.star.frame.XController interface, asking the controller for its frame, and asking this frame for its container window.
        """
        ...

    @property
    def DataSource(self) -> 'XDataSource_a2990ae7':
        """
        provides access to the data source belong to the database document
        """
        ...


