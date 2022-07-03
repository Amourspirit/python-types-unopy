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
# Namespace: com.sun.star.sdb
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .definition_content import DefinitionContent as DefinitionContent_e0d20d25
from .x_sub_document import XSubDocument as XSubDocument_a2da0b02

class DocumentDefinition(DefinitionContent_e0d20d25, XPropertySet_bc180bfa, XSubDocument_a2da0b02):
    """
    Service Class

    specifies a sub document of an OfficeDatabaseDocument.
    
    Usual instances of a DocumentDefinition are forms and reports.
    
    Note that the DocumentDefinition does not denote the actual document (i.e. an object supporting the com.sun.star.frame.XModel interface), but only a shortcut to access and load those actual documents.

    See Also:
        `API DocumentDefinition <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1DocumentDefinition.html>`_
    """
    @property
    def AsTemplate(self) -> bool:
        """
        Indicates if the document is to be used as template, for example, if a report is to be filled with data.
        """
        ...
    @property
    def Name(self) -> str:
        """
        is the name of the document.
        
        If the document is part of the container, it is not possible to alter the name.
        """
        ...


