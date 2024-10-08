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
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..xml.user_defined_attributes_supplier import UserDefinedAttributesSupplier as UserDefinedAttributesSupplier_9fbe1222
if typing.TYPE_CHECKING:
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from ..table.border_line import BorderLine as BorderLine_a3f80af6
    from .x_text import XText as XText_690408ca
    from .x_text_section import XTextSection as XTextSection_b1730b9f
    from ..util.color import Color as Color_68e908c5
    from com.sun.star.style.GraphicLocation import GraphicLocationProto  # type: ignore

class CellProperties(UserDefinedAttributesSupplier_9fbe1222, XPropertySet_bc180bfa):
    """
    Service Class

    service that holds all cell properties of a text table cell in a text document.
    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API CellProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1CellProperties.html>`_
    """
    @property
    def BackColor(self) -> Color_68e908c5:
        """
        contains the background color.
        """
        ...
    @BackColor.setter
    def BackColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def BackGraphic(self) -> XGraphic_a4da0afc:
        """
        contains the graphic object that is displayed as background graphic.
        
        **since**
        
            LibreOffice 6.1
        """
        ...
    @BackGraphic.setter
    def BackGraphic(self, value: XGraphic_a4da0afc) -> None:
        ...
    @property
    def BackGraphicFilter(self) -> str:
        """
        contains the name of the graphic filter of the background graphic.
        """
        ...
    @BackGraphicFilter.setter
    def BackGraphicFilter(self, value: str) -> None:
        ...
    @property
    def BackGraphicLocation(self) -> GraphicLocationProto:
        """
        determines the position of the background graphic.
        """
        ...
    @BackGraphicLocation.setter
    def BackGraphicLocation(self, value: GraphicLocationProto) -> None:
        ...
    @property
    def BackGraphicURL(self) -> str:
        """
        contains the URL to the background graphic.
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When an URL is set, then it will load the graphic and set the BackGraphic property.
        """
        ...
    @BackGraphicURL.setter
    def BackGraphicURL(self, value: str) -> None:
        ...
    @property
    def BackTransparent(self) -> bool:
        """
        determines whether the background is transparent.
        """
        ...
    @BackTransparent.setter
    def BackTransparent(self, value: bool) -> None:
        ...
    @property
    def BottomBorder(self) -> BorderLine_a3f80af6:
        """
        contains the bottom border line.
        """
        ...
    @BottomBorder.setter
    def BottomBorder(self, value: BorderLine_a3f80af6) -> None:
        ...
    @property
    def BottomBorderDistance(self) -> int:
        """
        contains the distance of the bottom border.
        """
        ...
    @BottomBorderDistance.setter
    def BottomBorderDistance(self, value: int) -> None:
        ...
    @property
    def CellName(self) -> str:
        """
        contains the cell name, see SwXTextTable.getCellByName for more information
        """
        ...
    @CellName.setter
    def CellName(self, value: str) -> None:
        ...
    @property
    def HasTextChangesOnly(self) -> bool:
        """
        If TRUE, the table cell wasn't deleted or inserted with its tracked cell content.
        
        **since**
        
            LibreOffice 7.6
        """
        ...
    @HasTextChangesOnly.setter
    def HasTextChangesOnly(self, value: bool) -> None:
        ...
    @property
    def IsProtected(self) -> bool:
        """
        determines whether the cell is write protected or not.
        """
        ...
    @IsProtected.setter
    def IsProtected(self, value: bool) -> None:
        ...
    @property
    def LeftBorder(self) -> BorderLine_a3f80af6:
        """
        contains the left border line.
        """
        ...
    @LeftBorder.setter
    def LeftBorder(self, value: BorderLine_a3f80af6) -> None:
        ...
    @property
    def LeftBorderDistance(self) -> int:
        """
        contains the distance of the left border.
        """
        ...
    @LeftBorderDistance.setter
    def LeftBorderDistance(self, value: int) -> None:
        ...
    @property
    def NumberFormat(self) -> int:
        """
        contains the number format.
        """
        ...
    @NumberFormat.setter
    def NumberFormat(self, value: int) -> None:
        ...
    @property
    def ParentText(self) -> XText_690408ca:
        """
        Parent text of this table cell.
        
        This might be a header text, body text, parent cell, etc.
        
        **since**
        
            LibreOffice 6.3
        """
        ...
    @ParentText.setter
    def ParentText(self, value: XText_690408ca) -> None:
        ...
    @property
    def RightBorder(self) -> BorderLine_a3f80af6:
        """
        contains the right border line.
        """
        ...
    @RightBorder.setter
    def RightBorder(self, value: BorderLine_a3f80af6) -> None:
        ...
    @property
    def RightBorderDistance(self) -> int:
        """
        contains the distance of the right border.
        """
        ...
    @RightBorderDistance.setter
    def RightBorderDistance(self, value: int) -> None:
        ...
    @property
    def TextSection(self) -> XTextSection_b1730b9f:
        """
        contains the text section the text table is contained in if there is any.
        """
        ...
    @TextSection.setter
    def TextSection(self, value: XTextSection_b1730b9f) -> None:
        ...
    @property
    def TopBorder(self) -> BorderLine_a3f80af6:
        """
        contains the top border line.
        """
        ...
    @TopBorder.setter
    def TopBorder(self, value: BorderLine_a3f80af6) -> None:
        ...
    @property
    def TopBorderDistance(self) -> int:
        """
        contains the distance of the top border.
        """
        ...
    @TopBorderDistance.setter
    def TopBorderDistance(self, value: int) -> None:
        ...
    @property
    def VertOrient(self) -> int:
        """
        the vertical orientation of the text inside of the table cells in this row.
        """
        ...
    @VertOrient.setter
    def VertOrient(self, value: int) -> None:
        ...