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
# Namespace: com.sun.star.document
# Libre Office Version: 2024.2
from typing_extensions import Literal
import typing
from ..io.io_exception import IOException as IOException_8c450a27
from ..uno.x_interface import XInterface as XInterface_8f010a43

class LockFileCorruptRequest(IOException_8c450a27):
    """
    Exception Class

    Is used for interaction handle to query user's decision when the lock file is corrupt.
    
    **since**
    
        LibreOffice 6.0

    See Also:
        `API LockFileCorruptRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1document_1_1LockFileCorruptRequest.html>`_
    """

    typeName: Literal['com.sun.star.document.LockFileCorruptRequest']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
        """
        ...

__all__ = ['LockFileCorruptRequest']

