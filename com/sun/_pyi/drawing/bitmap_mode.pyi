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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.2
from typing_extensions import Literal
from enum import Enum


class BitmapMode(Enum):
    """
    Enum Class

    

    See Also:
        `API BitmapMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#ad26489b8cfc631a6aa6a1a59fd2e2356>`_
    """
    NO_REPEAT: Literal['NO_REPEAT']
    """
    the bitmap is painted in its original or selected size.
    """
    REPEAT: Literal['REPEAT']
    """
    the bitmap is repeated over the fill area.
    """
    STRETCH: Literal['STRETCH']
    """
    the bitmap is stretched to fill the area.
    
    The text is stretched so that the longest line goes from the left to the right edge of the shape.
    """

__all__ = ['BitmapMode']

