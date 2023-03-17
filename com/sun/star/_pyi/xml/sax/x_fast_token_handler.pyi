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
# Libre Office Version: 7.4
# Namespace: com.sun.star.xml.sax
from typing_extensions import Literal
import uno
from ...uno.x_interface import XInterface as XInterface_8f010a43

class XFastTokenHandler(XInterface_8f010a43):
    """
    interface to translate XML strings to integer tokens.
    
    An instance of this interface can be registered at a XFastParser. It should be able to translate all XML names (element local names, attribute local names and constant attribute values) to integer tokens.
    
    A token value must be greater or equal to zero and less than FastToken.NAMESPACE. If a string identifier is not known to this instance, FastToken.DONTKNOW is returned.

    See Also:
        `API XFastTokenHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1sax_1_1XFastTokenHandler.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.sax.XFastTokenHandler']

    def getTokenFromUTF8(self, Identifier: uno.ByteSequence) -> int:
        """
        returns an integer token for the given string
        """
        ...
    def getUTF8Identifier(self, Token: int) -> uno.ByteSequence:
        """
        returns an identifier for the given integer token as a byte sequence encoded in UTF-8.
        """
        ...


