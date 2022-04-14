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
# Namespace: com.sun.star.awt
from typing_extensions import Literal
import typing
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .vcl_container_event import VclContainerEvent as VclContainerEvent_e1800d1e

class XVclContainerListener(XEventListener_c7230c4a):
    """
    makes it possible to receive container events.
    
    Container events are provided only for notification purposes. The VCL will automatically handle add and remove operations internally.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XVclContainerListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XVclContainerListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XVclContainerListener']

    def windowAdded(self, e: 'VclContainerEvent_e1800d1e') -> None:
        """
        is invoked when a window has been added to the VCL container window.
        """
    def windowRemoved(self, e: 'VclContainerEvent_e1800d1e') -> None:
        """
        is invoked when a window has been removed from the VCL container window.
        """

__all__ = ['XVclContainerListener']

