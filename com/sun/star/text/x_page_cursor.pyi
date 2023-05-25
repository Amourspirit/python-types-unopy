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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.text
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XPageCursor(XInterface_8f010a43):
    """
    makes it possible to perform cursor movements between pages.

    See Also:
        `API XPageCursor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XPageCursor.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.text.XPageCursor'

    def getPage(self) -> int:
        """
        """
        ...
    def jumpToEndOfPage(self) -> bool:
        """
        moves the cursor to the end of the current page.
        """
        ...
    def jumpToFirstPage(self) -> bool:
        """
        moves the cursor to the first page.
        """
        ...
    def jumpToLastPage(self) -> bool:
        """
        moves the cursor to the last page.
        """
        ...
    def jumpToNextPage(self) -> bool:
        """
        moves the cursor to the next page.
        """
        ...
    def jumpToPage(self, nPage: int) -> bool:
        """
        moves the cursor to the specified page.
        """
        ...
    def jumpToPreviousPage(self) -> bool:
        """
        moves the cursor to the previous page.
        """
        ...
    def jumpToStartOfPage(self) -> bool:
        """
        moves the cursor to the start of the current page.
        """
        ...



