# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.form
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_reset_listener import XResetListener as XResetListener_c86e0c5d


class XReset(XInterface_8f010a43):
    """
    provides functionality to reset components to some default values.
    
    The semantics of default value depends on the providing service.

    See Also:
        `API XReset <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XReset.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.form.XReset'

    def addResetListener(self, aListener: XResetListener_c86e0c5d) -> None:
        """
        adds the specified listener to receive events related to resetting the component.
        """
        ...
    def removeResetListener(self, aListener: XResetListener_c86e0c5d) -> None:
        """
        removes the specified listener
        """
        ...
    def reset(self) -> None:
        """
        resets a component to some default value.
        """
        ...


