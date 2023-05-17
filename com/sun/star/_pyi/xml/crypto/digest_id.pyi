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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.xml.crypto
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class DigestID(object):
    """
    Const

    The constant set contains identifiers of supported digest-creation algorithms.
    
    **since**
    
        OOo 3.4

    See Also:
        `API DigestID <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1DigestID.html>`_
    """
    SHA1: Literal[1]
    """
    identifier of SHA-1 algorithm
    """
    SHA256: Literal[2]
    """
    identifier of SHA-256 algorithm
    """
    SHA1_1K: Literal[3]
    """
    identifier of SHA-1 algorithm that is applied to the first kilobyte of data.
    """
    SHA256_1K: Literal[4]
    """
    identifier of SHA-256 algorithm that is applied to the first kilobyte of data.
    """
    SHA512: Literal[5]
    """
    identifier of SHA-512 algorithm
    
    **since**
    
        LibreOffice 6.0
    """
    SHA512_1K: Literal[6]
    """
    identifier of SHA-512 algorithm that is applied to the first kilobyte of data.
    
    **since**
    
        LibreOffice 6.0
    """

