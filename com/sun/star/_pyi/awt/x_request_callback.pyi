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
from abc import ABC
if typing.TYPE_CHECKING:
    from .x_callback import XCallback as XCallback_838209b9

class XRequestCallback(ABC):
    """
    specifies an interface which can be used to call back an implementation

    See Also:
        `API XRequestCallback <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XRequestCallback.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XRequestCallback']

    def addCallback(self, xCallback: 'XCallback_838209b9', aData: object) -> None:
        """
        adds a callback request to the implementation
        """
        ...


