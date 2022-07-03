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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.sdb.application
import typing
from .x_copy_table_wizard import XCopyTableWizard as XCopyTableWizard_89b7114f
if typing.TYPE_CHECKING:
    from ...beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
    from ...task.x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51

class CopyTableWizard(XCopyTableWizard_89b7114f):
    """
    Service Class

    describes a wizard which can be used to copy table like data from one database to another.
    
    **since**
    
        OOo 2.4

    See Also:
        `API CopyTableWizard <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1application_1_1CopyTableWizard.html>`_
    """
    def create(self, Source: 'XPropertySet_bc180bfa', Destination: 'XPropertySet_bc180bfa') -> None:
        """
        creates an executable wizard dialog, which is to guide the user through copying a table from one database to another.
        
        At creation time, an attempt will be made to obtain the connections described by Source resp. Dest. Failing to do so will result in an exception.
        
        If the connection has been newly created by the wizard (e.g. because the data access descriptor specified a DataSource instead of an ActiveConnection), then this connection will be disposed upon disposal of the wizard.
        
        The following members of the DataAccessDescriptor are supported, and evaluated in the given order:
        
        The first 5 items are used to obtain the connection, the last two to determine which of the connection's objects is to be copied. Note that Command and CommandType are required.
        
        Additionally to the obvious restrictions (such as that creating a view is not possible if the copy source and the copy destination denote different databases), the following restrictions apply to the settings, and possible combinations:
        
        Violating any of the above restrictions will result in an error at creation time.
        
        Only DataSourceName, DatabaseLocation, ActiveConnection are supported, effectively describing the target connection to copy the data to. They're evaluated in the order mentioned here, so if multiple of the are present, only the first one is evaluated.
        
        Also, at the moment the connection which is implied by either of the settings above must support the com.sun.star.sdb.Connection service. In particular, it is not sufficient to pass an SDBC-level connection.
        
        Note that creating a view (see CopyTableOperation.CreateAsView) is not supported if the target connection is an SDBC-level connection only.

        Raises:
            : ````
            : ````
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def createWithInteractionHandler(self, Source: 'XPropertySet_bc180bfa', Destination: 'XPropertySet_bc180bfa', InteractionHandler: 'XInteractionHandler_bf80e51') -> None:
        """
        creates an executable wizard dialog, which is to guide the user through copying a table from one database to another.
        
        The only difference to the create() constructor is that createWithInteractionHandler takes an additional argument, which can be used to intercept interactions (such as error messages) during the wizard run.
        
        When specifying this parameter, you should use an implementation supporting the com.sun.star.sdb.InteractionHandler, since the general-purpose com.sun.star.task.InteractionHandler cannot handle all requests described above.

        Raises:
            : ````
            : ````
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...


