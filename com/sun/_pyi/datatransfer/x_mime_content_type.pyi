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
# Namespace: com.sun.star.datatransfer
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XMimeContentType(XInterface_8f010a43):
    """
    An implementation of this interface represents a MIME content-type that conforms to Rfc2045 and Rfc2046.
    
    Instances that implement this interface could be created using the interface XMimeContentTypeFactory.

    See Also:
        `API XMimeContentType <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1XMimeContentType.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.datatransfer.XMimeContentType']

    def getFullMediaType(self) -> str:
        """
        To get the full media/submedia type of the MIME content-type.
        """
    def getMediaSubtype(self) -> str:
        """
        To get the media subtype of the MIME content-type.
        """
    def getMediaType(self) -> str:
        """
        To get the media type of the MIME content-type.
        """
    def getParameterValue(self, aName: str) -> str:
        """
        To get the value of a specified parameter.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
    def getParameters(self) -> 'typing.Tuple[str, ...]':
        """
        To get a list of parameters that the MIME content-type contains.
        """
    def hasParameter(self, aName: str) -> bool:
        """
        To query if a specific parameter is supported.
        
        A value of FALSE if the MIME content-type has not the specified parameter.
        """

__all__ = ['XMimeContentType']

