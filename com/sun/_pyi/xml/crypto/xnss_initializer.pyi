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
from .x_cipher_context_supplier import XCipherContextSupplier as XCipherContextSupplier_9fd31214
from .x_digest_context_supplier import XDigestContextSupplier as XDigestContextSupplier_a0151219
if typing.TYPE_CHECKING:
    from .nss_profile import NSSProfile as NSSProfile_e1f00ced

class XNSSInitializer(XCipherContextSupplier_9fd31214, XDigestContextSupplier_a0151219):
    """
    
    **since**
    
        LibreOffice 4.0

    See Also:
        `API XNSSInitializer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1XNSSInitializer.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.crypto.XNSSInitializer']

    def getNSSProfiles(self) -> 'typing.Tuple[NSSProfile_e1f00ced, ...]':
        """
        get the current profile list
        
        **since**
        
            LibreOffice 7.1
        """
    @property
    def IsNSSinitialized(self) -> bool:
        """
        the state of the NSS initialization
        
        This attribute returns true, if the NSS library is initialized.
        
        **since**
        
            LibreOffice 7.1
        """

    @property
    def NSSPath(self) -> str:
        """
        the current path to the NSS databases
        
        This attribute returns the current setting, based on the user selection or automatic detection. This value can change until someone uses NSS crypto functions, because just then LibreOffice initializes the NSS library and the value stays fixed until LibreOffice is restarted!
        
        **since**
        
            LibreOffice 7.1
        """


__all__ = ['XNSSInitializer']

