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
# Namespace: com.sun.star.awt
from __future__ import annotations
import typing
from .uno_control_model import UnoControlModel as UnoControlModel_c8ce0c58
if typing.TYPE_CHECKING:
    from .font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from ..util.color import Color as Color_68e908c5
    from com.sun.star.style.VerticalAlignment import VerticalAlignmentProto  # type: ignore

class UnoControlRadioButtonModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a UnoControlRadioButton.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UnoControlRadioButtonModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlRadioButtonModel.html>`_
    """
    @property
    def Align(self) -> int:
        """
        specifies the horizontal alignment of the text in the control.
        
        **since**
        
            OOo 2.0
        """
        ...
    @Align.setter
    def Align(self, value: int) -> None:
        ...
    @property
    def BackgroundColor(self) -> int:
        """
        specifies the background color (RGB) of the control.
        """
        ...
    @BackgroundColor.setter
    def BackgroundColor(self, value: int) -> None:
        ...
    @property
    def Enabled(self) -> bool:
        """
        determines whether the control is enabled or disabled.
        """
        ...
    @Enabled.setter
    def Enabled(self, value: bool) -> None:
        ...
    @property
    def FontDescriptor(self) -> FontDescriptor_bc110c0a:
        """
        specifies the font attributes of the text in the control.
        """
        ...
    @FontDescriptor.setter
    def FontDescriptor(self, value: FontDescriptor_bc110c0a) -> None:
        ...
    @property
    def FontEmphasisMark(self) -> int:
        """
        specifies the com.sun.star.text.FontEmphasis value of the text in the control.
        """
        ...
    @FontEmphasisMark.setter
    def FontEmphasisMark(self, value: int) -> None:
        ...
    @property
    def FontRelief(self) -> int:
        """
        specifies the com.sun.star.text.FontRelief value of the text in the control.
        """
        ...
    @FontRelief.setter
    def FontRelief(self, value: int) -> None:
        ...
    @property
    def Graphic(self) -> XGraphic_a4da0afc:
        """
        specifies a graphic to be displayed besides the label of the control
        
        If this property is present, it interacts with the ImageURL in the following way:
        
        **since**
        
            OOo 2.1
        """
        ...
    @Graphic.setter
    def Graphic(self, value: XGraphic_a4da0afc) -> None:
        ...
    @property
    def HelpText(self) -> str:
        """
        specifies the help text of the control.
        """
        ...
    @HelpText.setter
    def HelpText(self, value: str) -> None:
        ...
    @property
    def HelpURL(self) -> str:
        """
        specifies the help URL of the control.
        """
        ...
    @HelpURL.setter
    def HelpURL(self, value: str) -> None:
        ...
    @property
    def ImagePosition(self) -> int:
        """
        specifies the position of the image, if any, relative to the text, if any
        
        Valid values of this property are specified with ImagePosition.
        """
        ...
    @ImagePosition.setter
    def ImagePosition(self, value: int) -> None:
        ...
    @property
    def ImageURL(self) -> str:
        """
        specifies a URL to an image to display besides the label of the control
        """
        ...
    @ImageURL.setter
    def ImageURL(self, value: str) -> None:
        ...
    @property
    def Label(self) -> str:
        """
        specifies the label of the control.
        """
        ...
    @Label.setter
    def Label(self, value: str) -> None:
        ...
    @property
    def MultiLine(self) -> bool:
        """
        specifies that the text may be displayed on more than one line.
        
        **since**
        
            OOo 2.0
        """
        ...
    @MultiLine.setter
    def MultiLine(self, value: bool) -> None:
        ...
    @property
    def Printable(self) -> bool:
        """
        specifies that the control will be printed with the document.
        """
        ...
    @Printable.setter
    def Printable(self, value: bool) -> None:
        ...
    @property
    def State(self) -> int:
        """
        specifies the state of the control.
        """
        ...
    @State.setter
    def State(self, value: int) -> None:
        ...
    @property
    def Tabstop(self) -> bool:
        """
        specifies that the control can be reached with the TAB key.
        """
        ...
    @Tabstop.setter
    def Tabstop(self, value: bool) -> None:
        ...
    @property
    def TextColor(self) -> Color_68e908c5:
        """
        specifies the text color (RGB) of the control.
        """
        ...
    @TextColor.setter
    def TextColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def TextLineColor(self) -> Color_68e908c5:
        """
        specifies the text line color (RGB) of the control.
        """
        ...
    @TextLineColor.setter
    def TextLineColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def VerticalAlign(self) -> VerticalAlignmentProto:
        """
        specifies the vertical alignment of the text in the control.
        
        **since**
        
            OOo 2.0
        """
        ...
    @VerticalAlign.setter
    def VerticalAlign(self, value: VerticalAlignmentProto) -> None:
        ...
    @property
    def VisualEffect(self) -> int:
        """
        specifies a visual effect to apply to the radio button control.
        
        Possible values for this property are VisualEffect.FLAT and VisualEffect.LOOK3D.
        
        **since**
        
            OOo 2.0
        """
        ...
    @VisualEffect.setter
    def VisualEffect(self, value: int) -> None:
        ...
    @property
    def WritingMode(self) -> int:
        """
        denotes the writing mode used in the control, as specified in the com.sun.star.text.WritingMode2 constants group.
        
        Only com.sun.star.text.WritingMode2.LR_TB and com.sun.star.text.WritingMode2.RL_TB are supported at the moment.
        
        **since**
        
            OOo 3.1
        """
        ...
    @WritingMode.setter
    def WritingMode(self, value: int) -> None:
        ...