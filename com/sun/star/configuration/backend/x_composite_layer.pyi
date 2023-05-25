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
# Namespace: com.sun.star.configuration.backend
from __future__ import annotations
import typing

from .x_layer import XLayer as XLayer_4cd50fcb
if typing.TYPE_CHECKING:
    from .x_layer_handler import XLayerHandler as XLayerHandler_c5d61289


class XCompositeLayer(XLayer_4cd50fcb):
    """
    provides read access to layers that contain sublayers accessible through an additional criterion (for instance the locale they contain data for).
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XCompositeLayer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1XCompositeLayer.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.configuration.backend.XCompositeLayer'

    def listSubLayerIds(self) -> typing.Tuple[str, ...]:
        """
        Returns a list of the criteria that can be used to access the sublayers.

        Raises:
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def readSubLayerData(self, aHandler: XLayerHandler_c5d61289, aSubLayerId: str) -> None:
        """
        Describes the content of a particular sublayer to an XLayerHandler.
        
        Must be one the identifiers returned by XCompositeLayer.listSubLayerIds()

        Raises:
            com.sun.star.lang.NullPointerException: ``NullPointerException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
            MalformedDataException: ``MalformedDataException``
        """
        ...


