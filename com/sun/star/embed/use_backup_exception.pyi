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
# Namespace: com.sun.star.embed
# Libre Office Version: 2024.2
from typing_extensions import Literal
import typing
from ..io.io_exception import IOException as IOException_8c450a27
from ..uno.x_interface import XInterface as XInterface_8f010a43

class UseBackupException(IOException_8c450a27):
    """
    Exception Class

    This exception can be thrown in case a storage commit is failed.
    
    If a commit process of a storage fails on last transfer and the original content may be corrupted the storage should throw this exception to notify the user that a backup usage is required to restore the original content.
    
    The storage itself must disconnect from the medium it is based on to allow restoring. Although the storage will still contain all the data internally, and can be used as a temporary storage usually used.

    See Also:
        `API UseBackupException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1embed_1_1UseBackupException.html>`_
    """

    typeName: Literal['com.sun.star.embed.UseBackupException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., TemporaryFileURL: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            TemporaryFileURL (str, optional): TemporaryFileURL value.
        """
        ...
    @property
    def TemporaryFileURL(self) -> str:
        """
        The URL of the temporary file the storage is based on now.
        """
        ...
    @TemporaryFileURL.setter
    def TemporaryFileURL(self, value: str) -> None:
        ...

__all__ = ['UseBackupException']

