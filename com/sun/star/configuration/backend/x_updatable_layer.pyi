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


class XUpdatableLayer(XLayer_4cd50fcb):
    """
    Provides access to a read-write layer of configuration data for a given component and entity.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XUpdatableLayer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1XUpdatableLayer.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.configuration.backend.XUpdatableLayer'

    def replaceWith(self, aNewLayer: XLayer_4cd50fcb) -> None:
        """
        Replaces the current layer with the layer given as input parameter.
        
        After the replacement has been performed, reading the layer will return the new content. Some implementations may not support this, so after an update XLayer.readData() may fail.

        Raises:
            com.sun.star.lang.NullPointerException: ``NullPointerException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
            MalformedDataException: ``MalformedDataException``
        """
        ...


