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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.graphic
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ..beans.property_values import PropertyValues as PropertyValues_d6470ce6
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from ..io.x_stream import XStream as XStream_678908a4

class MediaProperties(ABC):
    """
    Service Class

    This service describes the properties that are used when using the XGraphicProvider interface methods.

    See Also:
        `API MediaProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1graphic_1_1MediaProperties.html>`_
    """
    @property
    def FilterData(self) -> 'PropertyValues_d6470ce6':
        """
        Additional properties that will be passed to the appropriate filter module.
        """
        ...
    @FilterData.setter
    def FilterData(self, value: 'PropertyValues_d6470ce6') -> None:
        ...
    @property
    def InputStream(self) -> 'XInputStream_98d40ab4':
        """
        This property is only used for loading graphics or querying graphic descriptors.
        
        A InputStream can be used instead of the URL property
        """
        ...
    @InputStream.setter
    def InputStream(self, value: 'XInputStream_98d40ab4') -> None:
        ...
    @property
    def MimeType(self) -> str:
        """
        This property is only used for storing graphics and describes the format into which the graphic is to be converted.
        
        At the moment, the following mime types are supported for storing graphics:
        """
        ...
    @MimeType.setter
    def MimeType(self, value: str) -> None:
        ...
    @property
    def OutputStream(self) -> 'XStream_678908a4':
        """
        This property is only used for storing graphics.
        
        A OutputStream can be used instead of the URL property
        """
        ...
    @OutputStream.setter
    def OutputStream(self, value: 'XStream_678908a4') -> None:
        ...
    @property
    def URL(self) -> str:
        """
        Property that describes the location of the source or target of the graphic as URL.
        
        A URL can be used instead of the InputStream or OutputStream property
        
        In addition to the normal protocols like file:// or http:// you can use private URLs as follows to get access to graphics lying inside the graphicrepository system within an Office context:
        
        Note: As of LibreOffice 6.1 GraphicObject scheme URLs are not supported anymore. For example:
        """
        ...
    @URL.setter
    def URL(self, value: str) -> None:
        ...

