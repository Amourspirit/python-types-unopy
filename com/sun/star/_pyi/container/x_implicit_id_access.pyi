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
# Libre Office Version: 7.4
# Namespace: com.sun.star.container
from typing_extensions import Literal
import typing
from .x_element_access import XElementAccess as XElementAccess_cd60e3f

class XImplicitIDAccess(XElementAccess_cd60e3f):
    """
    makes it possible to access contents through an implicit (unique) ID.

    See Also:
        `API XImplicitIDAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1container_1_1XImplicitIDAccess.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.container.XImplicitIDAccess']

    def getByImplicitID(self, ID: str) -> object:
        """

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    def getImplicitIDs(self) -> 'typing.Tuple[str, ...]':
        """
        """
        ...


