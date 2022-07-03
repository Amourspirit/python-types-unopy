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
# Namespace: com.sun.star.xml.crypto
from typing_extensions import Literal
import typing
import uno
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ...security.x_certificate import XCertificate as XCertificate_e55b0d3b

class XCertificateCreator(XInterface_8f010a43):
    """
    Interface for creating and adding certificates.
    
    **since**
    
        LibreOffice 6.2

    See Also:
        `API XCertificateCreator <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1XCertificateCreator.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.crypto.XCertificateCreator']

    def addDERCertificateToTheDatabase(self, aDerCertificate: uno.ByteSequence, aTrustString: str) -> 'XCertificate_e55b0d3b':
        """
        Adds a certificate to the certificate database with the trust provided by the trust string.
        """
        ...
    def createDERCertificateWithPrivateKey(self, aDerCertificate: uno.ByteSequence, aPrivateKey: uno.ByteSequence) -> 'XCertificate_e55b0d3b':
        """
        Create certificate from raw DER encoded certificate and associate the private key with the certificate.

        Raises:
            com.sun.star.uno.SecurityException: ``SecurityException``
        """
        ...


