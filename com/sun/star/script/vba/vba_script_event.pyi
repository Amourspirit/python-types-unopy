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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.script.vba
# Libre Office Version: 7.4
from ...lang.event_object import EventObject as EventObject_a3d70b03
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing


class VBAScriptEvent(EventObject_a3d70b03):
    """
    Struct Class

    Describes a VBA script event fired via XVBACompatibility.broadcastVBAScriptEvent(), and received by XVBAScriptListener.notifyVBAScriptEvent().

    See Also:
        `API VBAScriptEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1vba_1_1VBAScriptEvent.html>`_
    """
    typeName: str = 'com.sun.star.script.vba.VBAScriptEvent'

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., Identifier: typing.Optional[int] = ..., ModuleName: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Identifier (int, optional): Identifier value.
            ModuleName (str, optional): ModuleName value.
        """
        ...

    @property
    def Identifier(self) -> int:
        """
        Identifies the type of the event.
        """
        ...
    @Identifier.setter
    def Identifier(self, value: int) -> None:
        ...
    @property
    def ModuleName(self) -> str:
        """
        Contains the name of the involved VBA module.
        """
        ...
    @ModuleName.setter
    def ModuleName(self, value: str) -> None:
        ...
