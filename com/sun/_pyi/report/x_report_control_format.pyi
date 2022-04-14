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
# Namespace: com.sun.star.report
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ..awt.font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..awt.font_slant import FontSlant as FontSlant_849509ed
    from ..lang.locale import Locale as Locale_70d308fa
    from ..style.vertical_alignment import VerticalAlignment as VerticalAlignment_8d0e12
    from ..util.color import Color as Color_68e908c5

class XReportControlFormat(ABC):
    """
    specifies a format condition for a control.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XReportControlFormat <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1XReportControlFormat.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.report.XReportControlFormat']

    @property
    def CharAutoKerning(self) -> bool:
        """
        optional property to determine whether the kerning tables from the current font are used.
        
        Automatic kerning applies a spacing in between certain pairs of characters to make the text look better.
        """

    @property
    def CharCaseMap(self) -> int:
        """
        optional property which contains the value of the case-mapping of the text for formatting and displaying.
        """

    @property
    def CharColor(self) -> 'Color_68e908c5':
        """
        specifies the text color (RGB) of the control.
        """

    @property
    def CharCombineIsOn(self) -> bool:
        """
        determines whether text is formatted in two lines.
        
        It is linked to the properties CharCombinePrefix and CharCombineSuffix.
        """

    @property
    def CharCombinePrefix(self) -> str:
        """
        contains the prefix (usually parenthesis) before text that is formatted in two lines.
        
        It is linked to the properties CharCombineIsOn and CharCombineSuffix.
        """

    @property
    def CharCombineSuffix(self) -> str:
        """
        contains the suffix (usually parenthesis) after text that is formatted in two lines.
        
        It is linked to the properties CharCombineIsOn and CharCombinePrefix.
        """

    @property
    def CharContoured(self) -> bool:
        """
        specifies if the characters are formatted and displayed with a contour effect.
        """

    @property
    def CharEmphasis(self) -> int:
        """
        contains the font emphasis value as com.sun.star.text.FontEmphasis.
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
        This is the additional height used for subscript or superscript characters in units of percent.
        
        For subscript characters the value is negative and for superscript characters positive.
        """

    @property
    def CharFlash(self) -> bool:
        """
        If this optional property is TRUE, then the characters are flashing.
        """

    @property
    def CharFontCharSet(self) -> int:
        """
        This attribute contains the text encoding of the font as specified in com.sun.star.awt.CharSet.
        """

    @property
    def CharFontCharSetAsian(self) -> int:
        """
        This property contains the text encoding of the font as specified in com.sun.star.awt.CharSet.
        """

    @property
    def CharFontCharSetComplex(self) -> int:
        """
        This property contains the text encoding of the font as specified in com.sun.star.awt.CharSet.
        """

    @property
    def CharFontFamily(self) -> int:
        """
        This attribute contains font family as specified in com.sun.star.awt.FontFamily .
        """

    @property
    def CharFontFamilyAsian(self) -> int:
        """
        This property contains font family as specified in com.sun.star.awt.FontFamily .
        """

    @property
    def CharFontFamilyComplex(self) -> int:
        """
        This property contains font family as specified in com.sun.star.awt.FontFamily .
        """

    @property
    def CharFontName(self) -> str:
        """
        This attribute specifies the name of the font style.
        
        It may contain more than one name separated by comma.
        """

    @property
    def CharFontNameAsian(self) -> str:
        """
        This property specifies the name of the font style.
        
        It may contain more than one name separated by comma.
        """

    @property
    def CharFontNameComplex(self) -> str:
        """
        This property specifies the name of the font style.
        
        It may contain more than one name separated by comma.
        """

    @property
    def CharFontPitch(self) -> int:
        """
        This attribute contains the font pitch as specified in com.sun.star.awt.FontPitch.
        """

    @property
    def CharFontPitchAsian(self) -> int:
        """
        This property contains the font pitch as specified in com.sun.star.awt.FontPitch.
        """

    @property
    def CharFontPitchComplex(self) -> int:
        """
        This property contains the font pitch as specified in com.sun.star.awt.FontPitch.
        """

    @property
    def CharFontStyleName(self) -> str:
        """
        This attribute contains the name of the font style.
        
        This attribute may be empty.
        """

    @property
    def CharFontStyleNameAsian(self) -> str:
        """
        This property contains the name of the font style.
        
        This property may be empty.
        """

    @property
    def CharFontStyleNameComplex(self) -> str:
        """
        This property contains the name of the font style.
        
        This property may be empty.
        """

    @property
    def CharHeight(self) -> float:
        """
        This value contains the height of the characters in point.
        """

    @property
    def CharHeightAsian(self) -> float:
        """
        This value contains the height of the characters in point.
        """

    @property
    def CharHeightComplex(self) -> float:
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
    def CharKerning(self) -> int:
        """
        optional property which contains the value of the kerning of the characters.
        """

    @property
    def CharLocale(self) -> 'Locale_70d308fa':
        """
        contains the value of the locale.
        """

    @property
    def CharLocaleAsian(self) -> 'Locale_70d308fa':
        """
        contains the value of the locale.
        """

    @property
    def CharLocaleComplex(self) -> 'Locale_70d308fa':
        """
        contains the value of the locale.
        """

    @property
    def CharPosture(self) -> 'FontSlant_849509ed':
        """
        This attribute contains the value of the posture of the document.
        """

    @property
    def CharPostureAsian(self) -> 'FontSlant_849509ed':
        """
        This property contains the value of the posture of the document.
        """

    @property
    def CharPostureComplex(self) -> 'FontSlant_849509ed':
        """
        This property contains the value of the posture of the document.
        """

    @property
    def CharRelief(self) -> int:
        """
        specifies the com.sun.star.text.FontRelief value of the text in the control.
        """

    @property
    def CharRotation(self) -> int:
        """
        determines the rotation of a character in degree.
        
        Depending on the implementation only certain values may be allowed.
        """

    @property
    def CharScaleWidth(self) -> int:
        """
        determines the percentage value for scaling the width of characters.
        
        The value refers to the original width which is denoted by 100, and it has to be greater than 0.
        """

    @property
    def CharShadowed(self) -> bool:
        """
        specifies if the characters are formatted and displayed with a shadow effect.
        """

    @property
    def CharStrikeout(self) -> int:
        """
        determines the type of the strike out of the character.
        """

    @property
    def CharUnderline(self) -> int:
        """
        This attribute contains the value for the character underline.
        """

    @property
    def CharUnderlineColor(self) -> 'Color_68e908c5':
        """
        specifies the text line color (RGB) of the control.
        """

    @property
    def CharWeight(self) -> float:
        """
        This attribute contains the value of the font weight.
        """

    @property
    def CharWeightAsian(self) -> float:
        """
        This property contains the value of the font weight.
        """

    @property
    def CharWeightComplex(self) -> float:
        """
        This property contains the value of the font weight.
        """

    @property
    def CharWordMode(self) -> bool:
        """
        If this attribute is TRUE, the underline and strike-through properties are not applied to white spaces.
        """

    @property
    def ControlBackground(self) -> 'Color_68e908c5':
        """
        specifies the background color (RGB) of the control.
        """

    @property
    def ControlBackgroundTransparent(self) -> bool:
        """
        determines if the background color is set to transparent.
        """

    @property
    def ControlTextEmphasis(self) -> int:
        """
        specifies the com.sun.star.text.FontEmphasis value of the text in the control.
        """

    @property
    def FontDescriptor(self) -> 'FontDescriptor_bc110c0a':
        """
        specifies the font attributes of the text in the control.
        """

    @property
    def FontDescriptorAsian(self) -> 'FontDescriptor_bc110c0a':
        """
        specifies the font attributes of the text in the control.
        """

    @property
    def FontDescriptorComplex(self) -> 'FontDescriptor_bc110c0a':
        """
        specifies the font attributes of the text in the control.
        """

    @property
    def HyperLinkName(self) -> str:
        """
        contains the name of the hyperlink (if set).
        """

    @property
    def HyperLinkTarget(self) -> str:
        """
        contains the name of the target for a hyperlink (if set).
        """

    @property
    def HyperLinkURL(self) -> str:
        """
        contains the URL of a hyperlink (if set).
        """

    @property
    def ParaAdjust(self) -> int:
        """
        specifies the horizontal alignment of the text.
        """

    @property
    def UnvisitedCharStyleName(self) -> str:
        """
        contains the character style name for unvisited hyperlinks.
        """

    @property
    def VerticalAlign(self) -> 'VerticalAlignment_8d0e12':
        """
        specifies the vertical alignment of the text in the control.
        """

    @property
    def VisitedCharStyleName(self) -> str:
        """
        contains the character style name for visited hyperlinks.
        """


__all__ = ['XReportControlFormat']

