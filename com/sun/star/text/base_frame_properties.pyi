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
# Namespace: com.sun.star.text
from __future__ import annotations
import typing
from ..xml.user_defined_attributes_supplier import UserDefinedAttributesSupplier as UserDefinedAttributesSupplier_9fbe1222
if typing.TYPE_CHECKING:
    from ..awt.gradient import Gradient as Gradient_7a8a0982
    from ..awt.size import Size as Size_576707ef
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from ..table.border_line import BorderLine as BorderLine_a3f80af6
    from ..table.shadow_format import ShadowFormat as ShadowFormat_bb840bdf
    from .x_text_frame import XTextFrame as XTextFrame_9a7e0ab5
    from ..util.color import Color as Color_68e908c5
    from com.sun.star.style.GraphicLocation import GraphicLocationProto  # type: ignore
    from com.sun.star.drawing.FillStyle import FillStyleProto  # type: ignore
    from com.sun.star.text.WrapTextMode import WrapTextModeProto  # type: ignore

class BaseFrameProperties(UserDefinedAttributesSupplier_9fbe1222):
    """
    Service Class

    specifies the properties that are provided by all text frames, graphic objects, embedded objects and frame styles.
    
    **since**
    
        OOo 2.1

    See Also:
        `API BaseFrameProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1BaseFrameProperties.html>`_
    """
    @property
    def AllowOverlap(self) -> bool:
        """
        This defines if the frame is allowed to overlap with other anchored objects.
        
        **since**
        
            LibreOffice 6.4
        """
        ...
    @AllowOverlap.setter
    def AllowOverlap(self, value: bool) -> None:
        ...
    @property
    def AnchorFrame(self) -> XTextFrame_9a7e0ab5:
        """
        contains the text frame the current frame is anchored to.
        
        The value is valid only if the AnchorType is TextContentAnchorType.AT_FRAME.
        """
        ...
    @AnchorFrame.setter
    def AnchorFrame(self, value: XTextFrame_9a7e0ab5) -> None:
        ...
    @property
    def AnchorPageNo(self) -> int:
        """
        contains the number of the page where the objects are anchored.
        
        The value is valid only if the AnchorType is TextContentAnchorType.AT_PAGE.
        """
        ...
    @AnchorPageNo.setter
    def AnchorPageNo(self, value: int) -> None:
        ...
    @property
    def BackColor(self) -> Color_68e908c5:
        """
        contains the color of the background of the object.
        """
        ...
    @BackColor.setter
    def BackColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def BackGraphic(self) -> XGraphic_a4da0afc:
        """
        contains the graphic for the background.
        
        **since**
        
            LibreOffice 6.1
        """
        ...
    @BackGraphic.setter
    def BackGraphic(self, value: XGraphic_a4da0afc) -> None:
        ...
    @property
    def BackGraphicFilter(self) -> str:
        """
        contains the name of the file filter for the background graphic.
        """
        ...
    @BackGraphicFilter.setter
    def BackGraphicFilter(self, value: str) -> None:
        ...
    @property
    def BackGraphicLocation(self) -> GraphicLocationProto:
        """
        determines the position of the background graphic.
        """
        ...
    @BackGraphicLocation.setter
    def BackGraphicLocation(self, value: GraphicLocationProto) -> None:
        ...
    @property
    def BackGraphicURL(self) -> str:
        """
        contains the URL for the background graphic.
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When an URL is set, then it will load the graphic and set the BackGraphic property.
        """
        ...
    @BackGraphicURL.setter
    def BackGraphicURL(self, value: str) -> None:
        ...
    @property
    def BackTransparent(self) -> bool:
        """
        If TRUE, the \"BackColor\" is ignored.
        """
        ...
    @BackTransparent.setter
    def BackTransparent(self, value: bool) -> None:
        ...
    @property
    def BorderDistance(self) -> int:
        """
        contains the distance from the border to the object.
        """
        ...
    @BorderDistance.setter
    def BorderDistance(self, value: int) -> None:
        ...
    @property
    def BottomBorder(self) -> BorderLine_a3f80af6:
        """
        contains the bottom border of the object.
        """
        ...
    @BottomBorder.setter
    def BottomBorder(self, value: BorderLine_a3f80af6) -> None:
        ...
    @property
    def BottomBorderDistance(self) -> int:
        """
        contains the distance from the bottom border to the object.
        """
        ...
    @BottomBorderDistance.setter
    def BottomBorderDistance(self, value: int) -> None:
        ...
    @property
    def BottomMargin(self) -> int:
        """
        contains the bottom margin of the object.
        """
        ...
    @BottomMargin.setter
    def BottomMargin(self, value: int) -> None:
        ...
    @property
    def ContentProtected(self) -> bool:
        """
        determines if the content is protected.
        """
        ...
    @ContentProtected.setter
    def ContentProtected(self, value: bool) -> None:
        ...
    @property
    def Decorative(self) -> bool:
        """
        Determines if the frame is purely decorative.
        
        If TRUE, it is considered not part of the document content, and may be ignored by assistive technologies.
        
        **since**
        
            LibreOffice 7.5
        """
        ...
    @Decorative.setter
    def Decorative(self, value: bool) -> None:
        ...
    @property
    def Description(self) -> str:
        """
        contains description for the object
        
        The long description text can be entered to describe an object in more detail to users with screen reader software. The description is visible as an alternative tag for accessibility tools.
        
        **since**
        
            OOo 3.2
        """
        ...
    @Description.setter
    def Description(self, value: str) -> None:
        ...
    @property
    def FillGradient(self) -> Gradient_7a8a0982:
        """
        If the property FillStyle is set to FillStyle.GRADIENT, this describes the gradient used.
        
        **since**
        
            LibreOffice 4.1
        """
        ...
    @FillGradient.setter
    def FillGradient(self, value: Gradient_7a8a0982) -> None:
        ...
    @property
    def FillGradientName(self) -> str:
        """
        If the property FillStyle is set to FillStyle.GRADIENT, this is the name of the gradient used.
        
        **since**
        
            LibreOffice 4.1
        """
        ...
    @FillGradientName.setter
    def FillGradientName(self, value: str) -> None:
        ...
    @property
    def FillStyle(self) -> FillStyleProto:
        """
        This enumeration selects the style the area will be filled with.
        
        Currently only set for gradients.
        
        **since**
        
            LibreOffice 4.1
        """
        ...
    @FillStyle.setter
    def FillStyle(self, value: FillStyleProto) -> None:
        ...
    @property
    def FrameInteropGrabBag(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        """
        Grab bag of frame properties, used as a string-any map for interim interop purposes.
        
        This property is intentionally not handled by the ODF filter. Any member that should be handled there should be first moved out from this grab bag to a separate property.
        
        **since**
        
            LibreOffice 4.2
        """
        ...
    @FrameInteropGrabBag.setter
    def FrameInteropGrabBag(self, value: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        ...
    @property
    def Height(self) -> int:
        """
        contains the height of the object (1/100 mm).
        
        It is only valid if TextEmbeddedObject.RelativeHeight is zero.
        """
        ...
    @Height.setter
    def Height(self, value: int) -> None:
        ...
    @property
    def HoriOrient(self) -> int:
        """
        determines the horizontal orientation of the object.
        """
        ...
    @HoriOrient.setter
    def HoriOrient(self, value: int) -> None:
        ...
    @property
    def HoriOrientPosition(self) -> int:
        """
        contains the horizontal position of the object (1/100 mm).
        
        It is only valid if \"HoriOrient\" is HoriOrientation_NONE.
        """
        ...
    @HoriOrientPosition.setter
    def HoriOrientPosition(self, value: int) -> None:
        ...
    @property
    def HoriOrientRelation(self) -> int:
        """
        determines the environment of the object to which the orientation is related.
        """
        ...
    @HoriOrientRelation.setter
    def HoriOrientRelation(self, value: int) -> None:
        ...
    @property
    def HyperLinkName(self) -> str:
        """
        contains the name of the hyperlink that is set at the object.
        """
        ...
    @HyperLinkName.setter
    def HyperLinkName(self, value: str) -> None:
        ...
    @property
    def HyperLinkTarget(self) -> str:
        """
        contains the name of the target for a hyperlink that is set at the object.
        """
        ...
    @HyperLinkTarget.setter
    def HyperLinkTarget(self, value: str) -> None:
        ...
    @property
    def HyperLinkURL(self) -> str:
        """
        contains the URL of a hyperlink that is set at the object.
        """
        ...
    @HyperLinkURL.setter
    def HyperLinkURL(self, value: str) -> None:
        ...
    @property
    def IsSplitAllowed(self) -> bool:
        """
        If TRUE, the frame is allowed to be split at page breaks.
        
        **since**
        
            LibreOffice 7.6
        """
        ...
    @IsSplitAllowed.setter
    def IsSplitAllowed(self, value: bool) -> None:
        ...
    @property
    def IsSyncHeightToWidth(self) -> bool:
        """
        determines whether the height follows the width.
        """
        ...
    @IsSyncHeightToWidth.setter
    def IsSyncHeightToWidth(self, value: bool) -> None:
        ...
    @property
    def IsSyncWidthToHeight(self) -> bool:
        """
        determines whether the width follows the height.
        """
        ...
    @IsSyncWidthToHeight.setter
    def IsSyncWidthToHeight(self, value: bool) -> None:
        ...
    @property
    def LayoutSize(self) -> Size_576707ef:
        """
        returns the actual size of the object.
        
        Since to obtain the correct actual size of the object not only the layouting for the frame needs to be finished but the whole document needs to be formatted as well. Thus if that was not done previously it may take some while to retrieve this value.
        
        **since**
        
            OOo 2.0.4
        """
        ...
    @LayoutSize.setter
    def LayoutSize(self, value: Size_576707ef) -> None:
        ...
    @property
    def LeftBorder(self) -> BorderLine_a3f80af6:
        """
        contains the left border of the object.
        """
        ...
    @LeftBorder.setter
    def LeftBorder(self, value: BorderLine_a3f80af6) -> None:
        ...
    @property
    def LeftBorderDistance(self) -> int:
        """
        contains the distance from the left border to the object.
        """
        ...
    @LeftBorderDistance.setter
    def LeftBorderDistance(self, value: int) -> None:
        ...
    @property
    def LeftMargin(self) -> int:
        """
        contains the left margin of the object.
        """
        ...
    @LeftMargin.setter
    def LeftMargin(self, value: int) -> None:
        ...
    @property
    def Opaque(self) -> bool:
        """
        determines if the object is opaque or transparent for text.
        """
        ...
    @Opaque.setter
    def Opaque(self, value: bool) -> None:
        ...
    @property
    def PageToggle(self) -> bool:
        """
        determines if the object is mirrored on even pages.
        """
        ...
    @PageToggle.setter
    def PageToggle(self, value: bool) -> None:
        ...
    @property
    def PositionProtected(self) -> bool:
        """
        determines if the position is protected.
        """
        ...
    @PositionProtected.setter
    def PositionProtected(self, value: bool) -> None:
        ...
    @property
    def Print(self) -> bool:
        """
        determines if the object is included in printing.
        """
        ...
    @Print.setter
    def Print(self, value: bool) -> None:
        ...
    @property
    def RelativeHeight(self) -> int:
        """
        contains the relative height of the object.
        
        It is only valid if it is greater than zero.
        """
        ...
    @RelativeHeight.setter
    def RelativeHeight(self, value: int) -> None:
        ...
    @property
    def RelativeHeightRelation(self) -> int:
        """
        contains the relation of the relative height of the object.
        
        It is only valid if RelativeHeight is greater than zero.
        
        **since**
        
            LibreOffice 4.3
        """
        ...
    @RelativeHeightRelation.setter
    def RelativeHeightRelation(self, value: int) -> None:
        ...
    @property
    def RelativeWidth(self) -> int:
        """
        contains the relative width of the object.
        
        It is only valid if it is greater than zero.
        """
        ...
    @RelativeWidth.setter
    def RelativeWidth(self, value: int) -> None:
        ...
    @property
    def RelativeWidthRelation(self) -> int:
        """
        contains the relation of the relative width of the object.
        
        It is only valid if RelativeWidth is greater than zero.
        
        **since**
        
            LibreOffice 4.3
        """
        ...
    @RelativeWidthRelation.setter
    def RelativeWidthRelation(self, value: int) -> None:
        ...
    @property
    def RightBorder(self) -> BorderLine_a3f80af6:
        """
        contains the right border of the object.
        """
        ...
    @RightBorder.setter
    def RightBorder(self, value: BorderLine_a3f80af6) -> None:
        ...
    @property
    def RightBorderDistance(self) -> int:
        """
        contains the distance from the right border to the object.
        """
        ...
    @RightBorderDistance.setter
    def RightBorderDistance(self, value: int) -> None:
        ...
    @property
    def RightMargin(self) -> int:
        """
        contains the right margin of the object.
        """
        ...
    @RightMargin.setter
    def RightMargin(self, value: int) -> None:
        ...
    @property
    def ServerMap(self) -> bool:
        """
        determines if the object gets an image map from a server.
        """
        ...
    @ServerMap.setter
    def ServerMap(self, value: bool) -> None:
        ...
    @property
    def ShadowFormat(self) -> ShadowFormat_bb840bdf:
        """
        contains the type of the shadow of the object.
        """
        ...
    @ShadowFormat.setter
    def ShadowFormat(self, value: ShadowFormat_bb840bdf) -> None:
        ...
    @property
    def ShadowTransparence(self) -> int:
        """
        This defines the degree of transparence of the shadow in percent.
        
        This is the same as setting the Color member of the ShadowFormat property to an ARGB color.
        
        **since**
        
            LibreOffice 4.2
        """
        ...
    @ShadowTransparence.setter
    def ShadowTransparence(self, value: int) -> None:
        ...
    @property
    def Size(self) -> Size_576707ef:
        """
        contains the size of the object.
        """
        ...
    @Size.setter
    def Size(self, value: Size_576707ef) -> None:
        ...
    @property
    def SizeProtected(self) -> bool:
        """
        determines if the size is protected.
        """
        ...
    @SizeProtected.setter
    def SizeProtected(self, value: bool) -> None:
        ...
    @property
    def Surround(self) -> WrapTextModeProto:
        """
        determines the type of the surrounding text.
        """
        ...
    @Surround.setter
    def Surround(self, value: WrapTextModeProto) -> None:
        ...
    @property
    def SurroundAnchorOnly(self) -> bool:
        """
        determines if the text of the paragraph in which the object is anchored, wraps around the object.
        """
        ...
    @SurroundAnchorOnly.setter
    def SurroundAnchorOnly(self, value: bool) -> None:
        ...
    @property
    def Title(self) -> str:
        """
        contains short title for the object
        
        This short title is visible as an alternative tag in HTML format. Accessibility tools can read this text.
        
        **since**
        
            OOo 3.2
        """
        ...
    @Title.setter
    def Title(self, value: str) -> None:
        ...
    @property
    def Tooltip(self) -> str:
        """
        Contains popup text for the frame, used to for tooltip purposes if it's non-empty.
        
        **since**
        
            LibreOffice 7.4
        """
        ...
    @Tooltip.setter
    def Tooltip(self, value: str) -> None:
        ...
    @property
    def TopBorder(self) -> BorderLine_a3f80af6:
        """
        contains the top border of the object.
        """
        ...
    @TopBorder.setter
    def TopBorder(self, value: BorderLine_a3f80af6) -> None:
        ...
    @property
    def TopBorderDistance(self) -> int:
        """
        contains the distance from the top border to the object.
        """
        ...
    @TopBorderDistance.setter
    def TopBorderDistance(self, value: int) -> None:
        ...
    @property
    def TopMargin(self) -> int:
        """
        contains the top margin of the object.
        """
        ...
    @TopMargin.setter
    def TopMargin(self, value: int) -> None:
        ...
    @property
    def VertOrient(self) -> int:
        """
        determines the vertical orientation of the object.
        """
        ...
    @VertOrient.setter
    def VertOrient(self, value: int) -> None:
        ...
    @property
    def VertOrientPosition(self) -> int:
        """
        contains the vertical position of the object (1/100 mm).
        
        It is only valid if TextEmbeddedObject.VertOrient is VertOrientation.NONE.
        """
        ...
    @VertOrientPosition.setter
    def VertOrientPosition(self, value: int) -> None:
        ...
    @property
    def VertOrientRelation(self) -> int:
        """
        determines the environment of the object to which the orientation is related.
        """
        ...
    @VertOrientRelation.setter
    def VertOrientRelation(self, value: int) -> None:
        ...
    @property
    def Width(self) -> int:
        """
        contains the width of the object (1/100 mm).
        
        It is only valid if TextEmbeddedObject.RelativeWidth is zero.
        """
        ...
    @Width.setter
    def Width(self, value: int) -> None:
        ...
    @property
    def WrapInfluenceOnPosition(self) -> int:
        """
        determines the influence of the text wrap on the positioning of the shape
        
        The value of this property is only evaluated for the positioning of the shape, if the text document setting ConsiderTextWrapOnObjPos is TRUE. Valid values are given by WrapInfluenceOnPosition
        
        **since**
        
            OOo 2.0
        """
        ...
    @WrapInfluenceOnPosition.setter
    def WrapInfluenceOnPosition(self, value: int) -> None:
        ...
    @property
    def WrapTextAtFlyStart(self) -> bool:
        """
        If TRUE, text wraps around a split fly on all pages.
        
        **since**
        
            LibreOffice 24.2
        """
        ...
    @WrapTextAtFlyStart.setter
    def WrapTextAtFlyStart(self, value: bool) -> None:
        ...