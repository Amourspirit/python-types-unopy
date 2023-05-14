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
import typing
from .x_content_provider import XContentProvider as XContentProvider_d4150cc0


class ContentProviderInfo(object):
    """
    Struct Class

    A structure for content provider information.

    See Also:
        `API ContentProviderInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1ContentProviderInfo.html>`_
    """
    typeName: Literal['com.sun.star.ucb.ContentProviderInfo']

    def __init__(self, ContentProvider: typing.Optional[XContentProvider_d4150cc0] = ..., Scheme: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            ContentProvider (XContentProvider, optional): ContentProvider value.
            Scheme (str, optional): Scheme value.
        """
        ...


    @property
    def ContentProvider(self) -> XContentProvider_d4150cc0:
        """
        The content provider.
        """
        ...

    @ContentProvider.setter
    def ContentProvider(self, value: XContentProvider_d4150cc0) -> None:
        ...

    @property
    def Scheme(self) -> str:
        """
        The scheme the Provider is registered for.
        """
        ...

    @Scheme.setter
    def Scheme(self, value: str) -> None:
        ...

