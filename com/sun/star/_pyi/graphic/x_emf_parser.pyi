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
# Libre Office Version: 7.3
# Namespace: com.sun.star.graphic
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_values import PropertyValues as PropertyValues_d6470ce6
    from ..geometry.real_point2_d import RealPoint2D as RealPoint2D_d6e70c78
    from .x_primitive2_d import XPrimitive2D as XPrimitive2D_d5730c6d

class XEmfParser(XInterface_8f010a43):
    """
    XEmfParser interface.
    
    This interface allows to parse a WMF/EMF/EMF+ stream in form of a sequence of bytes to be parsed into a sequence of XPrimitive2Ds
    
    **since**
    
        LibreOffice 6.0

    See Also:
        `API XEmfParser <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1graphic_1_1XEmfParser.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.graphic.XEmfParser']

    def getDecomposition(self, xEmfStream: object, aAbsolutePath: str, Properties: 'PropertyValues_d6470ce6') -> 'typing.Tuple[XPrimitive2D_d5730c6d, ...]':
        """
        Retrieve decomposed list of simpler primitives.
        """
        ...
    def setSizeHint(self, Size: 'RealPoint2D_d6e70c78') -> None:
        """
        Sets a size hint on this object.
        
        **since**
        
            LibreOffice 7.1
        """
        ...


