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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.script.provider
from typing_extensions import Literal
import typing
import uno
from ...uno.x_interface import XInterface as XInterface_8f010a43

class XScript(XInterface_8f010a43):
    """
    This interface represents an invocable script or UNO function.

    See Also:
        `API XScript <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1provider_1_1XScript.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.script.provider.XScript']

    def invoke(self, aParams: 'typing.Tuple[object, ...]', aOutParamIndex: uno.ByteSequence, aOutParam: 'typing.Tuple[object, ...]') -> object:
        """
        invoke the script or function represented by the implementing object
        
        For example, if the script had the signaturelong foo( [inout] string a, [in] string b, [out] string c ) the call would look likebar.invoke( {\"foo\", \"foo2\", \"this-is-ignored\" }, aOutParamIndex, aOutParam); and after the call the out sequences would contain

        * ``aOutParamIndex`` is an out direction argument.
        * ``aOutParam`` is an out direction argument.

        Raises:
            : ````
            com.sun.star.reflection.InvocationTargetException: ``InvocationTargetException``
        """
        ...


