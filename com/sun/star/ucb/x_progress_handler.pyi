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
# Namespace: com.sun.star.ucb
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XProgressHandler(XInterface_8f010a43):
    """
    Handle a tasks notification that it has made some progress.

    See Also:
        `API XProgressHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XProgressHandler.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.ucb.XProgressHandler'

    def pop(self) -> None:
        """
        The task notifies the handler that it has finished its current activity.
        """
        ...
    def push(self, Status: typing.Any) -> None:
        """
        The task notifies the handler that it has started some new activity (possibly a sub-activity of another activity already making progress; therefore, these notifications behave in a stack-like manner).
        """
        ...
    def update(self, Status: typing.Any) -> None:
        """
        The task notifies the handler that its current activity is making progress.
        """
        ...


