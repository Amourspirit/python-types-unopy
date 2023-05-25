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
# Namespace: com.sun.star.security
from __future__ import annotations
import typing

import uno
from ..uno.x_interface import XInterface as XInterface_8f010a43


class XCertificateExtension(XInterface_8f010a43):
    """
    Interface of a PKI Certificate.
    
    This interface represents a x509 certificate.

    See Also:
        `API XCertificateExtension <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1security_1_1XCertificateExtension.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.security.XCertificateExtension'

    def isCritical(self) -> bool:
        """
        Check whether it is a critical extension.
        """
        ...

    @property
    def ExtensionId(self) -> uno.ByteSequence:
        """
        Get the extension object identifier in string.
        """
        ...
    @ExtensionId.setter
    def ExtensionId(self, value: uno.ByteSequence) -> None:
        ...
    @property
    def ExtensionValue(self) -> uno.ByteSequence:
        """
        Get the extension value.
        """
        ...
    @ExtensionValue.setter
    def ExtensionValue(self, value: uno.ByteSequence) -> None:
        ...


