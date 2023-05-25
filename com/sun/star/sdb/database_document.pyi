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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdb
from __future__ import annotations
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..sdbcx.x_data_descriptor_factory import XDataDescriptorFactory as XDataDescriptorFactory_46170fe5
from ..sdbcx.x_rename import XRename as XRename_848c09cc

class DatabaseDocument(XPropertySet_bc180bfa, XDataDescriptorFactory_46170fe5, XRename_848c09cc):
    """
    Service Class

    specifies a link to a document associated with a database document
    
    **since**
    
        OOo 2.0
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API DatabaseDocument <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1DatabaseDocument.html>`_
    """
    @property
    def Name(self) -> str:
        """
        is the name of the document.
        """
        ...
    @Name.setter
    def Name(self, value: str) -> None:
        ...
    @property
    def URL(self) -> str:
        """
        is the URL of the document.
        """
        ...
    @URL.setter
    def URL(self, value: str) -> None:
        ...
