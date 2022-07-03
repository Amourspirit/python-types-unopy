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
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from .x_all_listener import XAllListener as XAllListener_c91b0c54


class EventListener(object):
    """
    Struct Class


    See Also:
        `API EventListener <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1EventListener.html>`_
    """
    typeName: Literal['com.sun.star.script.EventListener']

    def __init__(self, AllListener: typing.Optional[XAllListener_c91b0c54] = ..., Helper: typing.Optional[object] = ..., ListenerType: typing.Optional[str] = ..., AddListenerParam: typing.Optional[str] = ..., EventMethod: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            AllListener (XAllListener, optional): AllListener value.
            Helper (object, optional): Helper value.
            ListenerType (str, optional): ListenerType value.
            AddListenerParam (str, optional): AddListenerParam value.
            EventMethod (str, optional): EventMethod value.
        """
        ...


    @property
    def AllListener(self) -> XAllListener_c91b0c54:
        ...


    @property
    def Helper(self) -> object:
        ...


    @property
    def ListenerType(self) -> str:
        ...


    @property
    def AddListenerParam(self) -> str:
        ...


    @property
    def EventMethod(self) -> str:
        ...


