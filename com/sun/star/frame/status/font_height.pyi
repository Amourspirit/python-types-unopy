# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.frame.status
# Libre Office Version: 2024.2
import typing


class FontHeight(object):
    """
    Struct Class

    describes the characteristics of a font.
    
    For example, this can be used to select a font.
    
    **since**
    
        OOo 2.0

    See Also:
        `API FontHeight <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1FontHeight.html>`_
    """
    typeName: str = 'com.sun.star.frame.status.FontHeight'

    def __init__(self, Height: typing.Optional[float] = ..., Prop: typing.Optional[int] = ..., Diff: typing.Optional[float] = ...) -> None:
        """
        Constructor

        Arguments:
            Height (float, optional): Height value.
            Prop (int, optional): Prop value.
            Diff (float, optional): Diff value.
        """
        ...

    @property
    def Height(self) -> float:
        """
        specifies the current height of the font.
        """
        ...
    @Height.setter
    def Height(self, value: float) -> None:
        ...
    @property
    def Prop(self) -> int:
        """
        specifies the height of the font in the measure of the destination.
        """
        ...
    @Prop.setter
    def Prop(self, value: int) -> None:
        ...
    @property
    def Diff(self) -> float:
        """
        specifies the width of the font in the measure of the destination.
        """
        ...
    @Diff.setter
    def Diff(self, value: float) -> None:
        ...

