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
# Namespace: com.sun.star.sheet.opencl
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .open_cl_platform import OpenCLPlatform as OpenCLPlatform_36540f36

class XOpenCLSelection(XInterface_8f010a43):
    """

    See Also:
        `API XOpenCLSelection <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1opencl_1_1XOpenCLSelection.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.opencl.XOpenCLSelection']

    def disableAutomaticDeviceSelection(self) -> None:
        """
        Disables automatic OpenCL Device Selection.
        """
    def disableOpcodeSubsetTest(self) -> None:
        """
        """
    def enableAutomaticDeviceSelection(self, force: bool) -> None:
        """
        Enables automatic OpenCL Device Selection.
        """
    def enableOpcodeSubsetTest(self) -> None:
        """
        """
    def enableOpenCL(self, enable: bool) -> None:
        """
        Enables or disables use of OpenCL for calculations.
        
        When using this API to enable OpenCL the configuration parameters are set to their built-in default values, not ones read from the installation of user-specific configuration.
        """
    def getDeviceID(self) -> int:
        """
        returns the index of the currently selected device.
        
        This is an index into the sequence of devices in the OpenCLPLatform object the device is part of in the current instance of LibreOffice (and not some a priori defined identifier for a specific model of device accessed through a specific platform).
        """
    def getFormulaCellNumberLimit(self) -> int:
        """
        """
    def getOpenCLPlatforms(self) -> 'typing.Tuple[OpenCLPlatform_36540f36, ...]':
        """
        lists all OpenCL devices and platforms
        """
    def getPlatformID(self) -> int:
        """
        returns the index of the platform of the currently selected device.
        
        This is an index into the sequence that getOpenCLPlatforms returns in the current instance of LibreOffice (and not some a priori defined identifier for an OpenCL platform).
        """
    def isOpcodeSubsetTested(self) -> bool:
        """
        """
    def isOpenCLEnabled(self) -> bool:
        """
        Returns true if calculation with OpenCL is enabled (at all).
        
        The actual use of OpenCL for a formula is also affected by the configuration settings specifying whether OpenCL is used for all opcodes or just for a subset, and the deny- and allowlists of OpenCL implementations that are in use.
        """
    def selectOpenCLDevice(self, platform: int, device: int) -> None:
        """
        Select the OpenCL device with the given platform and device number.
        
        The platform number corresponds to an index into the sequence returned by getOpenCLPlatforms, and the device number corresponds to an index into the sequence of devices in that platform.
        """
    def setFormulaCellNumberLimit(self, number: int) -> None:
        """
        """

__all__ = ['XOpenCLSelection']

