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
# Namespace: com.sun.star.text
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47


class XFormField(XInterface_8f010a43):
    """
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XFormField <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XFormField.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.text.XFormField'

    def getFieldType(self) -> str:
        """
        """
        ...
    def getParameters(self) -> XNameContainer_cb90e47:
        """
        """
        ...
    def setFieldType(self, fieldType: str) -> None:
        """
        """
        ...


