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


class TransferResult(object):
    """
    Struct Class

    Information about a transfer activity.

    See Also:
        `API TransferResult <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1TransferResult.html>`_
    """
    typeName: Literal['com.sun.star.ucb.TransferResult']

    def __init__(self, Source: typing.Optional[str] = ..., Target: typing.Optional[str] = ..., Result: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (str, optional): Source value.
            Target (str, optional): Target value.
            Result (object, optional): Result value.
        """


    @property
    def Source(self) -> str:
        """
        The URL of the source object.
        """


    @property
    def Target(self) -> str:
        """
        The URL of the target folder into which to transfer (a copy of) the source object.
        """


    @property
    def Result(self) -> object:
        """
        Either void if the transfer has been carried out successfully, or an exception indicating the kind of failure.
        """

