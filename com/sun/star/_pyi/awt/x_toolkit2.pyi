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
# Namespace: com.sun.star.awt
from typing_extensions import Literal
from .x_data_transfer_provider_access import XDataTransferProviderAccess as XDataTransferProviderAccess_78691108
from .x_extended_toolkit import XExtendedToolkit as XExtendedToolkit_d4c90cc3
from .x_message_box_factory import XMessageBoxFactory as XMessageBoxFactory_edaf0d72
from .x_reschedule import XReschedule as XReschedule_993e0ab0
from .x_system_child_factory import XSystemChildFactory as XSystemChildFactory_fd200ded
from .x_toolkit import XToolkit as XToolkit_7adf0992

class XToolkit2(XDataTransferProviderAccess_78691108, XExtendedToolkit_d4c90cc3, XMessageBoxFactory_edaf0d72, XReschedule_993e0ab0, XSystemChildFactory_fd200ded, XToolkit_7adf0992):
    """
    Provides a unified interface for the new-style service Toolkit to implement.
    
    **since**
    
        LibreOffice 4.0

    See Also:
        `API XToolkit2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XToolkit2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XToolkit2']


