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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.embed
# Libre Office Version: 2024.2
import typing
from ..beans.named_value import NamedValue as NamedValue_a37a0af3
from .x_embedded_object import XEmbeddedObject as XEmbeddedObject_ddee0cbe


class InsertedObjectInfo(object):
    """
    Struct Class

    is intended to provide result of creation of an embedded object by dialog.

    See Also:
        `API InsertedObjectInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1embed_1_1InsertedObjectInfo.html>`_
    """
    typeName: str = 'com.sun.star.embed.InsertedObjectInfo'

    def __init__(self, Object: typing.Optional[XEmbeddedObject_ddee0cbe] = ..., Options: typing.Optional[typing.Tuple[NamedValue_a37a0af3, ...]] = ...) -> None:
        """
        Constructor

        Arguments:
            Object (XEmbeddedObject, optional): Object value.
            Options (typing.Tuple[NamedValue, ...], optional): Options value.
        """
        ...

    @property
    def Object(self) -> XEmbeddedObject_ddee0cbe:
        """
        The new created embedded object.
        """
        ...
    @Object.setter
    def Object(self, value: XEmbeddedObject_ddee0cbe) -> None:
        ...
    @property
    def Options(self) -> typing.Tuple[NamedValue_a37a0af3, ...]:
        """
        Container related options selected by user.
        
        A dialog related to embedded object creation usually allows user to make some choices that can be container related. This information can be provided by this member.
        """
        ...
    @Options.setter
    def Options(self, value: typing.Tuple[NamedValue_a37a0af3, ...]) -> None:
        ...

