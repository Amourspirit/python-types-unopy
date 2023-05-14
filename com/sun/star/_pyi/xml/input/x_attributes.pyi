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
# Namespace: com.sun.star.xml.input
from typing_extensions import Literal
from ...uno.x_interface import XInterface as XInterface_8f010a43

class XAttributes(XInterface_8f010a43):
    """
    An element's attributes.

    See Also:
        `API XAttributes <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1input_1_1XAttributes.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.input.XAttributes']

    def getIndexByQName(self, qName: str) -> int:
        """
        Gets attribute index passing a QName.
        """
        ...
    def getIndexByUidName(self, uid: int, localName: str) -> int:
        """
        Gets attribute index passing a namespace uid and a local name.
        """
        ...
    def getLength(self) -> int:
        """
        Gets the number of attributes.
        """
        ...
    def getLocalNameByIndex(self, nIndex: int) -> str:
        """
        Gets the local name of an attribute.
        """
        ...
    def getQNameByIndex(self, nIndex: int) -> str:
        """
        Gets the QName of an attribute.
        """
        ...
    def getTypeByIndex(self, nIndex: int) -> str:
        """
        Gets the type of an attribute, if possible.
        """
        ...
    def getUidByIndex(self, nIndex: int) -> int:
        """
        Gets the namespace uid of an attribute.
        """
        ...
    def getValueByIndex(self, nIndex: int) -> str:
        """
        Gets the value of an attribute.
        """
        ...
    def getValueByUidName(self, uid: int, localName: str) -> str:
        """
        For convenience: Gets the value of an attribute passing uid, local name.
        """
        ...


