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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.java
# Libre Office Version: 2024.2
from typing_extensions import Literal
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class WrongJavaVersionException(Exception_85530a09):
    """
    Exception Class

    indicates that an operation involving Java (probably executing Java code) failed due to a wrong Java version.

    See Also:
        `API WrongJavaVersionException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1java_1_1WrongJavaVersionException.html>`_
    """

    typeName: Literal['com.sun.star.java.WrongJavaVersionException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., LowestSupportedVersion: typing.Optional[str] = ..., HighestSupportedVersion: typing.Optional[str] = ..., DetectedVersion: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            LowestSupportedVersion (str, optional): LowestSupportedVersion value.
            HighestSupportedVersion (str, optional): HighestSupportedVersion value.
            DetectedVersion (str, optional): DetectedVersion value.
        """
        ...
    @property
    def LowestSupportedVersion(self) -> str:
        """
        contains the lowest Java version for which the operation would succeed, or is left empty if this is unknown.
        """
        ...
    @LowestSupportedVersion.setter
    def LowestSupportedVersion(self, value: str) -> None:
        ...
    @property
    def HighestSupportedVersion(self) -> str:
        """
        contains the highest Java version for which the operation would succeed, or is left empty if this is unknown.
        """
        ...
    @HighestSupportedVersion.setter
    def HighestSupportedVersion(self, value: str) -> None:
        ...
    @property
    def DetectedVersion(self) -> str:
        """
        contains the Java version that has been detected, or is left empty if this is unknown.
        """
        ...
    @DetectedVersion.setter
    def DetectedVersion(self, value: str) -> None:
        ...

__all__ = ['WrongJavaVersionException']

