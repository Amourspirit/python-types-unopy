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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.ucb
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .content_info import ContentInfo as ContentInfo_98f60aa9
    from .x_content import XContent as XContent_79db0975


class XContentCreator(XInterface_8f010a43):
    """
    A creator for new (persistent) contents, like file system folders.
    
    Creation of a new (persistent) content:
    
    This interface is deprecated. Use Content property \"CreatableContentsInfo\" and command \"createNewContent\" instead.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XContentCreator <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XContentCreator.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.ucb.XContentCreator'

    def createNewContent(self, Info: ContentInfo_98f60aa9) -> XContent_79db0975:
        """
        creates a new content of given type.
        """
        ...
    def queryCreatableContentsInfo(self) -> typing.Tuple[ContentInfo_98f60aa9, ...]:
        """
        returns a list with information about the creatable contents.
        """
        ...


