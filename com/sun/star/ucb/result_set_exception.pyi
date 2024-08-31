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
# Namespace: com.sun.star.ucb
# Libre Office Version: 2024.2
from typing_extensions import Literal
import typing
from ..sdbc.sql_exception import SQLException as SQLException_acc90b43
from ..uno.x_interface import XInterface as XInterface_8f010a43

class ResultSetException(SQLException_acc90b43):
    """
    Exception Class

    This exception is thrown to propagate exceptions thrown by operations on ContentResultSets.

    See Also:
        `API ResultSetException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1ResultSetException.html>`_
    """

    typeName: Literal['com.sun.star.ucb.ResultSetException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., SQLState: typing.Optional[str] = ..., ErrorCode: typing.Optional[int] = ..., NextException: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            SQLState (str, optional): SQLState value.
            ErrorCode (int, optional): ErrorCode value.
            NextException (object, optional): NextException value.
        """
        ...

__all__ = ['ResultSetException']

