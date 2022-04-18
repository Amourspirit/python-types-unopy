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
# Namespace: com.sun.star.document
from typing_extensions import Literal
import typing
from .x_embedded_object_supplier import XEmbeddedObjectSupplier as XEmbeddedObjectSupplier_8b631174
if typing.TYPE_CHECKING:
    from ..embed.x_embedded_object import XEmbeddedObject as XEmbeddedObject_ddee0cbe
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc

class XEmbeddedObjectSupplier2(XEmbeddedObjectSupplier_8b631174):
    """
    represents something that provides an embedded object.

    See Also:
        `API XEmbeddedObjectSupplier2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XEmbeddedObjectSupplier2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.document.XEmbeddedObjectSupplier2']

    def getExtendedControlOverEmbeddedObject(self) -> 'XEmbeddedObject_ddee0cbe':
        """
        returns the object which is embedded into this object.
        
        This method does not return the model that is controlled by the embedded object, but the embedded object itself.
        """
    @property
    def Aspect(self) -> int:
        """
        allows to control the aspect of the object.
        """

    @property
    def ReplacementGraphic(self) -> 'XGraphic_a4da0afc':
        """
        allows to get the replacement image of the object.
        """

