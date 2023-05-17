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
# Namespace: com.sun.star.frame
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_frame import XFrame as XFrame_7a570956


class XSynchronousFrameLoader(XInterface_8f010a43):
    """
    loads a resource into a Frame.
    
    Unlike the XFrameLoader interface, this loading will be synchronous.

    See Also:
        `API XSynchronousFrameLoader <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XSynchronousFrameLoader.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.frame.XSynchronousFrameLoader']

    def cancel(self) -> None:
        """
        cancels the loading process.
        
        No notifications (neither to the frame or the caller) must be notified. Because it's a synchronous process this cancel call can be forced by another thread the loader thread only. Method XSynchronousFrameLoader.load() must return FALSE then and caller of this method XSynchronousFrameLoader.cancel() already knows the state ...
        """
        ...
    def load(self, Descriptor: 'typing.Tuple[PropertyValue_c9610c73, ...]', Frame: 'XFrame_7a570956') -> bool:
        """
        starts the loading of the specified resource into the specified Frame.
        """
        ...


