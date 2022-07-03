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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from .transfer_command_operation import TransferCommandOperation as TransferCommandOperation_486a0ff7


class GlobalTransferCommandArgument(object):
    """
    Struct Class

    This struct contains information needed to transfer objects from one location to another.

    See Also:
        `API GlobalTransferCommandArgument <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1GlobalTransferCommandArgument.html>`_
    """
    typeName: Literal['com.sun.star.ucb.GlobalTransferCommandArgument']

    def __init__(self, Operation: typing.Optional[TransferCommandOperation_486a0ff7] = ..., SourceURL: typing.Optional[str] = ..., TargetURL: typing.Optional[str] = ..., NewTitle: typing.Optional[str] = ..., NameClash: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Operation (TransferCommandOperation, optional): Operation value.
            SourceURL (str, optional): SourceURL value.
            TargetURL (str, optional): TargetURL value.
            NewTitle (str, optional): NewTitle value.
            NameClash (int, optional): NameClash value.
        """
        ...


    @property
    def Operation(self) -> TransferCommandOperation_486a0ff7:
        """
        contains the action to perform ( COPY, MOVE, LINK ).
        """
        ...


    @property
    def SourceURL(self) -> str:
        """
        contains the URL of the source object.
        """
        ...


    @property
    def TargetURL(self) -> str:
        """
        contains the URL of the target folder.
        """
        ...


    @property
    def NewTitle(self) -> str:
        """
        contains the title of the transferred object, if it is different from the original one.
        
        If this field is filled, for example, a file will be renamed while it is being transferred.
        """
        ...


    @property
    def NameClash(self) -> int:
        """
        describes how to act in case of title clashes while transferring the data.
        
        A title clash for instance occurs, if a file named \"foo.txt\" is to be transferred to a folder already containing another file named \"foo.txt\". Refer to NameClash for possible values for this field.
        """
        ...


