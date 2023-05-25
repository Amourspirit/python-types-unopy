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
# Namespace: com.sun.star.ucb
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .fetch_result import FetchResult as FetchResult_98510aab


class XFetchProviderForContentAccess(XInterface_8f010a43):
    """
    provides the possibility to load information offered by a XContentAccess for several rows of a ContentResultSet with a single function call.

    See Also:
        `API XFetchProviderForContentAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XFetchProviderForContentAccess.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.ucb.XFetchProviderForContentAccess'

    def fetchContentIdentifierStrings(self, nRowStartPosition: int, nRowCount: int, bDirection: bool) -> FetchResult_98510aab:
        """
        returns the content identifier strings of the columns of the indicated rows
        """
        ...
    def fetchContentIdentifiers(self, nRowStartPosition: int, nRowCount: int, bDirection: bool) -> FetchResult_98510aab:
        """
        returns the XContentIdentifiers of the columns of the indicated rows
        """
        ...
    def fetchContents(self, nRowStartPosition: int, nRowCount: int, bDirection: bool) -> FetchResult_98510aab:
        """
        returns the XContent s of the columns of the indicated rows
        """
        ...



