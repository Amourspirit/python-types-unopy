# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from typing_extensions import Literal
from .transfer_info import TransferInfo as TransferInfo_a4600b13
import typing


class TransferInfo2(TransferInfo_a4600b13):
    """
    Struct Class

    extends TransferInfo structure to give some additional parameters for transfers.

    See Also:
        `API TransferInfo2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1TransferInfo2.html>`_
    """
    typeName: Literal['com.sun.star.ucb.TransferInfo2']

    def __init__(self, MoveData: typing.Optional[bool] = ..., SourceURL: typing.Optional[str] = ..., NewTitle: typing.Optional[str] = ..., NameClash: typing.Optional[int] = ..., MimeType: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            MoveData (bool, optional): MoveData value.
            SourceURL (str, optional): SourceURL value.
            NewTitle (str, optional): NewTitle value.
            NameClash (int, optional): NameClash value.
            MimeType (str, optional): MimeType value.
        """
        ...


    @property
    def MimeType(self) -> str:
        """
        contains the MIME type of the source of the action
        """
        ...

    @MimeType.setter
    def MimeType(self, value: str) -> None:
        ...

