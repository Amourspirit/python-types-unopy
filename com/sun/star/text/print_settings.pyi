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
    from com.sun.star.text.NotePrintMode import NotePrintModeProto  # type: ignore

class PrintSettings(ABC):
    """
    Service Class

    These properties describe the printing of the content of a text document.

    See Also:
        `API PrintSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1PrintSettings.html>`_
    """
    @property
    def PrintAnnotationMode(self) -> NotePrintModeProto:
        """
        determines how notes are printed.
        """
        ...
    @PrintAnnotationMode.setter
    def PrintAnnotationMode(self, value: NotePrintModeProto) -> None:
        ...
    @property
    def PrintBlackFonts(self) -> bool:
        """
        determines if characters are always printed in black.
        """
        ...
    @PrintBlackFonts.setter
    def PrintBlackFonts(self, value: bool) -> None:
        ...
    @property
    def PrintControls(self) -> bool:
        """
        determines if control shapes are printed.
        """
        ...
    @PrintControls.setter
    def PrintControls(self, value: bool) -> None:
        ...
    @property
    def PrintDrawings(self) -> bool:
        """
        determines if shapes are printed.
        """
        ...
    @PrintDrawings.setter
    def PrintDrawings(self, value: bool) -> None:
        ...
    @property
    def PrintEmptyPages(self) -> bool:
        """
        determines if automatically inserted empty pages are printed.
        """
        ...
    @PrintEmptyPages.setter
    def PrintEmptyPages(self, value: bool) -> None:
        ...
    @property
    def PrintFaxName(self) -> str:
        """
        contains the name of the fax.
        """
        ...
    @PrintFaxName.setter
    def PrintFaxName(self, value: str) -> None:
        ...
    @property
    def PrintGraphics(self) -> bool:
        """
        determines if graphic objects are printed
        """
        ...
    @PrintGraphics.setter
    def PrintGraphics(self, value: bool) -> None:
        ...
    @property
    def PrintLeftPages(self) -> bool:
        """
        determines if left pages are printed.
        """
        ...
    @PrintLeftPages.setter
    def PrintLeftPages(self, value: bool) -> None:
        ...
    @property
    def PrintPageBackground(self) -> bool:
        """
        determines if the background color / background graphic of pages is printed.
        """
        ...
    @PrintPageBackground.setter
    def PrintPageBackground(self, value: bool) -> None:
        ...
    @property
    def PrintPaperFromSetup(self) -> bool:
        """
        specifies if the printer paper tray selection of the system printer is used.
        
        If com.sun.star.view.PrintSettings.PaperFromSetup is FALSE, then the paper tray selection of the page styles is used.
        """
        ...
    @PrintPaperFromSetup.setter
    def PrintPaperFromSetup(self, value: bool) -> None:
        ...
    @property
    def PrintProspect(self) -> bool:
        """
        determines if prospect printing is used.
        """
        ...
    @PrintProspect.setter
    def PrintProspect(self, value: bool) -> None:
        ...
    @property
    def PrintReversed(self) -> bool:
        """
        determines if the pages are printed in the reverse order, starting with the last page.
        """
        ...
    @PrintReversed.setter
    def PrintReversed(self, value: bool) -> None:
        ...
    @property
    def PrintRightPages(self) -> bool:
        """
        determines if right pages are printed.
        """
        ...
    @PrintRightPages.setter
    def PrintRightPages(self, value: bool) -> None:
        ...
    @property
    def PrintTables(self) -> bool:
        """
        determines if text tables are printed.
        """
        ...
    @PrintTables.setter
    def PrintTables(self, value: bool) -> None:
        ...