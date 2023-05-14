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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.4
from typing_extensions import Literal
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class ActionEvent(EventObject_a3d70b03):
    """
    Struct Class

    a semantic event which indicates that a component-defined action occurred.
    
    This high-level event is generated by a component (such as a Button) when the component-specific action occurs (such as being pressed). The event is passed to every XActionListener object that registered to receive such events using the component's addActionListener method.
    
    The object that implements the XActionListener interface gets this ActionEvent when the event occurs. The listener is therefore spared the details of processing individual mouse movements and mouse clicks, and can instead process a \"meaningful\" (semantic) event like \"button pressed\".

    See Also:
        `API ActionEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1ActionEvent.html>`_
    """
    typeName: Literal['com.sun.star.awt.ActionEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., ActionCommand: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            ActionCommand (str, optional): ActionCommand value.
        """
        ...


    @property
    def ActionCommand(self) -> str:
        """
        contains the command string associated with this action.
        """
        ...

    @ActionCommand.setter
    def ActionCommand(self, value: str) -> None:
        ...

