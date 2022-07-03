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
# Namespace: com.sun.star.xml.sax
from typing_extensions import Literal
import typing
from ...io.x_active_data_source import XActiveDataSource as XActiveDataSource_d1900c7f
from .x_extended_document_handler import XExtendedDocumentHandler as XExtendedDocumentHandler_89231159

class XWriter(XActiveDataSource_d1900c7f, XExtendedDocumentHandler_89231159):
    """
    Provides a unified interface for the new-style Writer service to implement.
    
    **since**
    
        LibreOffice 4.0

    See Also:
        `API XWriter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1sax_1_1XWriter.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.sax.XWriter']

    def setCustomEntityNames(self, replacements: 'typing.Tuple[typing.Tuple[str, str], ...]') -> None:
        """
        Adds support for custom entity names list.
        
        **since**
        
            LibreOffice 7.2
        """
        ...


