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
# Namespace: com.sun.star.document
from typing_extensions import Literal
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XExtendedFilterDetection(XInterface_8f010a43):
    """
    provides a \"deep\" filter detection
    
    A \"deep\" filter detection means looking into the document stream to detect the format of it. Services of type ExtendedTypeDetection must support this interface to be called from generic load mechanism of the office for that.

    See Also:
        `API XExtendedFilterDetection <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XExtendedFilterDetection.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.document.XExtendedFilterDetection']

    def detect(self, Descriptor: object) -> str:
        """
        controls agreement of a \"flat\" TypeDetection with given URL or arguments
        
        Registered services in configuration, which support this interface for different mime types, will be called automatically to look into the document stream and decide which format it represent. Add the collected information about detected documents in given MediaDescriptor Descriptor. The decision must be returned as any valid type name (which specifies the detected format) or an empty value for unknown formats.
        """
        ...


