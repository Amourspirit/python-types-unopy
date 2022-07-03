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
# Libre Office Version: 7.3
# Namespace: com.sun.star.configuration.backend
from .x_composite_layer import XCompositeLayer as XCompositeLayer_ed7f137e
from ...util.x_time_stamped import XTimeStamped as XTimeStamped_b09b0b7b

class Layer(XCompositeLayer_ed7f137e, XTimeStamped_b09b0b7b):
    """
    Service Class

    provides read-only access to a configuration data layer.
    
    A layer contains the configuration setting changes to be performed on a default settings tree to obtain the values of those settings for a given entity and component.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API Layer <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1Layer.html>`_
    """
    @property
    def URL(self) -> str:
        """
        The URL of the layer data.
        
        **since**
        
            OOo 2.0
        """
        ...


