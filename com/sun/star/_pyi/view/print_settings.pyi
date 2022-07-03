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
# Libre Office Version: 7.3
# Namespace: com.sun.star.view
from abc import ABC

class PrintSettings(ABC):
    """
    Service Class

    provides access to the settings for printing documents.
    
    These settings are printer independent but affect the rendering of the document.

    See Also:
        `API PrintSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1view_1_1PrintSettings.html>`_
    """
    @property
    def PrintAnnotationMode(self) -> int:
        """
        determines how annotations are printed.
        """
        ...
    @property
    def PrintBlackFonts(self) -> bool:
        """
        If TRUE, all characters are printed in black.
        
        It is useful for printing colored text on a b/w printer.
        """
        ...
    @property
    def PrintControls(self) -> bool:
        """
        If TRUE, control shapes are included in printing.
        """
        ...
    @property
    def PrintDrawings(self) -> bool:
        """
        If TRUE, drawing objects (shapes) are included in printing.
        """
        ...
    @property
    def PrintGraphics(self) -> bool:
        """
        If TRUE, graphic objects are included in printing.
        """
        ...
    @property
    def PrintLeftPages(self) -> bool:
        """
        If TRUE, left pages are included in printing.
        """
        ...
    @property
    def PrintPageBackground(self) -> bool:
        """
        If TRUE, the background of the page is printed.
        """
        ...
    @property
    def PrintProspect(self) -> bool:
        """
        If TRUE, the pages are printed in the order of prospects.
        """
        ...
    @property
    def PrintReversed(self) -> bool:
        """
        If TRUE, the pages are printed in reverse order.
        
        The last page is printed first.
        """
        ...
    @property
    def PrintRightPages(self) -> bool:
        """
        If TRUE, right pages are included in printing.
        """
        ...
    @property
    def PrintTables(self) -> bool:
        """
        If TRUE, tables are included in printing.
        """
        ...


