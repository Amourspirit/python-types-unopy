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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.drawing
import typing
from ..style.character_properties import CharacterProperties as CharacterProperties_1d4f0ef3
from ..style.character_properties_asian import CharacterPropertiesAsian as CharacterPropertiesAsian_6d8a10df
from ..style.character_properties_complex import CharacterPropertiesComplex as CharacterPropertiesComplex_90ca11cb
from ..style.paragraph_properties import ParagraphProperties as ParagraphProperties_1e240efc
from ..style.paragraph_properties_asian import ParagraphPropertiesAsian as ParagraphPropertiesAsian_6e8c10e8
from ..style.paragraph_properties_complex import ParagraphPropertiesComplex as ParagraphPropertiesComplex_91de11d4
if typing.TYPE_CHECKING:
    from ..container.x_index_replace import XIndexReplace as XIndexReplace_feed0dd7
    from .text_animation_direction import TextAnimationDirection as TextAnimationDirection_6c5510da
    from .text_animation_kind import TextAnimationKind as TextAnimationKind_1c710ebf
    from .text_fit_to_size_type import TextFitToSizeType as TextFitToSizeType_1bd90ebc
    from .text_horizontal_adjust import TextHorizontalAdjust as TextHorizontalAdjust_4cf9102e
    from .text_vertical_adjust import TextVerticalAdjust as TextVerticalAdjust_2c160f3e
    from ..text.writing_mode import WritingMode as WritingMode_a6dd0b36
    from ..text.x_text_columns import XTextColumns as XTextColumns_b17f0bab

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
    @property
    def NumberingRules(self) -> 'XIndexReplace_feed0dd7':
        """
        describes the numbering levels.
        
        The different rules accessible with this com.sun.star.container.XIndexReplace interface are sequences of property values as described in the service com.sun.star.style.NumberingRule.
        """
        ...
    @property
    def TextAnimationAmount(self) -> int:
        """
        This is the number of pixels the text is moved in each animation step.
        """
        ...
    @property
    def TextAnimationCount(self) -> int:
        """
        This number defines how many times the text animation is repeated.
        
        If this is set to zero, the repeat is endless.
        """
        ...
    @property
    def TextAnimationDelay(self) -> int:
        """
        This is the delay in thousandths of a second between each of the animation steps.
        """
        ...
    @property
    def TextAnimationDirection(self) -> 'TextAnimationDirection_6c5510da':
        """
        This enumeration defines the direction in which the text moves.
        """
        ...
    @property
    def TextAnimationKind(self) -> 'TextAnimationKind_1c710ebf':
        """
        This value defines the type of animation.
        """
        ...
    @property
    def TextAnimationStartInside(self) -> bool:
        """
        If this value is TRUE, the text is visible at the start of the animation.
        """
        ...
    @property
    def TextAnimationStopInside(self) -> bool:
        """
        If this value is TRUE, the text is visible at the end of the animation.
        """
        ...
    @property
    def TextAutoGrowHeight(self) -> bool:
        """
        If this value is TRUE, the height of the Shape is automatically expanded/shrunk when text is added to or removed from the Shape.
        """
        ...
    @property
    def TextAutoGrowWidth(self) -> bool:
        """
        If this value is TRUE, the width of the Shape is automatically expanded/shrunk when text is added to or removed from the Shape.
        """
        ...
    @property
    def TextColumns(self) -> 'XTextColumns_b17f0bab':
        """
        Column layout properties for the text.
        
        **since**
        
            LibreOffice 7.2
        """
        ...
    @property
    def TextContourFrame(self) -> bool:
        """
        If this value is TRUE, the left edge of every line of text is aligned with the left edge of this Shape.
        """
        ...
    @property
    def TextFitToSize(self) -> 'TextFitToSizeType_1bd90ebc':
        """
        With this set to a value other than NONE, the text inside of the Shape is stretched or scaled to fit into the Shape.
        """
        ...
    @property
    def TextHorizontalAdjust(self) -> 'TextHorizontalAdjust_4cf9102e':
        """
        adjusts the horizontal position of the text inside of the Shape.
        """
        ...
    @property
    def TextLeftDistance(self) -> int:
        """
        This is the distance from the left edge of the Shape to the left edge of the text.
        
        This is only useful if Text.TextHorizontalAdjust is BLOCK or STRETCH or if Text.TextFitSize is TRUE.
        """
        ...
    @property
    def TextLowerDistance(self) -> int:
        """
        This is the distance from the lower edge of the Shape to the lower edge of the text.
        
        This is only useful if Text.TextVerticalAdjust is BLOCK or if Text.TextFitSize is TRUE.
        """
        ...
    @property
    def TextMaximumFrameHeight(self) -> int:
        """
        with this property you can set the maximum height for a shape with text.
        
        On edit, the auto grow feature will not grow the object higher than the value of this property.
        """
        ...
    @property
    def TextMaximumFrameWidth(self) -> int:
        """
        with this property you can set the maximum width for a shape with text.
        
        On edit, the auto grow feature will not grow the objects wider than the value of this property.
        """
        ...
    @property
    def TextMinimumFrameHeight(self) -> int:
        """
        with this property you can set the minimum height for a shape with text.
        
        On edit, the auto grow feature will not shrink the objects height smaller than the value of this property.
        """
        ...
    @property
    def TextMinimumFrameWidth(self) -> int:
        """
        with this property you can set the minimum width for a shape with text.
        
        On edit, the auto grow feature will not shrink the object width smaller than the value of this property.
        """
        ...
    @property
    def TextRightDistance(self) -> int:
        """
        This is the distance from the right edge of the Shape to the right edge of the text.
        
        This is only useful if Text.TextHorizontalAdjust is BLOCK or STRETCH or if Text.TextFitSize is TRUE.
        """
        ...
    @property
    def TextUpperDistance(self) -> int:
        """
        This is the distance from the upper edge of the Shape to the upper edge of the text.
        
        This is only useful if Text.TextVerticalAdjust is BLOCK or if Text.TextFitSize is TRUE.
        """
        ...
    @property
    def TextVerticalAdjust(self) -> 'TextVerticalAdjust_2c160f3e':
        """
        adjusts the vertical position of the text inside of the Shape.
        """
        ...
    @property
    def TextWritingMode(self) -> 'WritingMode_a6dd0b36':
        """
        This value selects the writing mode for the text.
        """
        ...


