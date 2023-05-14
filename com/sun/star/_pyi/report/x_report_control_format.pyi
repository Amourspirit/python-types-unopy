# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
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
        ...
    @CharAutoKerning.setter
    def CharAutoKerning(self, value: bool) -> None:
        ...
    @property
    def CharCaseMap(self) -> int:
        """
        optional property which contains the value of the case-mapping of the text for formatting and displaying.
        """
        ...
    @CharCaseMap.setter
    def CharCaseMap(self, value: int) -> None:
        ...
    @property
    def CharColor(self) -> 'Color_68e908c5':
        """
        specifies the text color (RGB) of the control.
        """
        ...
    @CharColor.setter
    def CharColor(self, value: 'Color_68e908c5') -> None:
        ...
    @property
    def CharCombineIsOn(self) -> bool:
        """
        determines whether text is formatted in two lines.
        
        It is linked to the properties CharCombinePrefix and CharCombineSuffix.
        """
        ...
    @CharCombineIsOn.setter
    def CharCombineIsOn(self, value: bool) -> None:
        ...
    @property
    def CharCombinePrefix(self) -> str:
        """
        contains the prefix (usually parenthesis) before text that is formatted in two lines.
        
        It is linked to the properties CharCombineIsOn and CharCombineSuffix.
        """
        ...
    @CharCombinePrefix.setter
    def CharCombinePrefix(self, value: str) -> None:
        ...
    @property
    def CharCombineSuffix(self) -> str:
        """
        contains the suffix (usually parenthesis) after text that is formatted in two lines.
        
        It is linked to the properties CharCombineIsOn and CharCombinePrefix.
        """
        ...
    @CharCombineSuffix.setter
    def CharCombineSuffix(self, value: str) -> None:
        ...
    @property
    def CharContoured(self) -> bool:
        """
        specifies if the characters are formatted and displayed with a contour effect.
        """
        ...
    @CharContoured.setter
    def CharContoured(self, value: bool) -> None:
        ...
    @property
    def CharEmphasis(self) -> int:
        """
        contains the font emphasis value as com.sun.star.text.FontEmphasis.
        """
        ...
    @CharEmphasis.setter
    def CharEmphasis(self, value: int) -> None:
        ...
    @property
    def CharEscapement(self) -> int:
        """
        specifies the percentage by which to raise/lower superscript/subscript characters.
        
        Negative values denote subscripts and positive values superscripts.
        """
        ...
    @CharEscapement.setter
    def CharEscapement(self, value: int) -> None:
        ...
    @property
    def CharEscapementHeight(self) -> int:
        """
        This is the additional height used for subscript or superscript characters in units of percent.
        
        For subscript characters the value is negative and for superscript characters positive.
        """
        ...
    @CharEscapementHeight.setter
    def CharEscapementHeight(self, value: int) -> None:
        ...
    @property
    def CharFlash(self) -> bool:
        """
        If this optional property is TRUE, then the characters are flashing.
        """
        ...
    @CharFlash.setter
    def CharFlash(self, value: bool) -> None:
        ...
    @property
    def CharFontCharSet(self) -> int:
        """
        This attribute contains the text encoding of the font as specified in com.sun.star.awt.CharSet.
        """
        ...
    @CharFontCharSet.setter
    def CharFontCharSet(self, value: int) -> None:
        ...
    @property
    def CharFontCharSetAsian(self) -> int:
        """
        This property contains the text encoding of the font as specified in com.sun.star.awt.CharSet.
        """
        ...
    @CharFontCharSetAsian.setter
    def CharFontCharSetAsian(self, value: int) -> None:
        ...
    @property
    def CharFontCharSetComplex(self) -> int:
        """
        This property contains the text encoding of the font as specified in com.sun.star.awt.CharSet.
        """
        ...
    @CharFontCharSetComplex.setter
    def CharFontCharSetComplex(self, value: int) -> None:
        ...
    @property
    def CharFontFamily(self) -> int:
        """
        This attribute contains font family as specified in com.sun.star.awt.FontFamily .
        """
        ...
    @CharFontFamily.setter
    def CharFontFamily(self, value: int) -> None:
        ...
    @property
    def CharFontFamilyAsian(self) -> int:
        """
        This property contains font family as specified in com.sun.star.awt.FontFamily .
        """
        ...
    @CharFontFamilyAsian.setter
    def CharFontFamilyAsian(self, value: int) -> None:
        ...
    @property
    def CharFontFamilyComplex(self) -> int:
        """
        This property contains font family as specified in com.sun.star.awt.FontFamily .
        """
        ...
    @CharFontFamilyComplex.setter
    def CharFontFamilyComplex(self, value: int) -> None:
        ...
    @property
    def CharFontName(self) -> str:
        """
        This attribute specifies the name of the font style.
        
        It may contain more than one name separated by comma.
        """
        ...
    @CharFontName.setter
    def CharFontName(self, value: str) -> None:
        ...
    @property
    def CharFontNameAsian(self) -> str:
        """
        This property specifies the name of the font style.
        
        It may contain more than one name separated by comma.
        """
        ...
    @CharFontNameAsian.setter
    def CharFontNameAsian(self, value: str) -> None:
        ...
    @property
    def CharFontNameComplex(self) -> str:
        """
        This property specifies the name of the font style.
        
        It may contain more than one name separated by comma.
        """
        ...
    @CharFontNameComplex.setter
    def CharFontNameComplex(self, value: str) -> None:
        ...
    @property
    def CharFontPitch(self) -> int:
        """
        This attribute contains the font pitch as specified in com.sun.star.awt.FontPitch.
        """
        ...
    @CharFontPitch.setter
    def CharFontPitch(self, value: int) -> None:
        ...
    @property
    def CharFontPitchAsian(self) -> int:
        """
        This property contains the font pitch as specified in com.sun.star.awt.FontPitch.
        """
        ...
    @CharFontPitchAsian.setter
    def CharFontPitchAsian(self, value: int) -> None:
        ...
    @property
    def CharFontPitchComplex(self) -> int:
        """
        This property contains the font pitch as specified in com.sun.star.awt.FontPitch.
        """
        ...
    @CharFontPitchComplex.setter
    def CharFontPitchComplex(self, value: int) -> None:
        ...
    @property
    def CharFontStyleName(self) -> str:
        """
        This attribute contains the name of the font style.
        
        This attribute may be empty.
        """
        ...
    @CharFontStyleName.setter
    def CharFontStyleName(self, value: str) -> None:
        ...
    @property
    def CharFontStyleNameAsian(self) -> str:
        """
        This property contains the name of the font style.
        
        This property may be empty.
        """
        ...
    @CharFontStyleNameAsian.setter
    def CharFontStyleNameAsian(self, value: str) -> None:
        ...
    @property
    def CharFontStyleNameComplex(self) -> str:
        """
        This property contains the name of the font style.
        
        This property may be empty.
        """
        ...
    @CharFontStyleNameComplex.setter
    def CharFontStyleNameComplex(self, value: str) -> None:
        ...
    @property
    def CharHeight(self) -> float:
        """
        This value contains the height of the characters in point.
        """
        ...
    @CharHeight.setter
    def CharHeight(self, value: float) -> None:
        ...
    @property
    def CharHeightAsian(self) -> float:
        """
        This value contains the height of the characters in point.
        """
        ...
    @CharHeightAsian.setter
    def CharHeightAsian(self, value: float) -> None:
        ...
    @property
    def CharHeightComplex(self) -> float:
        """
        This value contains the height of the characters in point.
        """
        ...
    @CharHeightComplex.setter
    def CharHeightComplex(self, value: float) -> None:
        ...
    @property
    def CharHidden(self) -> bool:
        """
        If this optional property is TRUE, then the characters are invisible.
        
        **since**
        
            OOo 2.0
        """
        ...
    @CharHidden.setter
    def CharHidden(self, value: bool) -> None:
        ...
    @property
    def CharKerning(self) -> int:
        """
        optional property which contains the value of the kerning of the characters.
        """
        ...
    @CharKerning.setter
    def CharKerning(self, value: int) -> None:
        ...
    @property
    def CharLocale(self) -> 'Locale_70d308fa':
        """
        contains the value of the locale.
        """
        ...
    @CharLocale.setter
    def CharLocale(self, value: 'Locale_70d308fa') -> None:
        ...
    @property
    def CharLocaleAsian(self) -> 'Locale_70d308fa':
        """
        contains the value of the locale.
        """
        ...
    @CharLocaleAsian.setter
    def CharLocaleAsian(self, value: 'Locale_70d308fa') -> None:
        ...
    @property
    def CharLocaleComplex(self) -> 'Locale_70d308fa':
        """
        contains the value of the locale.
        """
        ...
    @CharLocaleComplex.setter
    def CharLocaleComplex(self, value: 'Locale_70d308fa') -> None:
        ...
    @property
    def CharPosture(self) -> 'FontSlant_849509ed':
        """
        This attribute contains the value of the posture of the document.
        """
        ...
    @CharPosture.setter
    def CharPosture(self, value: 'FontSlant_849509ed') -> None:
        ...
    @property
    def CharPostureAsian(self) -> 'FontSlant_849509ed':
        """
        This property contains the value of the posture of the document.
        """
        ...
    @CharPostureAsian.setter
    def CharPostureAsian(self, value: 'FontSlant_849509ed') -> None:
        ...
    @property
    def CharPostureComplex(self) -> 'FontSlant_849509ed':
        """
        This property contains the value of the posture of the document.
        """
        ...
    @CharPostureComplex.setter
    def CharPostureComplex(self, value: 'FontSlant_849509ed') -> None:
        ...
    @property
    def CharRelief(self) -> int:
        """
        specifies the com.sun.star.text.FontRelief value of the text in the control.
        """
        ...
    @CharRelief.setter
    def CharRelief(self, value: int) -> None:
        ...
    @property
    def CharRotation(self) -> int:
        """
        determines the rotation of a character in degree.
        
        Depending on the implementation only certain values may be allowed.
        """
        ...
    @CharRotation.setter
    def CharRotation(self, value: int) -> None:
        ...
    @property
    def CharScaleWidth(self) -> int:
        """
        determines the percentage value for scaling the width of characters.
        
        The value refers to the original width which is denoted by 100, and it has to be greater than 0.
        """
        ...
    @CharScaleWidth.setter
    def CharScaleWidth(self, value: int) -> None:
        ...
    @property
    def CharShadowed(self) -> bool:
        """
        specifies if the characters are formatted and displayed with a shadow effect.
        """
        ...
    @CharShadowed.setter
    def CharShadowed(self, value: bool) -> None:
        ...
    @property
    def CharStrikeout(self) -> int:
        """
        determines the type of the strike out of the character.
        """
        ...
    @CharStrikeout.setter
    def CharStrikeout(self, value: int) -> None:
        ...
    @property
    def CharUnderline(self) -> int:
        """
        This attribute contains the value for the character underline.
        """
        ...
    @CharUnderline.setter
    def CharUnderline(self, value: int) -> None:
        ...
    @property
    def CharUnderlineColor(self) -> 'Color_68e908c5':
        """
        specifies the text line color (RGB) of the control.
        """
        ...
    @CharUnderlineColor.setter
    def CharUnderlineColor(self, value: 'Color_68e908c5') -> None:
        ...
    @property
    def CharWeight(self) -> float:
        """
        This attribute contains the value of the font weight.
        """
        ...
    @CharWeight.setter
    def CharWeight(self, value: float) -> None:
        ...
    @property
    def CharWeightAsian(self) -> float:
        """
        This property contains the value of the font weight.
        """
        ...
    @CharWeightAsian.setter
    def CharWeightAsian(self, value: float) -> None:
        ...
    @property
    def CharWeightComplex(self) -> float:
        """
        This property contains the value of the font weight.
        """
        ...
    @CharWeightComplex.setter
    def CharWeightComplex(self, value: float) -> None:
        ...
    @property
    def CharWordMode(self) -> bool:
        """
        If this attribute is TRUE, the underline and strike-through properties are not applied to white spaces.
        """
        ...
    @CharWordMode.setter
    def CharWordMode(self, value: bool) -> None:
        ...
    @property
    def ControlBackground(self) -> 'Color_68e908c5':
        """
        specifies the background color (RGB) of the control.
        """
        ...
    @ControlBackground.setter
    def ControlBackground(self, value: 'Color_68e908c5') -> None:
        ...
    @property
    def ControlBackgroundTransparent(self) -> bool:
        """
        determines if the background color is set to transparent.
        """
        ...
    @ControlBackgroundTransparent.setter
    def ControlBackgroundTransparent(self, value: bool) -> None:
        ...
    @property
    def ControlTextEmphasis(self) -> int:
        """
        specifies the com.sun.star.text.FontEmphasis value of the text in the control.
        """
        ...
    @ControlTextEmphasis.setter
    def ControlTextEmphasis(self, value: int) -> None:
        ...
    @property
    def FontDescriptor(self) -> 'FontDescriptor_bc110c0a':
        """
        specifies the font attributes of the text in the control.
        """
        ...
    @FontDescriptor.setter
    def FontDescriptor(self, value: 'FontDescriptor_bc110c0a') -> None:
        ...
    @property
    def FontDescriptorAsian(self) -> 'FontDescriptor_bc110c0a':
        """
        specifies the font attributes of the text in the control.
        """
        ...
    @FontDescriptorAsian.setter
    def FontDescriptorAsian(self, value: 'FontDescriptor_bc110c0a') -> None:
        ...
    @property
    def FontDescriptorComplex(self) -> 'FontDescriptor_bc110c0a':
        """
        specifies the font attributes of the text in the control.
        """
        ...
    @FontDescriptorComplex.setter
    def FontDescriptorComplex(self, value: 'FontDescriptor_bc110c0a') -> None:
        ...
    @property
    def HyperLinkName(self) -> str:
        """
        contains the name of the hyperlink (if set).
        """
        ...
    @HyperLinkName.setter
    def HyperLinkName(self, value: str) -> None:
        ...
    @property
    def HyperLinkTarget(self) -> str:
        """
        contains the name of the target for a hyperlink (if set).
        """
        ...
    @HyperLinkTarget.setter
    def HyperLinkTarget(self, value: str) -> None:
        ...
    @property
    def HyperLinkURL(self) -> str:
        """
        contains the URL of a hyperlink (if set).
        """
        ...
    @HyperLinkURL.setter
    def HyperLinkURL(self, value: str) -> None:
        ...
    @property
    def ParaAdjust(self) -> int:
        """
        specifies the horizontal alignment of the text.
        """
        ...
    @ParaAdjust.setter
    def ParaAdjust(self, value: int) -> None:
        ...
    @property
    def UnvisitedCharStyleName(self) -> str:
        """
        contains the character style name for unvisited hyperlinks.
        """
        ...
    @UnvisitedCharStyleName.setter
    def UnvisitedCharStyleName(self, value: str) -> None:
        ...
    @property
    def VerticalAlign(self) -> 'VerticalAlignment_8d0e12':
        """
        specifies the vertical alignment of the text in the control.
        """
        ...
    @VerticalAlign.setter
    def VerticalAlign(self, value: 'VerticalAlignment_8d0e12') -> None:
        ...
    @property
    def VisitedCharStyleName(self) -> str:
        """
        contains the character style name for visited hyperlinks.
        """
        ...
    @VisitedCharStyleName.setter
    def VisitedCharStyleName(self, value: str) -> None:
        ...

