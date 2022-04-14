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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.drawing
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e

class XCustomShapeHandle(XInterface_8f010a43):
    """
    The XCustomShapeHandle.

    See Also:
        `API XCustomShapeHandle <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XCustomShapeHandle.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.drawing.XCustomShapeHandle']

    def getPosition(self) -> 'Point_5fb2085e':
        """
        is getting the actual handle position
        """
    def setControllerPosition(self, aPoint: 'Point_5fb2085e') -> None:
        """
        is setting a new position for the handle
        """

__all__ = ['XCustomShapeHandle']

