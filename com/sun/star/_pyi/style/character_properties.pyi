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
# Namespace: com.sun.star.style
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ..awt.font_slant import FontSlant as FontSlant_849509ed
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
    from ..lang.locale import Locale as Locale_70d308fa
    from ..table.border_line2 import BorderLine2 as BorderLine2_af200b28
    from ..table.shadow_format import ShadowFormat as ShadowFormat_bb840bdf
    from ..util.color import Color as Color_68e908c5

class CharacterProperties(ABC):
    """
    Service Class

    This is a set of properties to describe the style of characters.
    
    **since**
    
        LibreOffice 4.3

    See Also:
        `API CharacterProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1style_1_1CharacterProperties.html>`_
    """
    @property
    def CharInteropGrabBag(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        Grab bag of character properties, used as a string-any map for interim interop purposes.
        
        This property is intentionally not handled by the ODF filter. Any member that should be handled there should be first moved out from this grab bag to a separate property.
        
        **since**
        
            LibreOffice 4.3
        """
    @property
    def CharStyleNames(self) -> 'typing.Tuple[str, ...]':
        """
        This optional property specifies the names of the all styles applied to the font.
        
        It is not guaranteed that the order in the sequence reflects the order of the evaluation of the character style attributes.
        
        **since**
        
            OOo 1.1.2
        """
    @property
    def CharAutoKerning(self) -> bool:
        """
        This optional property determines whether the kerning tables from the current font are used.
        
        Automatic kerning applies a spacing in between certain pairs of characters to make the text look better.
        """
    @property
    def CharBackColor(self) -> 'Color_68e908c5':
        """
        This optional property contains the text background color.
        """
    @property
    def CharBackTransparent(self) -> bool:
        """
        This property determines if the text background color is set to transparent.
        """
    @property
    def CharBorderDistance(self) -> int:
        """
        This property contains the distance from the border to the object.
        
        **since**
        
            LibreOffice 4.2
        """
    @property
    def CharBottomBorder(self) -> 'BorderLine2_af200b28':
        """
        This property contains the bottom border of the object.
        
        **since**
        
            LibreOffice 4.2
        """
    @property
    def CharBottomBorderDistance(self) -> int:
        """
        This property contains the distance from the bottom border to the object.
        
        **since**
        
            LibreOffice 4.2
        """
    @property
    def CharCaseMap(self) -> int:
        """
        This optional property contains the value of the case-mapping of the text for formatting and displaying.
        """
    @property
    def CharColor(self) -> 'Color_68e908c5':
        """
        This property contains the value of the text color.
        """
    @property
    def CharColorTheme(self) -> int:
        """
        If available, keeps the color theme index, so that the character can be re-colored easily based on a theme.
        
        **since**
        
            LibreOffice 7.3
        """
    @property
    def CharColorTintOrShade(self) -> int:
        """
        Tint or shade of the character color.
        
        **since**
        
            LibreOffice 7.3
        """
    @property
    def CharCombineIsOn(self) -> bool:
        """
        This optional property determines whether text is formatted in two lines.
        
        It is linked to the properties CharCombinePrefix and CharCombineSuffix.
        """
    @property
    def CharCombinePrefix(self) -> str:
        """
        This optional property contains the prefix (usually parenthesis) before text that is formatted in two lines.
        
        It is linked to the properties CharCombineIsOn and CharCombineSuffix.
        """
    @property
    def CharCombineSuffix(self) -> str:
        """
        This optional property contains the suffix (usually parenthesis) after text that is formatted in two lines.
        
        It is linked to the properties CharCombineIsOn and CharCombinePrefix.
        """
    @property
    def CharContoured(self) -> bool:
        """
        This optional property specifies if the characters are formatted and displayed with a contour effect.
        """
    @property
    def CharCrossedOut(self) -> bool:
        """
        This property is TRUE if the characters are crossed out.
        """
    @property
    def CharEmphasis(self) -> int:
        """
        This optional property contains the font emphasis value.
        """
    @property
    def CharEscapement(self) -> int:
        """
        specifies the percentage by which to raise/lower superscript/subscript characters.
        
        Negative values denote subscripts and positive values superscripts.
        """
    @property
    def CharEscapementHeight(self) -> int:
        """
        This is the relative height used for subscript or superscript characters in units of percent.
        
        The value 100 denotes the original height of the characters.
        """
    @property
    def CharFlash(self) -> bool:
        """
        If this optional property is TRUE, then the characters are flashing.
        """
    @property
    def CharFontCharSet(self) -> int:
        """
        This property contains the text encoding of the font.
        """
    @property
    def CharFontFamily(self) -> int:
        """
        This property contains font family.
        """
    @property
    def CharFontName(self) -> str:
        """
        This property specifies the name of the font style.
        
        It may contain more than one name separated by comma.
        """
    @property
    def CharFontPitch(self) -> int:
        """
        This property contains the font pitch.
        """
    @property
    def CharFontStyleName(self) -> str:
        """
        This property contains the name of the font style.
        
        This property may be empty.
        """
    @property
    def CharFontType(self) -> int:
        """
        This optional property specifies the fundamental technology of the font.
        """
    @property
    def CharHeight(self) -> float:
        """
        This value contains the height of the characters in point.
        """
    @property
    def CharHidden(self) -> bool:
        """
        If this optional property is TRUE, then the characters are invisible.
        
        **since**
        
            OOo 2.0
        """
    @property
    def CharHighlight(self) -> 'Color_68e908c5':
        """
        Determines the color of the highlight.
        
        **since**
        
            LibreOffice 4.2
        """
    @property
    def CharKeepTogether(self) -> bool:
        """
        This optional property marks a range of characters to prevent it from being broken into two lines.
        
        A line break is applied before the range of characters if the layout makes a break necessary within the range.
        """
    @property
    def CharKerning(self) -> int:
        """
        This optional property contains the value of the kerning of the characters.
        """
    @property
    def CharLeftBorder(self) -> 'BorderLine2_af200b28':
        """
        This property contains the left border of the object.
        
        **since**
        
            LibreOffice 4.2
        """
    @property
    def CharLeftBorderDistance(self) -> int:
        """
        This property contains the distance from the left border to the object.
        
        **since**
        
            LibreOffice 4.2
        """
    @property
    def CharLocale(self) -> 'Locale_70d308fa':
        """
        This property contains the value of the locale.
        """
    @property
    def CharNoHyphenation(self) -> bool:
        """
        This optional property determines if the word can be hyphenated at the character.
        """
    @property
    def CharNoLineBreak(self) -> bool:
        """
        This optional property marks a range of characters to ignore a line break in this area.
        
        A line break is applied behind the range of characters if the layout makes a break necessary within the range. That means that the text may go through the border.
        """
    @property
    def CharPosture(self) -> 'FontSlant_849509ed':
        """
        This property contains the value of the posture of the document.
        """
    @property
    def CharRelief(self) -> int:
        """
        This optional property contains the relief style of the characters.
        """
    @property
    def CharRightBorder(self) -> 'BorderLine2_af200b28':
        """
        This property contains the right border of the object.
        
        **since**
        
            LibreOffice 4.2
        """
    @property
    def CharRightBorderDistance(self) -> int:
        """
        This property contains the distance from the right border to the object.
        
        **since**
        
            LibreOffice 4.2
        """
    @property
    def CharRotation(self) -> int:
        """
        This optional property determines the rotation of a character in tenths of a degree.
        
        Depending on the implementation only certain values may be allowed.
        """
    @property
    def CharRotationIsFitToLine(self) -> bool:
        """
        This optional property determines whether the text formatting tries to fit rotated text into the surrounded line height.
        """
    @property
    def CharScaleWidth(self) -> int:
        """
        This optional property determines the percentage value for scaling the width of characters.
        
        The value refers to the original width which is denoted by 100, and it has to be greater than 0.
        """
    @property
    def CharShadingValue(self) -> int:
        """
        This optional property contains the text shading value.
        """
    @property
    def CharShadowFormat(self) -> 'ShadowFormat_bb840bdf':
        """
        Determines the type, color, and width of the shadow.
        
        **since**
        
            LibreOffice 4.2
        """
    @property
    def CharShadowed(self) -> bool:
        """
        This optional property specifies if the characters are formatted and displayed with a shadow effect.
        """
    @property
    def CharStrikeout(self) -> int:
        """
        This property determines the type of the strike out of the character.
        """
    @property
    def CharStyleName(self) -> str:
        """
        This optional property specifies the name of the style of the font.
        """
    @property
    def CharTopBorder(self) -> 'BorderLine2_af200b28':
        """
        This property contains the top border of the object.
        
        **since**
        
            LibreOffice 4.2
        """
    @property
    def CharTopBorderDistance(self) -> int:
        """
        This property contains the distance from the top border to the object.
        
        **since**
        
            LibreOffice 4.2
        """
    @property
    def CharTransparence(self) -> int:
        """
        This is the transparency of the character text.
        
        The value 100 means entirely transparent, while 0 means not transparent at all.
        
        **since**
        
            LibreOffice 7.0
        """
    @property
    def CharUnderline(self) -> int:
        """
        This property contains the value for the character underline.
        """
    @property
    def CharUnderlineColor(self) -> 'Color_68e908c5':
        """
        This property contains the color of the underline for the characters.
        """
    @property
    def CharUnderlineHasColor(self) -> bool:
        """
        This property specifies if the property CharUnderlineColor is used for an underline.
        """
    @property
    def CharWeight(self) -> float:
        """
        This property contains the value of the font weight.
        """
    @property
    def CharWordMode(self) -> bool:
        """
        If this property is TRUE, the underline and strike-through properties are not applied to white spaces.
        """
    @property
    def HyperLinkName(self) -> str:
        """
        This optional property contains the name of the hyperlink.
        """
    @property
    def HyperLinkTarget(self) -> str:
        """
        This optional property contains the name of the target for a hyperlink.
        """
    @property
    def HyperLinkURL(self) -> str:
        """
        This optional property contains the URL of a hyperlink.
        """
    @property
    def RubyAdjust(self) -> int:
        """
        This optional property determines the adjustment of the ruby .
        """
    @property
    def RubyCharStyleName(self) -> str:
        """
        This optional property contains the name of the character style that is applied to RubyText.
        """
    @property
    def RubyIsAbove(self) -> bool:
        """
        This optional property determines whether the ruby text is printed above/left or below/right of the text.
        
        This property is replaced by RubyPosition.
        """
    @property
    def RubyPosition(self) -> int:
        """
        This optional property determines the position of the ruby .
        
        **since**
        
            LibreOffice 6.1
        """
    @property
    def RubyText(self) -> str:
        """
        This optional property contains the text that is set as ruby.
        """
    @property
    def TextUserDefinedAttributes(self) -> 'XNameContainer_cb90e47':
        """
        This property stores XML attributes.
        
        They will be saved to and restored from automatic styles inside XML files.
        """
    @property
    def UnvisitedCharStyleName(self) -> str:
        """
        This optional property contains the character style name for unvisited hyperlinks.
        """
    @property
    def VisitedCharStyleName(self) -> str:
        """
        This optional property contains the character style name for visited hyperlinks.
        """

