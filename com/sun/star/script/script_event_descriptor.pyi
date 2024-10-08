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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.script
# Libre Office Version: 2024.2
import typing


class ScriptEventDescriptor(object):
    """
    Struct Class

    describes an effect, especially a script to be executed, for a certain event given by the listener type and the name of the event method.

    See Also:
        `API ScriptEventDescriptor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1ScriptEventDescriptor.html>`_
    """
    typeName: str = 'com.sun.star.script.ScriptEventDescriptor'

    def __init__(self, ListenerType: typing.Optional[str] = ..., EventMethod: typing.Optional[str] = ..., AddListenerParam: typing.Optional[str] = ..., ScriptType: typing.Optional[str] = ..., ScriptCode: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            ListenerType (str, optional): ListenerType value.
            EventMethod (str, optional): EventMethod value.
            AddListenerParam (str, optional): AddListenerParam value.
            ScriptType (str, optional): ScriptType value.
            ScriptCode (str, optional): ScriptCode value.
        """
        ...

    @property
    def ListenerType(self) -> str:
        """
        listener type as string, same as listener-XIdlClass.getName().
        """
        ...
    @ListenerType.setter
    def ListenerType(self, value: str) -> None:
        ...
    @property
    def EventMethod(self) -> str:
        """
        event method as string.
        """
        ...
    @EventMethod.setter
    def EventMethod(self, value: str) -> None:
        ...
    @property
    def AddListenerParam(self) -> str:
        """
        data to be used if the addListener method needs an additional parameter.
        
        If the type of this parameter is different from string, it will be converted, when added.
        """
        ...
    @AddListenerParam.setter
    def AddListenerParam(self, value: str) -> None:
        ...
    @property
    def ScriptType(self) -> str:
        """
        type of the script language as string; for example, \"Basic\" or \"StarScript\".
        """
        ...
    @ScriptType.setter
    def ScriptType(self, value: str) -> None:
        ...
    @property
    def ScriptCode(self) -> str:
        """
        script code as string (the code has to correspond with the language defined by ScriptType).
        """
        ...
    @ScriptCode.setter
    def ScriptCode(self, value: str) -> None:
        ...

