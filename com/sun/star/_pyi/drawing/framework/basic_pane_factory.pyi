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
import typing
from .x_resource_factory import XResourceFactory as XResourceFactory_b3561268
if typing.TYPE_CHECKING:
    from ...frame.x_controller import XController as XController_b00e0b8f

class BasicPaneFactory(XResourceFactory_b3561268):
    """
    Service Class

    The BasicPaneFactory is a resource factory that provides the panes used by the Draw and Impress applications.
    
    This factory provides the center, left, and right pane. For the left pane there are two URLS, private:resource/floater/LeftImpressPane and private:resource/floater/LeftDrawPane, one for Impress, the other for Draw. The center pane and the right pane have the URLs private:resource/floater/CenterPane and private:resource/floater/RightPane respectively.
    
    This factory is typically created indirectly by registering it in the configuration and have the XModuleController create it on demand.

    See Also:
        `API BasicPaneFactory <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1BasicPaneFactory.html>`_
    """
    def create(self, xController: 'XController_b00e0b8f') -> None:
        """
        Give the controller to new instances so that they have access to the drawing framework controllers.
        """
        ...


