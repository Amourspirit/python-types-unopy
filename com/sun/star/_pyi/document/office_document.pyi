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
# Libre Office Version: 7.2
# Namespace: com.sun.star.document
import typing
from .x_document_event_broadcaster import XDocumentEventBroadcaster as XDocumentEventBroadcaster_b2f1126a
from .x_document_properties_supplier import XDocumentPropertiesSupplier as XDocumentPropertiesSupplier_dc4b137f
from .x_embedded_scripts import XEmbeddedScripts as XEmbeddedScripts_1ab50eb1
from .x_event_broadcaster import XEventBroadcaster as XEventBroadcaster_2b120f2b
from .x_events_supplier import XEventsSupplier as XEventsSupplier_ecd0e88
from .x_undo_manager_supplier import XUndoManagerSupplier as XUndoManagerSupplier_5aae1064
from .x_view_data_supplier import XViewDataSupplier as XViewDataSupplier_2ae20f28
from ..frame.x_model import XModel as XModel_7a6e095c
from ..frame.x_storable import XStorable as XStorable_998f0aa7
from ..util.x_modifiable import XModifiable as XModifiable_a4f60b0a
from ..view.x_print_job_broadcaster import XPrintJobBroadcaster as XPrintJobBroadcaster_19ea0ead
from ..view.x_printable import XPrintable as XPrintable_9a5b0abc
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class OfficeDocument(XDocumentEventBroadcaster_b2f1126a, XDocumentPropertiesSupplier_dc4b137f, XEmbeddedScripts_1ab50eb1, XEventBroadcaster_2b120f2b, XEventsSupplier_ecd0e88, XUndoManagerSupplier_5aae1064, XViewDataSupplier_2ae20f28, XModel_7a6e095c, XStorable_998f0aa7, XModifiable_a4f60b0a, XPrintJobBroadcaster_19ea0ead, XPrintable_9a5b0abc):
    """
    Service Class

    abstract service which specifies a storable and printable document
    
    All major document-like components should support this service instead of simple components which supports a com.sun.star.frame.Controller or pure com.sun.star.awt.XWindow only.
    
    **since**
    
        LibreOffice 4.2

    See Also:
        `API OfficeDocument <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1document_1_1OfficeDocument.html>`_
    """
    @property
    def InteropGrabBag(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        Grab bag of document properties, used as a string-any map for interim interop purposes.
        
        This property is intentionally not handled by the ODF filter. Any member that should be handled there should be first moved out from this grab bag to a separate property.
        
        **since**
        
            LibreOffice 4.2
        """
        ...
    @property
    def ApplyFormDesignMode(self) -> bool:
        """
        controls the initial (on-load) behavior of the form controls in the document
        
        If set to TRUE, upon loading the document, the form controls will be in design mode.If set to FALSE, they will be alive, i.e. operational.With this, you may control if your document works primarily as a form document.
        """
        ...
    @property
    def AutomaticControlFocus(self) -> bool:
        """
        controls the focus behavior of the form controls in the document
        
        If this flag is set to TRUE, any view belonging to the document should focus the first control in the document. With this, you may control if your document works primarily as a form document.
        """
        ...
    @property
    def RuntimeUID(self) -> str:
        """
        contains a unique id for the document
        
        Once calculated, the id must not change until the document has been closed. Upon closing it will not be made persistent. Thus, the document may get a different id every time it gets loaded.
        """
        ...


