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
    from .x_shape_group import XShapeGroup as XShapeGroup_c8d30c4a
    from .x_shapes import XShapes as XShapes_9a800ab0

class XShapeGrouper(XInterface_8f010a43):
    """
    specifies the group/ungroup functionality.

    See Also:
        `API XShapeGrouper <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XShapeGrouper.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.drawing.XShapeGrouper']

    def group(self, xShapes: 'XShapes_9a800ab0') -> 'XShapeGroup_c8d30c4a':
        """
        groups the Shapes inside a collection.
        
        Grouping of objects in text documents works only if none of the objects has an anchor of type com.sun.star.text.TextContentAnchorType.AS_CHARACTER .
        """
        ...
    def ungroup(self, aGroup: 'XShapeGroup_c8d30c4a') -> None:
        """
        ungroups a given GroupShape.
        """
        ...


