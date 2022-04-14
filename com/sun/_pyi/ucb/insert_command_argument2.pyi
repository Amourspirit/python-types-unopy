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
# Libre Office Version: 7.2
from typing_extensions import Literal
from .insert_command_argument import InsertCommandArgument as InsertCommandArgument_19550eb9
from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
import typing


class InsertCommandArgument2(InsertCommandArgument_19550eb9):
    """
    Struct Class

    The argument for the command \"insert\" augmented with some properties.

    See Also:
        `API InsertCommandArgument2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1InsertCommandArgument2.html>`_
    """
    typeName: Literal['com.sun.star.ucb.InsertCommandArgument2']

    def __init__(self, Data: typing.Optional[XInputStream_98d40ab4] = ..., ReplaceExisting: typing.Optional[bool] = ..., MimeType: typing.Optional[str] = ..., DocumentId: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Data (XInputStream, optional): Data value.
            ReplaceExisting (bool, optional): ReplaceExisting value.
            MimeType (str, optional): MimeType value.
            DocumentId (str, optional): DocumentId value.
        """


    @property
    def MimeType(self) -> str:
        """
        contains the MIME type of the document to insert
        """


    @property
    def DocumentId(self) -> str:
        """
        contains the Document Id of the document to insert
        """



__all__ = ['InsertCommandArgument2']
