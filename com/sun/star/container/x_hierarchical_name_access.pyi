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
# Namespace: com.sun.star.container
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XHierarchicalNameAccess(XInterface_8f010a43):
    """
    is used to have hierarchical access to elements within a container.
    
    You address an object of a specific level in the hierarchy by giving its fully qualified name, e.g., \"com.sun.star.uno.XInterface\".
    
    To implement inaccurate name access, support the com.sun.star.beans.XExactName interface.

    See Also:
        `API XHierarchicalNameAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1container_1_1XHierarchicalNameAccess.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.container.XHierarchicalNameAccess'

    def getByHierarchicalName(self, aName: str) -> typing.Any:
        """

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    def hasByHierarchicalName(self, aName: str) -> bool:
        """
        In many cases, the next call is XNameAccess.getByName(). You should optimize this case.
        """
        ...



