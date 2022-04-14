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
# Namespace: com.sun.star.script
# Libre Office Version: 7.2
from typing_extensions import Literal
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class AllEventObject(EventObject_a3d70b03):
    """
    Struct Class

    This event is a wrapper for an original event in a forwarding event.
    
    Usually the original event is the first argument in the array of arguments.

    See Also:
        `API AllEventObject <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1AllEventObject.html>`_
    """
    typeName: Literal['com.sun.star.script.AllEventObject']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., Arguments: typing.Optional[typing.Tuple[object, ...]] = ..., Helper: typing.Optional[object] = ..., ListenerType: typing.Optional[object] = ..., MethodName: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Arguments (typing.Tuple[object, ...], optional): Arguments value.
            Helper (object, optional): Helper value.
            ListenerType (object, optional): ListenerType value.
            MethodName (str, optional): MethodName value.
        """


    @property
    def Arguments(self) -> typing.Tuple[object, ...]:
        """
        The arguments of the original method.
        """


    @property
    def Helper(self) -> object:
        """
        A helper value for the implementation that can be used arbitrarily.
        
        This field reflects the third parameter of the method XAllListenerAdapterService.createAllListerAdapter().
        """


    @property
    def ListenerType(self) -> object:
        """
        contains the type of the original listener.
        """


    @property
    def MethodName(self) -> str:
        """
        The original method name on which the event was fired.
        """



__all__ = ['AllEventObject']
