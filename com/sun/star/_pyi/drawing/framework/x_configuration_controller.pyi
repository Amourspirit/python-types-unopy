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
# Namespace: com.sun.star.drawing.framework
from typing_extensions import Literal
import typing
from .x_configuration_controller_broadcaster import XConfigurationControllerBroadcaster as XConfigurationControllerBroadcaster_5e871a2e
from .x_configuration_controller_request_queue import XConfigurationControllerRequestQueue as XConfigurationControllerRequestQueue_7a5d1ab2
from .x_resource_factory_manager import XResourceFactoryManager as XResourceFactoryManager_3eb91523
if typing.TYPE_CHECKING:
    from .resource_activation_mode import ResourceActivationMode as ResourceActivationMode_2b5e14cf
    from .x_configuration import XConfiguration as XConfiguration_8f0511a0
    from .x_resource import XResource as XResource_3bcd0f90
    from .x_resource_id import XResourceId as XResourceId_5be3103d

class XConfigurationController(XConfigurationControllerBroadcaster_5e871a2e, XConfigurationControllerRequestQueue_7a5d1ab2, XResourceFactoryManager_3eb91523):
    """
    The configuration controller is responsible for the management of the set of active resources.
    
    There are two configurations of resources:
    
    When the two configurations differ then the current configuration is updated eventually to reflect the requested configuration. An update takes place when the following three conditions are fulfilled.
    
    Requests for configuration changes are handled in a two step process:
    
    The configuration controller sends the following events:

    See Also:
        `API XConfigurationController <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1XConfigurationController.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.drawing.framework.XConfigurationController']

    def getCurrentConfiguration(self) -> 'XConfiguration_8f0511a0':
        """
        Return a copy of the current configuration.
        
        Modifications to the returned configuration have no effect on the drawing framework.
        """
        ...
    def getRequestedConfiguration(self) -> 'XConfiguration_8f0511a0':
        """
        Return a copy of the requested configuration.
        
        Modifications to the returned configuration have no effect on the drawing framework.
        """
        ...
    def getResource(self, xResourceId: 'XResourceId_5be3103d') -> 'XResource_3bcd0f90':
        """
        Return the active resource specified by the given resource id.
        """
        ...
    def lock(self) -> None:
        """
        Lock the processing of configuration change requests.
        
        This is only necessary when more than one change request is being made in a row. It prevents an update being made (with all the visible UI changes) before all change requests are being made.
        
        Recursive lock() calls are recognized: the configuration controller is locked while lock() was called more often than unlock().
        """
        ...
    def requestResourceActivation(self, xResourceId: 'XResourceId_5be3103d', eMode: 'ResourceActivationMode_2b5e14cf') -> None:
        """
        Request the activation of a resource.
        
        The request is processed asynchronously. Notifications about configuration changes are sent after this call returns.
        
        When eMode is REPLACE then, before adding the resource activation to the request queue, similar resources linked to the same anchor are removed. This makes it easier to switch between resources whose activation is mutually exclusive. For example, there can only be one view per pane, so before activating a new view the old one has to be deactivated.
        
        When eMode is ADD then the resource is requested without further changes.
        """
        ...
    def requestResourceDeactivation(self, xResourceId: 'XResourceId_5be3103d') -> None:
        """
        Request the deactivation of a resource.
        
        The request is processed asynchronously. Notifications about configuration changes are sent after this call returns.
        
        Requesting the deactivation of a resource that is not active is not an error.
        """
        ...
    def restoreConfiguration(self, xConfiguration: 'XConfiguration_8f0511a0') -> None:
        """
        Replace the requested configuration with the given configuration and schedule an update of the current configuration.
        
        Together with the getCurrentConfiguration() and getRequestedConfiguration() methods this allows the saving and restoring of configurations. However, the given configuration can have other origins then these methods.
        
        The given configuration is transformed into a list of change requests so that the resulting requested configuration equals the given configuration. This has the advantage that not only the resource activations and deactivations but all configuration changes are properly broadcasted.
        
        Note that because of the configuration change notifications listeners can make more configuration change requests, so that the resulting requested configuration can be different from the given configuration.
        """
        ...
    def unlock(self) -> None:
        """
        Unlock the processing of configuration change requests.
        
        When unlock() is called as many times as lock() and the queue of configuration change requests is not empty the configuration controller continues the processing of the change requests. An update of the current configuration will eventually being made.
        """
        ...
    def update(self) -> None:
        """
        Explicitly request an update of the current configuration.
        
        Call it when a resource is activated or deactivated without the control and knowledge of the drawing framework. Calling this method (from outside the drawing framework) should hardly every be necessary.
        """
        ...


