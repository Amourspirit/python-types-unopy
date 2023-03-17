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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class NameToken(object):
    """
    Struct Class

    contains the information regarding named tokens

    See Also:
        `API NameToken <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1NameToken.html>`_
    """
    typeName: Literal['com.sun.star.sheet.NameToken']

    def __init__(self, Index: typing.Optional[int] = ..., Sheet: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Index (int, optional): Index value.
            Sheet (int, optional): Sheet value.
        """
        ...


    @property
    def Index(self) -> int:
        ...


    @property
    def Sheet(self) -> int:
        ...


