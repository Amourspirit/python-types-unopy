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
# Namespace: com.sun.star.text.textfield
from __future__ import annotations
from ..text_field import TextField as TextField_90260a56

class GetReference(TextField_90260a56):
    """
    Service Class

    specifies service of a reference field.
    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API GetReference <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1GetReference.html>`_
    """
    @property
    def CurrentPresentation(self) -> str:
        """
        contains the current content of the text field.
        
        This property is especially useful for import/export purposes.
        """
        ...
    @CurrentPresentation.setter
    def CurrentPresentation(self, value: str) -> None:
        ...
    @property
    def ReferenceFieldLanguage(self) -> str:
        """
        contains the language id of the alternative language-dependent references.
        
        Alternative language-dependent forms of reference types.
        
        The current set of supported languages is:
        
        **since**
        
            LibreOffice 6.1
        """
        ...
    @ReferenceFieldLanguage.setter
    def ReferenceFieldLanguage(self, value: str) -> None:
        ...
    @property
    def ReferenceFieldPart(self) -> int:
        """
        contains the type of the reference.
        """
        ...
    @ReferenceFieldPart.setter
    def ReferenceFieldPart(self, value: int) -> None:
        ...
    @property
    def ReferenceFieldSource(self) -> int:
        """
        contains the source of the reference.
        """
        ...
    @ReferenceFieldSource.setter
    def ReferenceFieldSource(self, value: int) -> None:
        ...
    @property
    def SequenceNumber(self) -> int:
        """
        contains the sequence number of a set expression field that is used as sequence field or the value of the ReferenceId property of a footnote or endnote.
        """
        ...
    @SequenceNumber.setter
    def SequenceNumber(self, value: int) -> None:
        ...
    @property
    def SourceName(self) -> str:
        """
        contains the name of the source.
        
        Depending on the property ReferenceFieldSource it may be the name of a bookmark, a reference mark.
        """
        ...
    @SourceName.setter
    def SourceName(self, value: str) -> None:
        ...

