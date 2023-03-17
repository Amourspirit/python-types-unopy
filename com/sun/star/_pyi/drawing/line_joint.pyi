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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.4
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class LineJoint(Enum):
    """
    Enum

    

    See Also:
        `API LineJoint <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#aa36e7b530c7d0049f623b0effe54d04f>`_
    """
    typeName: str = 'com.sun.star.drawing.LineJoint'

    BEVEL: 'uno.Enum'
    """
    the edges of the thick lines will be joined by lines
    """
    MIDDLE: 'uno.Enum'
    """
    the middle value between the joints is used
    """
    MITER: 'uno.Enum'
    """
    the lines join at intersections
    """
    NONE: 'uno.Enum'
    """
    the area is not filled.
    
    The text size is only defined by the font properties.
    
    Don't animate this text.
    
    the line is hidden.
    
    the joint between lines will not be connected
    
    the line has no special end.
    """
    ROUND: 'uno.Enum'
    """
    the dash is a point
    
    the lines join with an arc
    
    the line will get a half circle as additional cap
    """

