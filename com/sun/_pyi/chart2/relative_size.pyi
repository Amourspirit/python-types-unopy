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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class RelativeSize(object):
    """
    Struct Class

    Gives a position relative to some size defined by other means.
    
    Values from 0 to 1 cover the entire reference rectangle. Values may also be greater than one, meaning a bigger size than the reference size. Negative values are not allowed.

    See Also:
        `API RelativeSize <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1RelativeSize.html>`_
    """
    typeName: Literal['com.sun.star.chart2.RelativeSize']

    def __init__(self, Primary: typing.Optional[float] = ..., Secondary: typing.Optional[float] = ...) -> None:
        """
        Constructor

        Arguments:
            Primary (float, optional): Primary value.
            Secondary (float, optional): Secondary value.
        """


    @property
    def Primary(self) -> float:
        """
        The extension in the primary direction.
        
        The direction is defined by the object using this point.
        
        Typically, the direction is determined by an Orientation. Another typical use would be the direction of a given orientation-angle.
        
        The values are relative to the page or an object. Values between 0 and 1 span the complete bounding rectangle of the page/object.
        
        For a western Orientation this is the width.
        """


    @property
    def Secondary(self) -> float:
        """
        The extension in the secondary direction.
        
        The direction is defined by the object using this point.
        
        Typically, the direction is determined by an Orientation. Another typical use would be the direction perpendicular to a given orientation-angle.
        
        The values are relative to the page or an object. Values between 0 and 1 span the complete bounding rectangle of the page/object.
        
        For a western Orientation this is the height.
        """



__all__ = ['RelativeSize']
