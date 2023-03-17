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
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class TransferInfo(object):
    """
    Struct Class

    contains information needed to transfer objects from one location to another.
    
    The transfer command is always called on the target folder. For a details description of the transfer command refer to the documentation of service Content.

    See Also:
        `API TransferInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1TransferInfo.html>`_
    """
    typeName: Literal['com.sun.star.ucb.TransferInfo']

    def __init__(self, MoveData: typing.Optional[bool] = ..., SourceURL: typing.Optional[str] = ..., NewTitle: typing.Optional[str] = ..., NameClash: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            MoveData (bool, optional): MoveData value.
            SourceURL (str, optional): SourceURL value.
            NewTitle (str, optional): NewTitle value.
            NameClash (int, optional): NameClash value.
        """
        ...


    @property
    def MoveData(self) -> bool:
        """
        contains the flags describing whether the data shall be moved instead of copied.
        """
        ...


    @property
    def SourceURL(self) -> str:
        """
        contains the URL of the source of the action (e.g.
        
        the URL of a file to move).
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
        
        A title clash for instance occurs, if a file named \"foo.txt\" is to be transferred to a folder already containing another file named \"foo.txt\".
        
        The value can be one of the NameClash constants.
        
        Implementations that are not able to detect whether there is a clashing resource may ignore NameClash.ERROR and NameClash.RENAME always write the new data.
        """
        ...


