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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..container.x_named import XNamed as XNamed_a6520b08

class DataPilotItem(XPropertySet_bc180bfa, XNamed_a6520b08):
    """
    Service Class

    represents a single item in a data pilot field.
    
    **since**
    
        OOo 2.4

    See Also:
        `API DataPilotItem <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1DataPilotItem.html>`_
    """
    @property
    def IsHidden(self) -> bool:
        """
        specifies whether the item is hidden.
        """
        ...
    @property
    def Position(self) -> int:
        """
        specifies the item's position in its field if sorting is manual.
        
        **since**
        
            OOo 2.4
        """
        ...
    @property
    def ShowDetail(self) -> bool:
        """
        specifies whether the item is showing detail.
        """
        ...


