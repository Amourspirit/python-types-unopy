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
if typing.TYPE_CHECKING:
    from .data_flavor import DataFlavor as DataFlavor_ffd30deb

class XTransferableEx(XInterface_8f010a43):
    """
    Interface to be implemented by objects used to provide data for a transfer operation.

    See Also:
        `API XTransferableEx <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1XTransferableEx.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.datatransfer.XTransferableEx']

    def queryTransferDataFlavors(self, requestedFlavors: 'typing.Tuple[DataFlavor_ffd30deb, ...]') -> 'typing.Tuple[DataFlavor_ffd30deb, ...]':
        """
        """

__all__ = ['XTransferableEx']

