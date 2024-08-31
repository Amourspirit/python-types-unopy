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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.drawing
from __future__ import annotations
import typing
from ..style.character_properties import CharacterProperties as CharacterProperties_1d4f0ef3
from ..style.character_properties_asian import CharacterPropertiesAsian as CharacterPropertiesAsian_6d8a10df
from ..style.character_properties_complex import CharacterPropertiesComplex as CharacterPropertiesComplex_90ca11cb
from ..style.paragraph_properties import ParagraphProperties as ParagraphProperties_1e240efc
from ..style.paragraph_properties_asian import ParagraphPropertiesAsian as ParagraphPropertiesAsian_6e8c10e8
from ..style.paragraph_properties_complex import ParagraphPropertiesComplex as ParagraphPropertiesComplex_91de11d4
if typing.TYPE_CHECKING:
    from ..container.x_index_replace import XIndexReplace as XIndexReplace_feed0dd7
    from ..text.x_text_columns import XTextColumns as XTextColumns_b17f0bab
    from com.sun.star.drawing.TextAnimationDirection import TextAnimationDirectionProto  # type: ignore
    from com.sun.star.drawing.TextAnimationKind import TextAnimationKindProto  # type: ignore
    from com.sun.star.drawing.TextFitToSizeType import TextFitToSizeTypeProto  # type: ignore
    from com.sun.star.drawing.TextHorizontalAdjust import TextHorizontalAdjustProto  # type: ignore
    from com.sun.star.drawing.TextVerticalAdjust import TextVerticalAdjustProto  # type: ignore
    from com.sun.star.text.WritingMode import WritingModeProto  # type: ignore

class TextProperties(CharacterProperties_1d4f0ef3, CharacterPropertiesAsian_6d8a10df, CharacterPropertiesComplex_90ca11cb, ParagraphProperties_1e240efc, ParagraphPropertiesAsian_6e8c10e8, ParagraphPropertiesComplex_91de11d4):
    """
    Service Class

    This is a set of properties to describe the style for rendering the text area inside a shape.
    
    **since**
    
        LibreOffice 7.2

    See Also:
        `API TextProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1TextProperties.html>`_
    """
    @property
    def IsNumbering(self) -> bool:
        """
        If this is TRUE, numbering is ON for the text of this Shape.
        """
        ...
    @IsNumbering.setter
    def IsNumbering(self, value: bool) -> None:
        ...
    @property
    def NumberingRules(self) -> XIndexReplace_feed0dd7:
        """
        describes the numbering levels.
        
        The different rules accessible with this com.sun.star.container.XIndexReplace interface are sequences of property values as described in the service com.sun.star.style.NumberingRule.
        """
        ...
    @NumberingRules.setter
    def NumberingRules(self, value: XIndexReplace_feed0dd7) -> None:
        ...
    @property
    def TextAnimationAmount(self) -> int:
        """
        This is the number of pixels the text is moved in each animation step.
        """
        ...
    @TextAnimationAmount.setter
    def TextAnimationAmount(self, value: int) -> None:
        ...
    @property
    def TextAnimationCount(self) -> int:
        """
        This number defines how many times the text animation is repeated.
        
        If this is set to zero, the repeat is endless.
        """
        ...
    @TextAnimationCount.setter
    def TextAnimationCount(self, value: int) -> None:
        ...
    @property
    def TextAnimationDelay(self) -> int:
        """
        This is the delay in thousandths of a second between each of the animation steps.
        """
        ...
    @TextAnimationDelay.setter
    def TextAnimationDelay(self, value: int) -> None:
        ...
    @property
    def TextAnimationDirection(self) -> TextAnimationDirectionProto:
        """
        This enumeration defines the direction in which the text moves.
        """
        ...
    @TextAnimationDirection.setter
    def TextAnimationDirection(self, value: TextAnimationDirectionProto) -> None:
        ...
    @property
    def TextAnimationKind(self) -> TextAnimationKindProto:
        """
        This value defines the type of animation.
        """
        ...
    @TextAnimationKind.setter
    def TextAnimationKind(self, value: TextAnimationKindProto) -> None:
        ...
    @property
    def TextAnimationStartInside(self) -> bool:
        """
        If this value is TRUE, the text is visible at the start of the animation.
        """
        ...
    @TextAnimationStartInside.setter
    def TextAnimationStartInside(self, value: bool) -> None:
        ...
    @property
    def TextAnimationStopInside(self) -> bool:
        """
        If this value is TRUE, the text is visible at the end of the animation.
        """
        ...
    @TextAnimationStopInside.setter
    def TextAnimationStopInside(self, value: bool) -> None:
        ...
    @property
    def TextAutoGrowHeight(self) -> bool:
        """
        If this value is TRUE, the height of the Shape is automatically expanded/shrunk when text is added to or removed from the Shape.
        """
        ...
    @TextAutoGrowHeight.setter
    def TextAutoGrowHeight(self, value: bool) -> None:
        ...
    @property
    def TextAutoGrowWidth(self) -> bool:
        """
        If this value is TRUE, the width of the Shape is automatically expanded/shrunk when text is added to or removed from the Shape.
        """
        ...
    @TextAutoGrowWidth.setter
    def TextAutoGrowWidth(self, value: bool) -> None:
        ...
    @property
    def TextColumns(self) -> XTextColumns_b17f0bab:
        """
        Column layout properties for the text.
        
        **since**
        
            LibreOffice 7.2
        """
        ...
    @TextColumns.setter
    def TextColumns(self, value: XTextColumns_b17f0bab) -> None:
        ...
    @property
    def TextContourFrame(self) -> bool:
        """
        If this value is TRUE, the left edge of every line of text is aligned with the left edge of this Shape.
        """
        ...
    @TextContourFrame.setter
    def TextContourFrame(self, value: bool) -> None:
        ...
    @property
    def TextFitToSize(self) -> TextFitToSizeTypeProto:
        """
        With this set to a value other than NONE, the text inside of the Shape is stretched or scaled to fit into the Shape.
        """
        ...
    @TextFitToSize.setter
    def TextFitToSize(self, value: TextFitToSizeTypeProto) -> None:
        ...
    @property
    def TextHorizontalAdjust(self) -> TextHorizontalAdjustProto:
        """
        adjusts the horizontal position of the text inside of the Shape.
        """
        ...
    @TextHorizontalAdjust.setter
    def TextHorizontalAdjust(self, value: TextHorizontalAdjustProto) -> None:
        ...
    @property
    def TextLeftDistance(self) -> int:
        """
        This is the distance from the left edge of the Shape to the left edge of the text.
        
        This is only useful if Text.TextHorizontalAdjust is BLOCK or STRETCH or if Text.TextFitSize is TRUE.
        """
        ...
    @TextLeftDistance.setter
    def TextLeftDistance(self, value: int) -> None:
        ...
    @property
    def TextLowerDistance(self) -> int:
        """
        This is the distance from the lower edge of the Shape to the lower edge of the text.
        
        This is only useful if Text.TextVerticalAdjust is BLOCK or if Text.TextFitSize is TRUE.
        """
        ...
    @TextLowerDistance.setter
    def TextLowerDistance(self, value: int) -> None:
        ...
    @property
    def TextMaximumFrameHeight(self) -> int:
        """
        with this property you can set the maximum height for a shape with text.
        
        On edit, the auto grow feature will not grow the object higher than the value of this property.
        """
        ...
    @TextMaximumFrameHeight.setter
    def TextMaximumFrameHeight(self, value: int) -> None:
        ...
    @property
    def TextMaximumFrameWidth(self) -> int:
        """
        with this property you can set the maximum width for a shape with text.
        
        On edit, the auto grow feature will not grow the objects wider than the value of this property.
        """
        ...
    @TextMaximumFrameWidth.setter
    def TextMaximumFrameWidth(self, value: int) -> None:
        ...
    @property
    def TextMinimumFrameHeight(self) -> int:
        """
        with this property you can set the minimum height for a shape with text.
        
        On edit, the auto grow feature will not shrink the objects height smaller than the value of this property.
        """
        ...
    @TextMinimumFrameHeight.setter
    def TextMinimumFrameHeight(self, value: int) -> None:
        ...
    @property
    def TextMinimumFrameWidth(self) -> int:
        """
        with this property you can set the minimum width for a shape with text.
        
        On edit, the auto grow feature will not shrink the object width smaller than the value of this property.
        """
        ...
    @TextMinimumFrameWidth.setter
    def TextMinimumFrameWidth(self, value: int) -> None:
        ...
    @property
    def TextRightDistance(self) -> int:
        """
        This is the distance from the right edge of the Shape to the right edge of the text.
        
        This is only useful if Text.TextHorizontalAdjust is BLOCK or STRETCH or if Text.TextFitSize is TRUE.
        """
        ...
    @TextRightDistance.setter
    def TextRightDistance(self, value: int) -> None:
        ...
    @property
    def TextUpperDistance(self) -> int:
        """
        This is the distance from the upper edge of the Shape to the upper edge of the text.
        
        This is only useful if Text.TextVerticalAdjust is BLOCK or if Text.TextFitSize is TRUE.
        """
        ...
    @TextUpperDistance.setter
    def TextUpperDistance(self, value: int) -> None:
        ...
    @property
    def TextVerticalAdjust(self) -> TextVerticalAdjustProto:
        """
        adjusts the vertical position of the text inside of the Shape.
        """
        ...
    @TextVerticalAdjust.setter
    def TextVerticalAdjust(self, value: TextVerticalAdjustProto) -> None:
        ...
    @property
    def TextWritingMode(self) -> WritingModeProto:
        """
        This value selects the writing mode for the text.
        """
        ...
    @TextWritingMode.setter
    def TextWritingMode(self, value: WritingModeProto) -> None:
        ...