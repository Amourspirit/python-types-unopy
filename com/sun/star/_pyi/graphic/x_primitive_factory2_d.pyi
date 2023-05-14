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
# Namespace: com.sun.star.graphic
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..drawing.x_draw_page import XDrawPage as XDrawPage_b07a0b57
    from ..drawing.x_shape import XShape as XShape_8fd00a3d
    from .x_primitive2_d import XPrimitive2D as XPrimitive2D_d5730c6d

class XPrimitiveFactory2D(XInterface_8f010a43):
    """
    XPrimitiveFactory2D interface.
    
    Use this interface to generate XPrimitive2D instances

    See Also:
        `API XPrimitiveFactory2D <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1graphic_1_1XPrimitiveFactory2D.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.graphic.XPrimitiveFactory2D']

    def createPrimitivesFromXDrawPage(self, xDrawPage: 'XDrawPage_b07a0b57', aParms: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> 'typing.Tuple[XPrimitive2D_d5730c6d, ...]':
        """
        Create primitives from com.sun.star.drawing.XDrawPage.
        """
        ...
    def createPrimitivesFromXShape(self, xShape: 'XShape_8fd00a3d', aParms: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> 'typing.Tuple[XPrimitive2D_d5730c6d, ...]':
        """
        Create primitives from com.sun.star.drawing.XShape.
        """
        ...


