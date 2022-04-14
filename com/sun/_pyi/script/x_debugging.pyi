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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.script
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .context_information import ContextInformation as ContextInformation_1ece0f08

class XDebugging(XInterface_8f010a43):
    """
    makes it possible to set breakpoints in an interpreter.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XDebugging <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XDebugging.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.script.XDebugging']

    def clearAllBreakPoints(self, aModuleName: str) -> None:
        """
        clears all breakpoints in the module set by \"setBreakPoint\".
        """
    def doContinue(self) -> None:
        """
        continues the program execution.
        """
    def dumpVariable(self, aVariableName: str, nCallStackPos: int) -> str:
        """
        returns the value of the variable at the given stack position.
        """
    def eval(self, aSourceCode: str, nCallStackPos: int) -> str:
        """
        Evaluates an expression.
        """
    def getContextInformation(self, nCallStackPos: int) -> 'ContextInformation_1ece0f08':
        """
        returns more detailed information about a specified stack frame.
        """
    def getStackTrace(self) -> 'typing.Tuple[str, ...]':
        """
        Returns the engine's stack trace of the current execute position.
        
        Line break is the delimiter.
        """
    def isVariable(self, aVariableName: str, nCallStackPos: int) -> bool:
        """
        returns whether the given variable exists within the specified stack frame.
        """
    def setBreakPoint(self, aModuleName: str, nSourceCodeLine: int, bOn: bool) -> int:
        """
        returns the source code line where the breakpoint was set.
        """
    def setVariable(self, aVariableName: str, aValue: str, nCallStackPos: int) -> None:
        """
        sets the value of the specified variable within the specified stack frame.
        """
    def stepIn(self) -> None:
        """
        executes the next and only the next statement.
        
        If the next statement is a function call, only the function entered.
        """
    def stepOut(self) -> None:
        """
        executes the program until the next return from this stack frame.
        """
    def stepOver(self) -> None:
        """
        executes the next and only the next statement.
        
        If the next statement is a function call, the function is executed completely.
        """
    def stop(self) -> None:
        """
        stops the execution of the interpreter.
        
        To continue with the execution, call XDebugging.doContinue().
        """

__all__ = ['XDebugging']

