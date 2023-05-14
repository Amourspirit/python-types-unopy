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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.beans
from .x_fast_property_set import XFastPropertySet as XFastPropertySet_ee6b0d88
from .x_multi_property_set import XMultiPropertySet as XMultiPropertySet_fd880e05
from .x_property_access import XPropertyAccess as XPropertyAccess_e1d40d20
from .x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_property_state import XPropertyState as XPropertyState_d55c0ccf

class PropertySet(XFastPropertySet_ee6b0d88, XMultiPropertySet_fd880e05, XPropertyAccess_e1d40d20, XPropertySet_bc180bfa, XPropertyState_d55c0ccf):
    """
    Service Class

    This is a generic service which should be supported by all services which have properties.
    
    It specifies several, mostly optional ways to access properties.

    See Also:
        `API PropertySet <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1beans_1_1PropertySet.html>`_
    """
    ...

