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
# Namespace: com.sun.star.view
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73


class XPrintable(XInterface_8f010a43):
    """
    offers printing functionality.

    See Also:
        `API XPrintable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1view_1_1XPrintable.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.view.XPrintable'

    def getPrinter(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        """
        The attributes of the current printer are used for formatting.
        """
        ...
    def print(self, xOptions: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        """
        prints the object.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def setPrinter(self, aPrinter: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        """
        assigns a new printer to the object.
        
        Setting a new printer will cause reformatting.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...


