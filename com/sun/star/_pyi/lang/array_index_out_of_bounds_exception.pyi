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
# Namespace: com.sun.star.lang
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing
from .index_out_of_bounds_exception import IndexOutOfBoundsException as IndexOutOfBoundsException_66d010a9
from ..uno.x_interface import XInterface as XInterface_8f010a43

class ArrayIndexOutOfBoundsException(IndexOutOfBoundsException_66d010a9):
    """
    Exception Class

    This exception is thrown to indicate that an array has been accessed with an illegal index.
    
    The index is either negative or greater than or equal to the size of the array.

    See Also:
        `API ArrayIndexOutOfBoundsException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1lang_1_1ArrayIndexOutOfBoundsException.html>`_
    """

    typeName: Literal['com.sun.star.lang.ArrayIndexOutOfBoundsException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
        """
        ...

__all__ = ['ArrayIndexOutOfBoundsException']

