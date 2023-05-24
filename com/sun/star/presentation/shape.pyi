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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.presentation
from __future__ import annotations
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ..util.color import Color as Color_68e908c5
    from com.sun.star.presentation.AnimationEffect import AnimationEffectProto
    from com.sun.star.presentation.ClickAction import ClickActionProto
    from com.sun.star.presentation.AnimationSpeed import AnimationSpeedProto

class Shape(ABC):
    """
    Service Class

    this service is supported from all shapes inside a PresentationDocument.
    
    This usually enhances objects of type com.sun.star.drawing.Shape with presentation properties.

    See Also:
        `API Shape <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1presentation_1_1Shape.html>`_
    """
    @property
    def Bookmark(self) -> str:
        """
        is a generic URL for the property OnClick.
        """
        ...
    @Bookmark.setter
    def Bookmark(self, value: str) -> None:
        ...
    @property
    def DimColor(self) -> Color_68e908c5:
        """
        This is the color for dimming this shape.
        
        This color is used if the property com.sun.star.drawing.Shape.DimPrev is TRUE and com.sun.star.drawing.Shape.DimHide is FALSE.
        """
        ...
    @DimColor.setter
    def DimColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def DimHide(self) -> bool:
        """
        If this property and the property com.sun.star.drawing.Shape.DimPrev are both TRUE, the shape is hidden instead of dimmed to a color.
        """
        ...
    @DimHide.setter
    def DimHide(self, value: bool) -> None:
        ...
    @property
    def DimPrevious(self) -> bool:
        """
        If this property is TRUE, this shape is dimmed to the color of property com.sun.star.drawing.Shape.DimColor after executing its animation effect.
        """
        ...
    @DimPrevious.setter
    def DimPrevious(self, value: bool) -> None:
        ...
    @property
    def Effect(self) -> AnimationEffectProto:
        """
        selects the animation effect of this shape.
        """
        ...
    @Effect.setter
    def Effect(self, value: AnimationEffectProto) -> None:
        ...
    @property
    def IsEmptyPresentationObject(self) -> bool:
        """
        If this is a default presentation object and if it is empty, this property is TRUE.
        """
        ...
    @IsEmptyPresentationObject.setter
    def IsEmptyPresentationObject(self, value: bool) -> None:
        ...
    @property
    def IsPresentationObject(self) -> bool:
        """
        If this is a presentation object, this property is TRUE.
        
        Presentation objects are objects like TitleTextShape and OutlinerShape.
        """
        ...
    @IsPresentationObject.setter
    def IsPresentationObject(self, value: bool) -> None:
        ...
    @property
    def OnClick(self) -> ClickActionProto:
        """
        selects an action performed after the user clicks on this shape.
        """
        ...
    @OnClick.setter
    def OnClick(self, value: ClickActionProto) -> None:
        ...
    @property
    def PlayFull(self) -> bool:
        """
        If this property is TRUE, the sound of this shape is played in full.
        
        The default behavior is to stop the sound after completing the animation effect.
        """
        ...
    @PlayFull.setter
    def PlayFull(self, value: bool) -> None:
        ...
    @property
    def PresentationOrder(self) -> int:
        """
        This is the position of this shape in the order of the shapes which can be animated on its page.
        
        The animations are executed in this order, starting at the shape with the PresentationOrder \"one.\" You can change the order by changing this number. Setting it to \"one\" makes this shape the first shape in the execution order for the animation effects.
        """
        ...
    @PresentationOrder.setter
    def PresentationOrder(self, value: int) -> None:
        ...
    @property
    def Sound(self) -> str:
        """
        This is the URL to a sound file that is played while the animation effect of this shape is running.
        """
        ...
    @Sound.setter
    def Sound(self, value: str) -> None:
        ...
    @property
    def SoundOn(self) -> bool:
        """
        If this property is set to TRUE, a sound is played while the animation effect is executed.
        """
        ...
    @SoundOn.setter
    def SoundOn(self, value: bool) -> None:
        ...
    @property
    def Speed(self) -> AnimationSpeedProto:
        """
        This is the speed of the animation effect.
        """
        ...
    @Speed.setter
    def Speed(self, value: AnimationSpeedProto) -> None:
        ...
    @property
    def TextEffect(self) -> AnimationEffectProto:
        """
        This is the animation effect for the text inside this shape.
        """
        ...
    @TextEffect.setter
    def TextEffect(self, value: AnimationEffectProto) -> None:
        ...
    @property
    def Verb(self) -> int:
        """
        specifies an \"OLE2\" verb for the ClickAction VERB in the property com.sun.star.drawing.Shape.OnClick.
        """
        ...
    @Verb.setter
    def Verb(self, value: int) -> None:
        ...

