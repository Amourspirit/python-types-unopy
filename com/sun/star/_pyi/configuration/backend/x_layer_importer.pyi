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
# Namespace: com.sun.star.configuration.backend
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_backend import XBackend as XBackend_6ce81076
    from .x_layer import XLayer as XLayer_4cd50fcb

class XLayerImporter(XInterface_8f010a43):
    """
    allows importing a layer into a Backend
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XLayerImporter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1XLayerImporter.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.configuration.backend.XLayerImporter']

    def getTargetBackend(self) -> 'XBackend_6ce81076':
        """
        gets the target backend for importing.
        """
        ...
    def importLayer(self, aLayer: 'XLayer_4cd50fcb') -> None:
        """
        Imports the layer given into the backend.
        
        This method imports data for the current entity of the backend.

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.NullPointerException: ``NullPointerException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def importLayerForEntity(self, aLayer: 'XLayer_4cd50fcb', aEntity: str) -> None:
        """
        Imports the layer given into the backend for a given entity.
        
        This method imports data for the current entity of the backend.

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.NullPointerException: ``NullPointerException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def setTargetBackend(self, aBackend: 'XBackend_6ce81076') -> None:
        """
        sets the target backend for importing.

        Raises:
            com.sun.star.lang.NullPointerException: ``NullPointerException``
        """
        ...


