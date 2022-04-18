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
# Libre Office Version: 7.3
# Namespace: com.sun.star.io
from typing_extensions import Literal
from .x_output_stream import XOutputStream as XOutputStream_a4e00b35

class XTextOutputStream(XOutputStream_a4e00b35):
    """
    Interface to write strings to a stream using a special character encoding.
    
    This interfaces allows to write strings to a stream. The character encoding to be used can be set by setEncoding(). Default encoding is \"utf8\".

    See Also:
        `API XTextOutputStream <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XTextOutputStream.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.io.XTextOutputStream']

    def setEncoding(self, Encoding: str) -> None:
        """
        sets character encoding.
        """
    def writeString(self, aString: str) -> None:
        """
        writes a string to the stream using the encoding defined by setEncoding().
        
        Line breaks or delimiters that may be necessary to support XTextInputStream.readLine() and XTextInputStream.readString() have to be added manually to the parameter string.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
