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
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing
from ..beans.x_tolerant_multi_property_set import XTolerantMultiPropertySet as XTolerantMultiPropertySet_7bd4114e
from ..document.x_action_lockable import XActionLockable as XActionLockable_cb30e3a
from .sheet_ranges_query import SheetRangesQuery as SheetRangesQuery_efbe0d90
from .x_cell_addressable import XCellAddressable as XCellAddressable_ed700d53
from .x_sheet_annotation_anchor import XSheetAnnotationAnchor as XSheetAnnotationAnchor_48670fe8
from ..style.character_properties import CharacterProperties as CharacterProperties_1d4f0ef3
from ..style.character_properties_asian import CharacterPropertiesAsian as CharacterPropertiesAsian_6d8a10df
from ..style.character_properties_complex import CharacterPropertiesComplex as CharacterPropertiesComplex_90ca11cb
from ..style.paragraph_properties import ParagraphProperties as ParagraphProperties_1e240efc
from ..style.paragraph_properties_asian import ParagraphPropertiesAsian as ParagraphPropertiesAsian_6e8c10e8
from ..style.paragraph_properties_complex import ParagraphPropertiesComplex as ParagraphPropertiesComplex_91de11d4
from ..table.cell import Cell as Cell_680c0890
from ..table.x_column_row_range import XColumnRowRange as XColumnRowRange_e0e70cfb
from ..text.text import Text as Text_607f0872
from ..text.x_text_fields_supplier import XTextFieldsSupplier as XTextFieldsSupplier_d5d0e75
from ..util.x_indent import XIndent as XIndent_7b290980
from ..util.x_modify_broadcaster import XModifyBroadcaster as XModifyBroadcaster_fd990df0
from ..util.x_replaceable import XReplaceable as XReplaceable_b0750b6e
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e
    from ..awt.size import Size as Size_576707ef
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
    from .x_sheet_conditional_entries import XSheetConditionalEntries as XSheetConditionalEntries_694810c0
    from com.sun.star.table.CellContentType import CellContentTypeProto  # type: ignore

class SheetCell(SheetRangesQuery_efbe0d90, CharacterProperties_1d4f0ef3, CharacterPropertiesAsian_6d8a10df, CharacterPropertiesComplex_90ca11cb, ParagraphProperties_1e240efc, ParagraphPropertiesAsian_6e8c10e8, ParagraphPropertiesComplex_91de11d4, Cell_680c0890, Text_607f0872, XTolerantMultiPropertySet_7bd4114e, XActionLockable_cb30e3a, XCellAddressable_ed700d53, XSheetAnnotationAnchor_48670fe8, XColumnRowRange_e0e70cfb, XTextFieldsSupplier_d5d0e75, XIndent_7b290980, XModifyBroadcaster_fd990df0, XReplaceable_b0750b6e):
    """
    Service Class

    represents a single addressable cell in a spreadsheet document.
    
    **since**
    
        OOo 2.0

    See Also:
        `API SheetCell <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1SheetCell.html>`_
    """
    @property
    def AbsoluteName(self) -> str:
        """
        Returns the absolute address of the range as string, e.g.
        
        \"$Sheet1.$B$2\".
        """
        ...
    @AbsoluteName.setter
    def AbsoluteName(self, value: str) -> None:
        ...
    @property
    def CellContentType(self) -> CellContentTypeProto:
        """
        contains the content type of the cell.
        
        **since**
        
            LibreOffice 6.1
        """
        ...
    @CellContentType.setter
    def CellContentType(self, value: CellContentTypeProto) -> None:
        ...
    @property
    def ConditionalFormat(self) -> XSheetConditionalEntries_694810c0:
        """
        contains the conditional formatting settings for this cell.
        
        After a conditional format has been changed it has to be reinserted into the property set.
        """
        ...
    @ConditionalFormat.setter
    def ConditionalFormat(self, value: XSheetConditionalEntries_694810c0) -> None:
        ...
    @property
    def ConditionalFormatLocal(self) -> XSheetConditionalEntries_694810c0:
        """
        contains the conditional formatting settings for this cell, using localized formulas.
        
        After a conditional format has been changed it has to be reinserted into the property set.
        """
        ...
    @ConditionalFormatLocal.setter
    def ConditionalFormatLocal(self, value: XSheetConditionalEntries_694810c0) -> None:
        ...
    @property
    def FormulaLocal(self) -> str:
        """
        contains the formula string with localized function names.
        
        This property can also be used to set a new localized formula.
        """
        ...
    @FormulaLocal.setter
    def FormulaLocal(self, value: str) -> None:
        ...
    @property
    def FormulaResultType(self) -> int:
        """
        contains the content type of the cell.
        
        This property returns not com.sun.star.sheet.FormulaResult but instead com.sun.star.table.CellContentType. Use FormulaResult2 if the correct property is needed.
        """
        ...
    @FormulaResultType.setter
    def FormulaResultType(self, value: int) -> None:
        ...
    @property
    def FormulaResultType2(self) -> int:
        """
        contains the result type of a formula.
        
        **since**
        
            LibreOffice 6.1
        """
        ...
    @FormulaResultType2.setter
    def FormulaResultType2(self, value: int) -> None:
        ...
    @property
    def Position(self) -> Point_5fb2085e:
        """
        contains the position of this cell in the sheet (in 1/100 mm).
        
        This property contains the absolute position in the whole sheet, not the position in the visible area.
        """
        ...
    @Position.setter
    def Position(self, value: Point_5fb2085e) -> None:
        ...
    @property
    def Size(self) -> Size_576707ef:
        """
        contains the size of this cell (in 1/100 mm).
        """
        ...
    @Size.setter
    def Size(self, value: Size_576707ef) -> None:
        ...
    @property
    def Validation(self) -> XPropertySet_bc180bfa:
        """
        contains the data validation settings for this cell.
        
        After the data validation settings have been changed the validation has to be reinserted into the property set.
        """
        ...
    @Validation.setter
    def Validation(self, value: XPropertySet_bc180bfa) -> None:
        ...
    @property
    def ValidationLocal(self) -> XPropertySet_bc180bfa:
        """
        contains the data validation settings for this cell, using localized formulas.
        
        After the data validation settings have been changed the validation has to be reinserted into the property set.
        """
        ...
    @ValidationLocal.setter
    def ValidationLocal(self, value: XPropertySet_bc180bfa) -> None:
        ...