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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.datatransfer
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class DataFlavor(object):
    """
    Struct Class

    Each instance represents the concept of a data format as it would appear on a clipboard, or during drag and drop.

    See Also:
        `API DataFlavor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1datatransfer_1_1DataFlavor.html>`_
    """
    typeName: Literal['com.sun.star.datatransfer.DataFlavor']

    def __init__(self, MimeType: typing.Optional[str] = ..., HumanPresentableName: typing.Optional[str] = ..., DataType: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            MimeType (str, optional): MimeType value.
            HumanPresentableName (str, optional): HumanPresentableName value.
            DataType (object, optional): DataType value.
        """


    @property
    def MimeType(self) -> str:
        """
        The MIME content-type (type/subtype) string describing the data format of the object to transfer.
        
        MimeType must conform to Rfc2045 and Rfc2046)
        """


    @property
    def HumanPresentableName(self) -> str:
        """
        A human presentable name for the data format.
        """


    @property
    def DataType(self) -> object:
        """
        The type of the object to transfer, for example, XOutputStream.
        """



__all__ = ['DataFlavor']
