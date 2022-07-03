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
# Namespace: com.sun.star.text
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class ViewSettings(XPropertySet_bc180bfa):
    """
    Service Class

    provides access to the settings of the controller of a text document.
    
    **since**
    
        LibreOffice 5.1

    See Also:
        `API ViewSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1ViewSettings.html>`_
    """
    @property
    def HideWhitespace(self) -> bool:
        """
        If this property is TRUE, whitespaces around pages are hidden.
        
        **since**
        
            LibreOffice 5.1
        """
        ...
    @property
    def HorizontalRulerMetric(self) -> int:
        """
        metric unit of the horizontal ruler
        
        Uses values com.sun.star.awt.FieldUnit
        
        **since**
        
            OOo 3.1
        """
        ...
    @property
    def IsExecuteHyperlinks(self) -> bool:
        """
        If this property is TRUE hyperlinks in the document are executed (loaded) on mouse click.
        
        Otherwise they are handled like normal text.
        """
        ...
    @property
    def IsRasterVisible(self) -> bool:
        """
        Specifies whether to display the grid or not.
        
        **since**
        
            OOo 2.0
        """
        ...
    @property
    def IsSnapToRaster(self) -> bool:
        """
        Specifies whether to move frames, drawing elements, and form functions only between grid points.
        
        **since**
        
            OOo 2.0
        """
        ...
    @property
    def IsVertRulerRightAligned(self) -> bool:
        """
        If this property is TRUE, the vertical ruler is aligned to the right side of the view and the vertical scrollbar is on the left.
        """
        ...
    @property
    def RasterResolutionX(self) -> int:
        """
        Defines the unit of measure for the spacing between grid points on the X-axis.
        
        The value must be greater than 0. The application may enforce more restricting bounds for the value.
        
        **since**
        
            OOo 2.0
        """
        ...
    @property
    def RasterResolutionY(self) -> int:
        """
        Defines the unit of measure for the spacing between grid points on the Y-axis.
        
        The value must be greater than 0. The application may enforce more restricting bounds for the value.
        
        **since**
        
            OOo 2.0
        """
        ...
    @property
    def RasterSubdivisionX(self) -> int:
        """
        Specifies the number of intervals between grid points on the X-axis.
        
        The value must be greater or equal to 0, and the application may enforce an upper bound for the value.
        
        **since**
        
            OOo 2.0
        """
        ...
    @property
    def RasterSubdivisionY(self) -> int:
        """
        Specifies the number of intervals between grid points on the Y-axis.
        
        The value must be greater or equal to 0, and the application may enforce an upper bound for the value.
        
        **since**
        
            OOo 2.0
        """
        ...
    @property
    def ShowAnnotations(self) -> bool:
        """
        If this property is TRUE, annotations (notes) are visible.
        """
        ...
    @property
    def ShowBookmarks(self) -> bool:
        """
        If this property is TRUE, bookmark positions are displayed.
        
        **since**
        
            LibreOffice 7.0
        """
        ...
    @property
    def ShowBreaks(self) -> bool:
        """
        If this property is TRUE, paragraph line breaks are visible.
        """
        ...
    @property
    def ShowChangesInMargin(self) -> bool:
        """
        If this property is TRUE, tracked deletions are shown in margin.
        
        **since**
        
            LibreOffice 7.1
        """
        ...
    @property
    def ShowContentTips(self) -> bool:
        """
        If this property is TRUE, tips for document content are shown, typically in a help balloon when the mouse is over the content.
        
        **since**
        
            LibreOffice 4.1
        """
        ...
    @property
    def ShowDrawings(self) -> bool:
        """
        If this property is TRUE, shapes are visible.
        """
        ...
    @property
    def ShowFieldCommands(self) -> bool:
        """
        If this property is TRUE, text fields are shown with their commands; otherwise the content is visible.
        """
        ...
    @property
    def ShowFootnoteBackground(self) -> bool:
        """
        If this property is TRUE, footnotes symbols are displayed with gray background.
        """
        ...
    @property
    def ShowGraphics(self) -> bool:
        """
        If this property is TRUE, graphic objects are visible.
        """
        ...
    @property
    def ShowHiddenCharacters(self) -> bool:
        """
        If this property is TRUE, hidden characters are displayed.
        
        **since**
        
            OOo 3.0
        """
        ...
    @property
    def ShowHiddenParagraphs(self) -> bool:
        """
        If this property is TRUE, hidden paragraphs are displayed.
        """
        ...
    @property
    def ShowHiddenText(self) -> bool:
        """
        If this property is TRUE, hidden text is displayed.
        """
        ...
    @property
    def ShowHoriRuler(self) -> bool:
        """
        If this property is TRUE and the property ShowRulers is TRUE, the horizontal ruler is displayed.
        """
        ...
    @property
    def ShowHoriScrollBar(self) -> bool:
        """
        If this property is TRUE and the property ShowRulers is TRUE, the horizontal scroll bar is displayed.
        """
        ...
    @property
    def ShowIndexMarkBackground(self) -> bool:
        """
        If this property is TRUE, index marks are displayed with gray background.
        """
        ...
    @property
    def ShowInlineTooltips(self) -> bool:
        """
        If this property is TRUE, tooltips for tracked changes are shown.
        
        **since**
        
            LibreOffice 6.1
        """
        ...
    @property
    def ShowNonprintingCharacters(self) -> bool:
        """
        If this property is TRUE, the settings of non-printing characters are applied.
        
        This option controls the use of the settings ShowHiddenCharacters, ShowTabstops, ShowSpaces, ShowBreaks and ShowParaBreaks
        
        **since**
        
            OOo 3.0
        """
        ...
    @property
    def ShowOnlineLayout(self) -> bool:
        """
        If this property is TRUE the document will be displayed as if it were a HTML document.
        """
        ...
    @property
    def ShowOutlineContentVisibilityButton(self) -> bool:
        """
        If this property is TRUE, the outline content visibility toggle button is shown.
        
        **since**
        
            LibreOffice 7.1
        """
        ...
    @property
    def ShowParaBreaks(self) -> bool:
        """
        If this property is TRUE, paragraph breaks are visible.
        """
        ...
    @property
    def ShowProtectedSpaces(self) -> bool:
        """
        If this property is TRUE, protected spaces (hard spaces) are displayed with gray background.
        """
        ...
    @property
    def ShowRulers(self) -> bool:
        """
        ShowHoriRuler and ShowVertRuler determine whether a ruler is visible.
        """
        ...
    @property
    def ShowScrollBarTips(self) -> bool:
        """
        If this property is TRUE, and the scroll bar is shown, a tool tip is displayed while scrolling.
        
        **since**
        
            LibreOffice 4.2
        """
        ...
    @property
    def ShowSoftHyphens(self) -> bool:
        """
        If this property is TRUE, soft hyphens are displayed with gray background.
        """
        ...
    @property
    def ShowSpaces(self) -> bool:
        """
        If this property is TRUE, spaces are displayed with dots.
        """
        ...
    @property
    def ShowTableBoundaries(self) -> bool:
        """
        If this property is TRUE, table boundaries are displayed.
        """
        ...
    @property
    def ShowTables(self) -> bool:
        """
        If this property is TRUE, tables are visible.
        """
        ...
    @property
    def ShowTabstops(self) -> bool:
        """
        If this property is TRUE, tab stops are visible.
        """
        ...
    @property
    def ShowTextBoundaries(self) -> bool:
        """
        If this property is TRUE, text boundaries are displayed.
        """
        ...
    @property
    def ShowTextFieldBackground(self) -> bool:
        """
        If this property is TRUE, text fields are displayed with gray background.
        """
        ...
    @property
    def ShowVertRuler(self) -> bool:
        """
        If this property is TRUE, the vertical ruler is displayed.
        """
        ...
    @property
    def ShowVertScrollBar(self) -> bool:
        """
        If this property is TRUE, the vertical scroll bar is displayed.
        """
        ...
    @property
    def SmoothScrolling(self) -> bool:
        """
        If this property is TRUE, smooth scrolling is active.
        """
        ...
    @property
    def TreatSubOutlineLevelsAsContent(self) -> bool:
        """
        If this property is TRUE, sub outline levels are treated as content in outline content visibility actions.
        
        **since**
        
            LibreOffice 7.2
        """
        ...
    @property
    def UseHeaderFooterMenu(self) -> bool:
        """
        If this property is TRUE, the advanced menu for header/footer is shown.
        
        **since**
        
            LibreOffice 6.2
        """
        ...
    @property
    def VerticalRulerMetric(self) -> int:
        """
        metric unit of the vertical ruler
        
        Uses values from com.sun.star.awt.FieldUnit
        
        **since**
        
            OOo 3.1
        """
        ...
    @property
    def ZoomType(self) -> int:
        """
        This property defines the zoom type for the document.
        """
        ...
    @property
    def ZoomValue(self) -> int:
        """
        Defines the zoom value to use.
        
        Valid only if the ZoomType is set to com.sun.star.view.DocumentZoomType.BY_VALUE.
        """
        ...


