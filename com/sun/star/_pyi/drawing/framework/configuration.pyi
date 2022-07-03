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
# Namespace: com.sun.star.drawing.framework
from .x_configuration import XConfiguration as XConfiguration_8f0511a0

class Configuration(XConfiguration_8f0511a0):
    """
    Service Class

    This service provides the means for constructing new configurations.
    
    Most likely use is the XConfigurationController.restoreConfiguration() method.

    See Also:
        `API Configuration <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1Configuration.html>`_
    """
    def create(self) -> None:
        """
        Create an empty configuration.
        
        This should not be necessary very often. Changes to an existing configuration are more likely.
        """
        ...


