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
# Namespace: com.sun.star.sheet
import typing
from ..document.settings import Settings as Settings_b2bc0bb8
if typing.TYPE_CHECKING:
    from ..util.color import Color as Color_68e908c5

class DocumentSettings(Settings_b2bc0bb8):
    """
    Service Class

    describes properties that apply to the whole spreadsheet document.
    
    For settings that affect view properties, these settings apply to subsequently created views and are saved with the document, while SpreadsheetViewSettings can be used to alter a specific view that is already open.

    See Also:
        `API DocumentSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1DocumentSettings.html>`_
    """
    @property
    def GridColor(self) -> 'Color_68e908c5':
        """
        specifies the color in which the cell grid is displayed.
        """
    @property
    def HasColumnRowHeaders(self) -> bool:
        """
        enables the column and row headers of the view.
        """
    @property
    def HasSheetTabs(self) -> bool:
        """
        enables the sheet tabs of the view.
        """
    @property
    def IsDocumentShared(self) -> bool:
        """
        enables the document sharing feature (Tools->Share Spreadsheet)
        """
    @property
    def IsOutlineSymbolsSet(self) -> bool:
        """
        enables the display of outline symbols.
        """
    @property
    def IsRasterAxisSynchronized(self) -> bool:
        """
        enables the synchronization of horizontal and vertical grid settings in the user interface.
        """
    @property
    def IsSnapToRaster(self) -> bool:
        """
        enables the restriction of object movement and resizing of drawing objects to the raster.
        """
    @property
    def RasterIsVisible(self) -> bool:
        """
        enables the display of the drawing object raster.
        """
    @property
    def RasterResolutionX(self) -> int:
        """
        specifies the distance between horizontal grid elements in 1/100 mm.
        """
    @property
    def RasterResolutionY(self) -> int:
        """
        specifies the distance between vertical grid elements in 1/100 mm.
        """
    @property
    def RasterSubdivisionX(self) -> int:
        """
        specifies the number of subdivisions between two horizontal grid elements.
        """
    @property
    def RasterSubdivisionY(self) -> int:
        """
        specifies the number of subdivisions between two vertical grid elements.
        """
    @property
    def ShowGrid(self) -> bool:
        """
        enables the display of the cell grid.
        """
    @property
    def ShowNotes(self) -> bool:
        """
        controls whether a marker is shown for notes in cells.
        """
    @property
    def ShowPageBreaks(self) -> bool:
        """
        enables display of page breaks.
        """
    @property
    def ShowZeroValues(self) -> bool:
        """
        enables display of zero-values.
        """


