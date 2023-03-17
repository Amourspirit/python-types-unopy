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
# Libre Office Version: 7.4
from typing_extensions import Literal
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .interrupt_reason import InterruptReason as InterruptReason_f3d00dd2


class InterruptEngineEvent(EventObject_a3d70b03):
    """
    Struct Class

    describes an interrupt which occurs in the scripting engine.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API InterruptEngineEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1InterruptEngineEvent.html>`_
    """
    typeName: Literal['com.sun.star.script.InterruptEngineEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., Name: typing.Optional[str] = ..., SourceCode: typing.Optional[str] = ..., StartLine: typing.Optional[int] = ..., StartColumn: typing.Optional[int] = ..., EndLine: typing.Optional[int] = ..., EndColumn: typing.Optional[int] = ..., ErrorMessage: typing.Optional[str] = ..., Reason: typing.Optional[InterruptReason_f3d00dd2] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Name (str, optional): Name value.
            SourceCode (str, optional): SourceCode value.
            StartLine (int, optional): StartLine value.
            StartColumn (int, optional): StartColumn value.
            EndLine (int, optional): EndLine value.
            EndColumn (int, optional): EndColumn value.
            ErrorMessage (str, optional): ErrorMessage value.
            Reason (InterruptReason, optional): Reason value.
        """
        ...


    @property
    def Name(self) -> str:
        """
        fully qualified name to address the module or function affected by the event that took place.
        
        If the module or function can't be addressed by name (for example, in case that a runtime-generated eval-module is executed), this string is empty.
        """
        ...


    @property
    def SourceCode(self) -> str:
        """
        source code of the Module affected by the event that took place.
        
        If the source can be accessed using the ModuleName, or if the source is unknown (executing compiled code), this string can be empty.
        """
        ...


    @property
    def StartLine(self) -> int:
        """
        contains the first line in the module's source code that is affected by the event that took place.
        
        If \"name\" addresses a function, all line and column values are nevertheless given relative to the module's source. If source code is not available, this value addresses a binary position in the compiled code.
        """
        ...


    @property
    def StartColumn(self) -> int:
        """
        contains the first column in the \"StartLine\" that is affected by the event that took place.
        """
        ...


    @property
    def EndLine(self) -> int:
        """
        contains the last line in the module's source code that is affected by the event that took place.
        """
        ...


    @property
    def EndColumn(self) -> int:
        """
        contains the first column in the \"EndLine\" which is NOT affected by the event that took place.
        """
        ...


    @property
    def ErrorMessage(self) -> str:
        """
        error message.
        
        Only valid if Reason is RuntimeError or CompileError.
        """
        ...


    @property
    def Reason(self) -> InterruptReason_f3d00dd2:
        """
        contains the interrupt reason.
        """
        ...


