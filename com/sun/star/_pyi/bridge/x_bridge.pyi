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
# Namespace: com.sun.star.bridge
from typing_extensions import Literal
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XBridge(XInterface_8f010a43):
    """
    main interface for an interprocess bridge.

    See Also:
        `API XBridge <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1bridge_1_1XBridge.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.bridge.XBridge']

    def getDescription(self) -> str:
        """
        a unique descriptive string: protocol + \":\" + XConnection.getDescription()
        """
        ...
    def getInstance(self, sInstanceName: str) -> 'XInterface_8f010a43':
        """
        tries to get an interface from the remote that is known by this name.
        
        In general, this method is called once to get the initial object from the remote, but it is allowed to call the method multiple times.
        """
        ...
    def getName(self) -> str:
        """
        name that the bridge got when it was created.
        """
        ...


