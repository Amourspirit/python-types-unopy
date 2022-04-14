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
# Namespace: com.sun.star.uri
from typing_extensions import Literal
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XVndSunStarScriptUrl(XInterface_8f010a43):
    """
    represents absolute “vnd.sun.star.script” URLs.
    
    These URLs are of the form
    vnd-sun-star-script-url = \"VND.SUN.STAR.SCRIPT:\" name [\"?\" parameter *(\"&\" parameter)]
    name = 1*schar
    parameter = key \"=\" value
    key = 1*schar
    value = *schar
    schar = unreserved / escaped / \"$\" / \"+\" / \",\" / \":\" / \";\" / \"@\" / \"[\" / \"]\"
    See RFC 3986 RFC 2234 for details.
    
    The names, keys, and values are arbitrary Unicode strings (non-empty Unicode strings in the case of names and keys), encoded as UTF-8 byte sequences. It is an error if any of them does not represent a valid UTF-8 byte sequence. Keys are compared for equality character-by-character, without considering case folding or normalization. There may be multiple parameters with equal keys.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XVndSunStarScriptUrl <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uri_1_1XVndSunStarScriptUrl.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.uri.XVndSunStarScriptUrl']

    def getName(self) -> str:
        """
        returns the name part of this URL.
        """
    def getParameter(self, key: str) -> str:
        """
        returns the value of a parameter with a given key.
        """
    def hasParameter(self, key: str) -> bool:
        """
        returns whether this URL has a parameter with a given key.
        """
    def setName(self, name: str) -> None:
        """
        sets the name part of this URL.
        
        **since**
        
            OOo 3.0

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def setParameter(self, key: str, value: str) -> None:
        """
        sets the value of a parameter with a given key.
        
        **since**
        
            OOo 3.0

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

__all__ = ['XVndSunStarScriptUrl']

