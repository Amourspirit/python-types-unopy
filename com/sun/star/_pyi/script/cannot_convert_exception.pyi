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
# Namespace: com.sun.star.script
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43
from ..uno.type_class import TypeClass as TypeClass_853109f2

class CannotConvertException(Exception_85530a09):
    """
    Exception Class

    This exception is thrown to indicate that a type conversion can not be performed.

    See Also:
        `API CannotConvertException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1script_1_1CannotConvertException.html>`_
    """

    typeName: Literal['com.sun.star.script.CannotConvertException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., DestinationTypeClass: typing.Optional[TypeClass_853109f2] = ..., Reason: typing.Optional[int] = ..., ArgumentIndex: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            DestinationTypeClass (TypeClass, optional): DestinationTypeClass value.
            Reason (int, optional): Reason value.
            ArgumentIndex (int, optional): ArgumentIndex value.
        """
        ...
    @property
    def DestinationTypeClass(self) -> TypeClass_853109f2:
        """
        This member contains the class of the type to which the value should be converted.
        """
        ...

    @property
    def Reason(self) -> int:
        """
        This member contains the reason that the conversion failed.
        
        Have a look at FailReason.
        """
        ...

    @property
    def ArgumentIndex(self) -> int:
        """
        If the conversion of a method argument fails, this is the index of the value in the \"IN\" argument list.
        
        [optional]
        """
        ...


__all__ = ['CannotConvertException']

