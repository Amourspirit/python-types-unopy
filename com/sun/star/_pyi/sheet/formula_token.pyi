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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class FormulaToken(object):
    """
    Struct Class

    contains a single token within a formula.

    See Also:
        `API FormulaToken <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1FormulaToken.html>`_
    """
    typeName: Literal['com.sun.star.sheet.FormulaToken']

    def __init__(self, OpCode: typing.Optional[int] = ..., Data: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            OpCode (int, optional): OpCode value.
            Data (object, optional): Data value.
        """
        ...


    @property
    def OpCode(self) -> int:
        """
        is the OpCode of the token.
        """
        ...

    @OpCode.setter
    def OpCode(self, value: int) -> None:
        ...

    @property
    def Data(self) -> object:
        """
        is additional data in the token, depending on the OpCode.
        """
        ...

    @Data.setter
    def Data(self, value: object) -> None:
        ...

