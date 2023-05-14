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
        ...
    @GridColor.setter
    def GridColor(self, value: 'Color_68e908c5') -> None:
        ...
    @property
    def HasColumnRowHeaders(self) -> bool:
        """
        enables the column and row headers of the view.
        """
        ...
    @HasColumnRowHeaders.setter
    def HasColumnRowHeaders(self, value: bool) -> None:
        ...
    @property
    def HasSheetTabs(self) -> bool:
        """
        enables the sheet tabs of the view.
        """
        ...
    @HasSheetTabs.setter
    def HasSheetTabs(self, value: bool) -> None:
        ...
    @property
    def IsDocumentShared(self) -> bool:
        """
        enables the document sharing feature (Tools->Share Spreadsheet)
        """
        ...
    @IsDocumentShared.setter
    def IsDocumentShared(self, value: bool) -> None:
        ...
    @property
    def IsOutlineSymbolsSet(self) -> bool:
        """
        enables the display of outline symbols.
        """
        ...
    @IsOutlineSymbolsSet.setter
    def IsOutlineSymbolsSet(self, value: bool) -> None:
        ...
    @property
    def IsRasterAxisSynchronized(self) -> bool:
        """
        enables the synchronization of horizontal and vertical grid settings in the user interface.
        """
        ...
    @IsRasterAxisSynchronized.setter
    def IsRasterAxisSynchronized(self, value: bool) -> None:
        ...
    @property
    def IsSnapToRaster(self) -> bool:
        """
        enables the restriction of object movement and resizing of drawing objects to the raster.
        """
        ...
    @IsSnapToRaster.setter
    def IsSnapToRaster(self, value: bool) -> None:
        ...
    @property
    def RasterIsVisible(self) -> bool:
        """
        enables the display of the drawing object raster.
        """
        ...
    @RasterIsVisible.setter
    def RasterIsVisible(self, value: bool) -> None:
        ...
    @property
    def RasterResolutionX(self) -> int:
        """
        specifies the distance between horizontal grid elements in 1/100 mm.
        """
        ...
    @RasterResolutionX.setter
    def RasterResolutionX(self, value: int) -> None:
        ...
    @property
    def RasterResolutionY(self) -> int:
        """
        specifies the distance between vertical grid elements in 1/100 mm.
        """
        ...
    @RasterResolutionY.setter
    def RasterResolutionY(self, value: int) -> None:
        ...
    @property
    def RasterSubdivisionX(self) -> int:
        """
        specifies the number of subdivisions between two horizontal grid elements.
        """
        ...
    @RasterSubdivisionX.setter
    def RasterSubdivisionX(self, value: int) -> None:
        ...
    @property
    def RasterSubdivisionY(self) -> int:
        """
        specifies the number of subdivisions between two vertical grid elements.
        """
        ...
    @RasterSubdivisionY.setter
    def RasterSubdivisionY(self, value: int) -> None:
        ...
    @property
    def ShowGrid(self) -> bool:
        """
        enables the display of the cell grid.
        """
        ...
    @ShowGrid.setter
    def ShowGrid(self, value: bool) -> None:
        ...
    @property
    def ShowNotes(self) -> bool:
        """
        controls whether a marker is shown for notes in cells.
        """
        ...
    @ShowNotes.setter
    def ShowNotes(self, value: bool) -> None:
        ...
    @property
    def ShowPageBreaks(self) -> bool:
        """
        enables display of page breaks.
        """
        ...
    @ShowPageBreaks.setter
    def ShowPageBreaks(self, value: bool) -> None:
        ...
    @property
    def ShowZeroValues(self) -> bool:
        """
        enables display of zero-values.
        """
        ...
    @ShowZeroValues.setter
    def ShowZeroValues(self, value: bool) -> None:
        ...

