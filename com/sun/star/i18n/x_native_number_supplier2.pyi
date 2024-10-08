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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.i18n
from __future__ import annotations
import typing

from .x_native_number_supplier import XNativeNumberSupplier as XNativeNumberSupplier_1eb80ec4
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa


class XNativeNumberSupplier2(XNativeNumberSupplier_1eb80ec4):
    """
    Methods to convert between strings of ASCII Arabic digits and native numeral strings, using NatNum params.
    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API XNativeNumberSupplier2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XNativeNumberSupplier2.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.i18n.XNativeNumberSupplier2'

    def getNativeNumberStringParams(self, NumberString: str, Locale: Locale_70d308fa, NativeNumberMode: int, NativeNumberParameters: str) -> str:
        """
        Returns native number string for given number string, using NatNum params.
        """
        ...


