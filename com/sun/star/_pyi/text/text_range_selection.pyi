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
# Namespace: com.sun.star.text
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from .text_position import TextPosition as TextPosition_b2ae0bc7


class TextRangeSelection(object):
    """
    Struct Class


    See Also:
        `API TextRangeSelection <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1TextRangeSelection.html>`_
    """
    typeName: Literal['com.sun.star.text.TextRangeSelection']

    def __init__(self, Start: typing.Optional[TextPosition_b2ae0bc7] = ..., End: typing.Optional[TextPosition_b2ae0bc7] = ...) -> None:
        """
        Constructor

        Arguments:
            Start (TextPosition, optional): Start value.
            End (TextPosition, optional): End value.
        """
        ...


    @property
    def Start(self) -> TextPosition_b2ae0bc7:
        ...


    @property
    def End(self) -> TextPosition_b2ae0bc7:
        ...


