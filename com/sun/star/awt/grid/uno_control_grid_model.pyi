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
# Namespace: com.sun.star.awt.grid
from __future__ import annotations
import typing
from ..uno_control_model import UnoControlModel as UnoControlModel_c8ce0c58
if typing.TYPE_CHECKING:
    from ..font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from .x_grid_column_model import XGridColumnModel as XGridColumnModel_16290e65
    from .x_grid_data_model import XGridDataModel as XGridDataModel_f8b20d71
    from ...util.color import Color as Color_68e908c5
    from com.sun.star.view.SelectionType import SelectionTypeProto  # type: ignore
    from com.sun.star.style.VerticalAlignment import VerticalAlignmentProto  # type: ignore

class UnoControlGridModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a UnoControlGrid control.
    
    **since**
    
        OOo 3.3

    See Also:
        `API UnoControlGridModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1grid_1_1UnoControlGridModel.html>`_
    """
    @property
    def RowBackgroundColors(self) -> typing.Tuple[Color_68e908c5, ...]:
        """
        specifies the colors to be used as background for data rows.
        
        If this sequence is non-empty, the data rows will be rendered with alternating background colors: Assuming the sequence has n elements, each row will use the background color as specified by its number's remainder modulo n.
        
        If this sequence is empty, all rows will use the same background color as the control as whole.
        
        If this property has a value of VOID, rows will be painted in alternating background colors, every second row having a background color derived from the control's selection color.
        """
        ...
    @RowBackgroundColors.setter
    def RowBackgroundColors(self, value: typing.Tuple[Color_68e908c5, ...]) -> None:
        ...
    @property
    def ActiveSelectionBackgroundColor(self) -> Color_68e908c5:
        """
        specifies the color to be used when drawing the background of selected cells, while the control has the focus.
        
        If this property has a value of VOID, the grid control renderer will use some default color, depending on the control's style settings.
        """
        ...
    @ActiveSelectionBackgroundColor.setter
    def ActiveSelectionBackgroundColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def ActiveSelectionTextColor(self) -> Color_68e908c5:
        """
        specifies the color to be used when drawing the text of selected cells, while the control has the focus.
        
        If this property has a value of VOID, the grid control renderer will use some default color, depending on the control's style settings.
        """
        ...
    @ActiveSelectionTextColor.setter
    def ActiveSelectionTextColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def ColumnHeaderHeight(self) -> int:
        """
        specifies the height of the column header row, if applicable.
        
        The height is specified in application font units - see com.sun.star.util.MeasureUnit.
        
        The value given here is ignored if ShowColumnHeader is FALSE.
        
        If the property is VOID, the grid control shall automatically determine a height which conveniently allows, according to the used font, to display one line of text.
        """
        ...
    @ColumnHeaderHeight.setter
    def ColumnHeaderHeight(self, value: int) -> None:
        ...
    @property
    def ColumnModel(self) -> XGridColumnModel_16290e65:
        """
        Specifies the XGridColumnModel that is providing the column structure.
        
        You can implement your own instance of XGridColumnModel or use the DefaultGridColumnModel.
        
        The column model is in the ownership of the grid model: When you set a new column model, or dispose the grid model, then the (old) column model is disposed, too.
        
        The default for this property is an empty instance of the DefaultGridColumnModel.
        """
        ...
    @ColumnModel.setter
    def ColumnModel(self, value: XGridColumnModel_16290e65) -> None:
        ...
    @property
    def FontDescriptor(self) -> FontDescriptor_bc110c0a:
        """
        specifies the font attributes of the text in the control.
        """
        ...
    @FontDescriptor.setter
    def FontDescriptor(self, value: FontDescriptor_bc110c0a) -> None:
        ...
    @property
    def FontEmphasisMark(self) -> int:
        """
        specifies the com.sun.star.text.FontEmphasis value of the text in the control.
        """
        ...
    @FontEmphasisMark.setter
    def FontEmphasisMark(self, value: int) -> None:
        ...
    @property
    def FontRelief(self) -> int:
        """
        specifies the com.sun.star.text.FontRelief value of the text in the control.
        """
        ...
    @FontRelief.setter
    def FontRelief(self, value: int) -> None:
        ...
    @property
    def GridDataModel(self) -> XGridDataModel_f8b20d71:
        """
        Specifies the XGridDataModel that is providing the hierarchical data.
        
        You can implement your own instance of XGridDataModel or use the DefaultGridDataModel.
        
        The data model is in the ownership of the grid model: When you set a new data model, or dispose the grid model, then the (old) data model is disposed, too.
        
        The default for this property is an empty instance of the DefaultGridDataModel.
        """
        ...
    @GridDataModel.setter
    def GridDataModel(self, value: XGridDataModel_f8b20d71) -> None:
        ...
    @property
    def GridLineColor(self) -> Color_68e908c5:
        """
        specifies the color to be used when drawing lines between cells
        
        If this property has a value of VOID, the grid control renderer will use some default color, depending on the control's style settings.
        """
        ...
    @GridLineColor.setter
    def GridLineColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def HScroll(self) -> bool:
        """
        Specifies the vertical scrollbar mode.
        
        The default value is FALSE
        """
        ...
    @HScroll.setter
    def HScroll(self, value: bool) -> None:
        ...
    @property
    def HeaderBackgroundColor(self) -> Color_68e908c5:
        """
        specifies the color to be used when drawing the background of row or column headers
        
        If this property has a value of VOID, the grid control renderer will use some default color, depending on the control's style settings.
        """
        ...
    @HeaderBackgroundColor.setter
    def HeaderBackgroundColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def HeaderTextColor(self) -> Color_68e908c5:
        """
        specifies the color to be used when drawing the text within row or column headers
        
        If this property has a value of VOID, the grid control renderer will use some default color, depending on the control's style settings.
        """
        ...
    @HeaderTextColor.setter
    def HeaderTextColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def HelpText(self) -> str:
        """
        specifies the help text of the control.
        """
        ...
    @HelpText.setter
    def HelpText(self, value: str) -> None:
        ...
    @property
    def HelpURL(self) -> str:
        """
        specifies the help URL of the control.
        """
        ...
    @HelpURL.setter
    def HelpURL(self, value: str) -> None:
        ...
    @property
    def InactiveSelectionBackgroundColor(self) -> Color_68e908c5:
        """
        specifies the color to be used when drawing the background of selected cells, while the control does not have the focus.
        
        If this property has a value of VOID, the grid control renderer will use some default color, depending on the control's style settings.
        """
        ...
    @InactiveSelectionBackgroundColor.setter
    def InactiveSelectionBackgroundColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def InactiveSelectionTextColor(self) -> Color_68e908c5:
        """
        specifies the color to be used when drawing the text of selected cells, while the control does not have the focus.
        
        If this property has a value of VOID, the grid control renderer will use some default color, depending on the control's style settings.
        """
        ...
    @InactiveSelectionTextColor.setter
    def InactiveSelectionTextColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def RowHeaderWidth(self) -> int:
        """
        specifies the width of the row header column, if applicable.
        
        The width is specified in application font units - see com.sun.star.util.MeasureUnit.
        
        The value given here is ignored if ShowRowHeader is FALSE.
        """
        ...
    @RowHeaderWidth.setter
    def RowHeaderWidth(self, value: int) -> None:
        ...
    @property
    def RowHeight(self) -> int:
        """
        Specifies the height of rows in the grid control.
        
        The height is specified in application font units - see com.sun.star.util.MeasureUnit.
        """
        ...
    @RowHeight.setter
    def RowHeight(self, value: int) -> None:
        ...
    @property
    def SelectionModel(self) -> SelectionTypeProto:
        """
        Specifies the selection mode that is enabled for this grid control.
        
        The default value is com.sun.star.view.SelectionType.SINGLE
        """
        ...
    @SelectionModel.setter
    def SelectionModel(self, value: SelectionTypeProto) -> None:
        ...
    @property
    def ShowColumnHeader(self) -> bool:
        """
        Specifies whether the grid control should display a title row.
        
        The default value is TRUE
        """
        ...
    @ShowColumnHeader.setter
    def ShowColumnHeader(self, value: bool) -> None:
        ...
    @property
    def ShowRowHeader(self) -> bool:
        """
        Specifies whether the grid control should display a special header column.
        
        The default value is FALSE
        """
        ...
    @ShowRowHeader.setter
    def ShowRowHeader(self, value: bool) -> None:
        ...
    @property
    def Tabstop(self) -> bool:
        """
        Specifies that the control can be reached with the TAB key.
        """
        ...
    @Tabstop.setter
    def Tabstop(self, value: bool) -> None:
        ...
    @property
    def TextColor(self) -> Color_68e908c5:
        """
        specifies the color to be used when drawing cell texts
        
        If this property has a value of VOID, the grid control renderer will use some default color, depending on the control's style settings.
        """
        ...
    @TextColor.setter
    def TextColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def TextLineColor(self) -> Color_68e908c5:
        """
        specifies the color to be used when drawing text lines (underlining and strikethrough)
        
        If this property has a value of VOID, the grid control renderer will use some default color, depending on the control's style settings.
        """
        ...
    @TextLineColor.setter
    def TextLineColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def UseGridLines(self) -> bool:
        """
        controls whether or not to paint horizontal and vertical lines between the grid cells.
        """
        ...
    @UseGridLines.setter
    def UseGridLines(self, value: bool) -> None:
        ...
    @property
    def VScroll(self) -> bool:
        """
        Specifies the horizontal scrollbar mode.
        
        The default value is FALSE
        """
        ...
    @VScroll.setter
    def VScroll(self, value: bool) -> None:
        ...
    @property
    def VerticalAlign(self) -> VerticalAlignmentProto:
        """
        specifies the vertical alignment of the content in the control.
        """
        ...
    @VerticalAlign.setter
    def VerticalAlign(self, value: VerticalAlignmentProto) -> None:
        ...