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
# Namespace: com.sun.star.animations
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class Event(object):
    """
    Struct Class

    an event has a source that causes an event to be fired and a trigger that defines under which condition an event should be raised and an offset if the event should be raised a defined amount of time after the event is triggered.

    See Also:
        `API Event <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1animations_1_1Event.html>`_
    """
    typeName: Literal['com.sun.star.animations.Event']

    def __init__(self, Source: typing.Optional[object] = ..., Trigger: typing.Optional[int] = ..., Offset: typing.Optional[object] = ..., Repeat: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (object, optional): Source value.
            Trigger (int, optional): Trigger value.
            Offset (object, optional): Offset value.
            Repeat (int, optional): Repeat value.
        """


    @property
    def Source(self) -> object:
        """
        this is the source for this event.
        """


    @property
    def Trigger(self) -> int:
        """
        this is the trigger that fires this event.
        """


    @property
    def Offset(self) -> object:
        """
        an optional offset in seconds or Timing.INDEFINITE.
        
        This is the timespan between the triggering of the event and actually raising the event
        """


    @property
    def Repeat(self) -> int:
        """
        an option repeat value.
        
        If the Trigger is EventTrigger, this is the number of repeats after which the event is initially raised.
        """



__all__ = ['Event']
