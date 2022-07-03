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
# Namespace: com.sun.star.sdb
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class XDataAccessDescriptorFactory(ABC):
    """
    allows creating instances of the DataAccessDescriptor service.
    
    Data access descriptors are finally only bags of properties with a defined semantics. Depending on the context in which you use them, certain of their properties are needed or unneeded.The descriptor factory allows you to create instances which offer all properties potentially needed at a descriptor.

    See Also:
        `API XDataAccessDescriptorFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1XDataAccessDescriptorFactory.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sdb.XDataAccessDescriptorFactory']

    def createDataAccessDescriptor(self) -> 'XPropertySet_bc180bfa':
        """
        creates a DataAccessDescriptor which supports all properties defined for this service, even if they're normally optional only.
        """
        ...


