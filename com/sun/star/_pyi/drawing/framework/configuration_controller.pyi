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
# Namespace: com.sun.star.drawing.framework
import typing
from .x_configuration_controller import XConfigurationController as XConfigurationController_557c15c4
if typing.TYPE_CHECKING:
    from ...frame.x_controller import XController as XController_b00e0b8f

class ConfigurationController(XConfigurationController_557c15c4):
    """
    Service Class

    See XConfigurationController for a description of the configuration controller.
    
    This service is used at the moment by the XControllerManager to create a configuration controller. This allows developers to replace the default implementation of the configuration controller with their own. This may not be a useful feature. Furthermore the sub controllers may need a tighter coupling than the interfaces allow. These are reasons for removing this service in the future and let the controller manager create the sub controllers directly.

    See Also:
        `API ConfigurationController <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1ConfigurationController.html>`_
    """
    def create(self, xController: 'XController_b00e0b8f') -> None:
        """
        """

