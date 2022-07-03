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
# Namespace: com.sun.star.frame
from typing_extensions import Literal
import typing
from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from .x_frame import XFrame as XFrame_7a570956
    from .x_model import XModel as XModel_7a6e095c

class XController(XComponent_98dc0ab5):
    """
    With this interface, components viewed in a Frame can serve events (by supplying dispatches).

    See Also:
        `API XController <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XController.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.frame.XController']

    def attachFrame(self, Frame: 'XFrame_7a570956') -> None:
        """
        is called to attach the controller with its managing frame.
        """
        ...
    def attachModel(self, Model: 'XModel_7a6e095c') -> bool:
        """
        is called to attach the controller to a new model.
        """
        ...
    def getFrame(self) -> 'XFrame_7a570956':
        """
        provides access to owner frame of this controller
        """
        ...
    def getModel(self) -> 'XModel_7a6e095c':
        """
        provides access to currently attached model
        """
        ...
    def getViewData(self) -> object:
        """
        provides access to current view status
        """
        ...
    def restoreViewData(self, Data: object) -> None:
        """
        restores the view status using the data gotten from a previous call to XController.getViewData().
        """
        ...
    def suspend(self, Suspend: bool) -> bool:
        """
        is called to prepare the controller for closing the view
        """
        ...


