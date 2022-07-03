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
# Namespace: com.sun.star.rendering
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class FontMetrics(object):
    """
    Struct Class

    Metrics global to the font, i.e.
    
    not specific to single glyphs. The font height is defined as ascent+descent+internalLeading, and therefore not explicitly included here.
    
    Please note that when querying FontMetrics from an XCanvasFont interface, all values here are given relative to the font cell size. That means, the referenceCharWidth and/or ascent+descent+internalLeading will approximately (rounded to integer device resolution, or exactly, if fractional font rendering is enabled) match the referenceAdvancement/cellSize members of the FontRequest for which the XCanvasFont was queried. Please be aware that the values returned in this structure only map one-to-one to device pixel, if the combined rendering transformation for text output equals the identity transformation. Otherwise, the text output (and thus the resulting metrics) will be subject to that transformation. Depending on the underlying font technology, actual device output might be off by up to one device pixel from the transformed metrics.
    
    **since**
    
        OOo 2.0

    See Also:
        `API FontMetrics <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1FontMetrics.html>`_
    """
    typeName: Literal['com.sun.star.rendering.FontMetrics']

    def __init__(self, Ascent: typing.Optional[float] = ..., Descent: typing.Optional[float] = ..., InternalLeading: typing.Optional[float] = ..., ExternalLeading: typing.Optional[float] = ..., ReferenceCharSize: typing.Optional[float] = ..., UnderlineOffset: typing.Optional[float] = ..., StrikeThroughOffset: typing.Optional[float] = ...) -> None:
        """
        Constructor

        Arguments:
            Ascent (float, optional): Ascent value.
            Descent (float, optional): Descent value.
            InternalLeading (float, optional): InternalLeading value.
            ExternalLeading (float, optional): ExternalLeading value.
            ReferenceCharSize (float, optional): ReferenceCharSize value.
            UnderlineOffset (float, optional): UnderlineOffset value.
            StrikeThroughOffset (float, optional): StrikeThroughOffset value.
        """
        ...


    @property
    def Ascent(self) -> float:
        """
        Ascent (above the baseline) part of the font.
        """
        ...


    @property
    def Descent(self) -> float:
        """
        Descent (below the baseline) part of the font.
        """
        ...


    @property
    def InternalLeading(self) -> float:
        """
        Extra space above ascent.
        """
        ...


    @property
    def ExternalLeading(self) -> float:
        """
        Extra space outside the font cells.
        
        It should not contain ink marks and is typically used by the font designer to modify the line distance.
        """
        ...


    @property
    def ReferenceCharSize(self) -> float:
        """
        This value specifies the reference character width of the font.
        
        It's roughly equivalent to the average width of all characters, and if one needs a font with double character width, the referenceCharSize should be doubled.
        """
        ...


    @property
    def UnderlineOffset(self) -> float:
        """
        Specifies the offset to be added to the baseline when drawing underlined text.
        """
        ...


    @property
    def StrikeThroughOffset(self) -> float:
        """
        Specifies the offset to be added to the baseline when striking through the text.
        """
        ...


