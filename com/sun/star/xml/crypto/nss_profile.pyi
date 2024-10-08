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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.xml.crypto
# Libre Office Version: 2024.2
import typing
from ...mozilla.mozilla_product_type import MozillaProductType as MozillaProductType_2e210f5b


class NSSProfile(object):
    """
    Struct Class

    
    **since**
    
        LibreOffice 7.1

    See Also:
        `API NSSProfile <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1xml_1_1crypto_1_1NSSProfile.html>`_
    """
    typeName: str = 'com.sun.star.xml.crypto.NSSProfile'

    def __init__(self, Name: typing.Optional[str] = ..., Path: typing.Optional[str] = ..., Type: typing.Optional[MozillaProductType_2e210f5b] = ...) -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Path (str, optional): Path value.
            Type (MozillaProductType, optional): Type value.
        """
        ...

    @property
    def Name(self) -> str:
        """
        the name of the NSS profile
        
        Normally the name will reflect the name of the Mozilla profile. But the profile list also contains the following special entries: MANUAL and MOZILLA_CERTIFICATE_FOLDER. These will have a product type of MozillaProductType.Default and might have an empty path, if that value is not available.
        """
        ...
    @Name.setter
    def Name(self, value: str) -> None:
        ...
    @property
    def Path(self) -> str:
        """
        the path to the NSS databases
        """
        ...
    @Path.setter
    def Path(self, value: str) -> None:
        ...
    @property
    def Type(self) -> MozillaProductType_2e210f5b:
        """
        the type of the NSS profile
        """
        ...
    @Type.setter
    def Type(self, value: MozillaProductType_2e210f5b) -> None:
        ...

