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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.scanner
# Libre Office Version: 7.2
from typing_extensions import Literal
from ooo.oenv.env_const import UNO_NONE
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43
from .scan_error import ScanError as ScanError_b0d90b81

class ScannerException(Exception_85530a09):
    """
    Exception Class

    A ScannerException gets thrown if an object of type XScannerManager could not complete a specific action.

    See Also:
        `API ScannerException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1scanner_1_1ScannerException.html>`_
    """

    typeName: Literal['com.sun.star.scanner.ScannerException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., Error: typing.Optional[ScanError_b0d90b81] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Error (ScanError, optional): Error value.
        """
    @property
    def Error(self) -> ScanError_b0d90b81:
        """
        Error: contains the specific reason for failure.
        """


__all__ = ['ScannerException']

