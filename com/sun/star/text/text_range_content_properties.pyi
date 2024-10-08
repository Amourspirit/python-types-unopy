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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.text
from __future__ import annotations
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ..table.x_cell import XCell as XCell_70d408e8
    from .x_document_index import XDocumentIndex as XDocumentIndex_c9330c5c
    from .x_document_index_mark import XDocumentIndexMark as XDocumentIndexMark_fe490de7
    from .x_footnote import XFootnote as XFootnote_901e0a73
    from .x_text_content import XTextContent as XTextContent_b16e0ba5
    from .x_text_frame import XTextFrame as XTextFrame_9a7e0ab5
    from .x_text_section import XTextSection as XTextSection_b1730b9f
    from .x_text_table import XTextTable as XTextTable_9a810ab2

class TextRangeContentProperties(ABC):
    """
    Service Class

    describes the structural properties to retrieve text contents.
    
    **since**
    
        OOo 3.3

    See Also:
        `API TextRangeContentProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextRangeContentProperties.html>`_
    """
    @property
    def Cell(self) -> XCell_70d408e8:
        """
        may contain a table cell.
        """
        ...
    @Cell.setter
    def Cell(self, value: XCell_70d408e8) -> None:
        ...
    @property
    def ContentControl(self) -> XTextContent_b16e0ba5:
        """
        may contain a content control.
        
        **since**
        
            LibreOffice 7.4
        """
        ...
    @ContentControl.setter
    def ContentControl(self, value: XTextContent_b16e0ba5) -> None:
        ...
    @property
    def DocumentIndex(self) -> XDocumentIndex_c9330c5c:
        """
        may contain a document index.
        """
        ...
    @DocumentIndex.setter
    def DocumentIndex(self, value: XDocumentIndex_c9330c5c) -> None:
        ...
    @property
    def DocumentIndexMark(self) -> XDocumentIndexMark_fe490de7:
        """
        may contain a document index mark.
        """
        ...
    @DocumentIndexMark.setter
    def DocumentIndexMark(self, value: XDocumentIndexMark_fe490de7) -> None:
        ...
    @property
    def Endnote(self) -> XFootnote_901e0a73:
        """
        may contain an endnote.
        """
        ...
    @Endnote.setter
    def Endnote(self, value: XFootnote_901e0a73) -> None:
        ...
    @property
    def Footnote(self) -> XFootnote_901e0a73:
        """
        may contain a footnote.
        """
        ...
    @Footnote.setter
    def Footnote(self, value: XFootnote_901e0a73) -> None:
        ...
    @property
    def LineBreak(self) -> XTextContent_b16e0ba5:
        """
        Properties of the linebreak, e.g.
        
        for clearing break purposes.
        
        **since**
        
            LibreOffice 7.4
        """
        ...
    @LineBreak.setter
    def LineBreak(self, value: XTextContent_b16e0ba5) -> None:
        ...
    @property
    def NestedTextContent(self) -> XTextContent_b16e0ba5:
        """
        may contain a nested text content.
        
        For example, may contain an InContentMetadata or a com.sun.star.text.textfield.MetadataField.
        """
        ...
    @NestedTextContent.setter
    def NestedTextContent(self, value: XTextContent_b16e0ba5) -> None:
        ...
    @property
    def ReferenceMark(self) -> XTextContent_b16e0ba5:
        """
        may contain a reference mark.
        """
        ...
    @ReferenceMark.setter
    def ReferenceMark(self, value: XTextContent_b16e0ba5) -> None:
        ...
    @property
    def TextFrame(self) -> XTextFrame_9a7e0ab5:
        """
        may contain a text frame.
        """
        ...
    @TextFrame.setter
    def TextFrame(self, value: XTextFrame_9a7e0ab5) -> None:
        ...
    @property
    def TextParagraph(self) -> XTextContent_b16e0ba5:
        """
        Paragraph for the start of this range.
        
        **since**
        
            LibreOffice 6.0
        """
        ...
    @TextParagraph.setter
    def TextParagraph(self, value: XTextContent_b16e0ba5) -> None:
        ...
    @property
    def TextSection(self) -> XTextSection_b1730b9f:
        """
        may contain a text section.
        """
        ...
    @TextSection.setter
    def TextSection(self, value: XTextSection_b1730b9f) -> None:
        ...
    @property
    def TextTable(self) -> XTextTable_9a810ab2:
        """
        may contain a text table.
        """
        ...
    @TextTable.setter
    def TextTable(self, value: XTextTable_9a810ab2) -> None:
        ...

