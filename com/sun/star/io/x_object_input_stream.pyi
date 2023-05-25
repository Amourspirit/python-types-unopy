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
# Namespace: com.sun.star.io
from __future__ import annotations
import typing

from .x_data_input_stream import XDataInputStream as XDataInputStream_c56e0c2e
if typing.TYPE_CHECKING:
    from .x_persist_object import XPersistObject as XPersistObject_af2f0b79


class XObjectInputStream(XDataInputStream_c56e0c2e):
    """
    reads XPersistObject implementations from a stream

    See Also:
        `API XObjectInputStream <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XObjectInputStream.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.io.XObjectInputStream'

    def readObject(self) -> XPersistObject_af2f0b79:
        """
        reads an object from the stream.
        
        In general, it reads the service name, instantiates the object and calls read on the XPersistObject interface with itself as argument.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...


