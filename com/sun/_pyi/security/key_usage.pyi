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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.security
from typing_extensions import Literal


class KeyUsage:
    """
    Const Class


    See Also:
        `API KeyUsage <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1security_1_1KeyUsage.html>`_
    """
    DIGITAL_SIGNATURE: Literal[128]
    NON_REPUDIATION: Literal[64]
    KEY_ENCIPHERMENT: Literal[32]
    DATA_ENCIPHERMENT: Literal[16]
    KEY_AGREEMENT: Literal[8]
    KEY_CERT_SIGN: Literal[4]
    CRL_SIGN: Literal[2]

__all__ = ['KeyUsage']
