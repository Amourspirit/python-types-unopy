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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.embed
from typing_extensions import Literal
import typing
from .x_common_embed_persist import XCommonEmbedPersist as XCommonEmbedPersist_16930e8d
if typing.TYPE_CHECKING:
    from .x_storage import XStorage as XStorage_8e460a32

class XLinkageSupport(XCommonEmbedPersist_16930e8d):
    """
    specifies an additional implementation for linked embedded object support.

    See Also:
        `API XLinkageSupport <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XLinkageSupport.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.embed.XLinkageSupport']

    def breakLink(self, xStorage: 'XStorage_8e460a32', sEntryName: str) -> None:
        """
        breaks the link and provides the object with a parent storage and a name for object's entry
        
        This method can be used only for links implementations that implement the whole set of embedded object interfaces. Usually the sets of interfaces are the same for links and objects. An example of exception from this are OOo links that do not implement XEmbedPersist interface. For such cases the method will throw an exception.
        
        The link will be broken and the linked object will become a normal embedded object.
        
        An entry with the specified name should be created or opened inside provided storage. This entry will be used for the object persistence. If the entry exists already all its contents will be ignored.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.embed.WrongStateException: ``WrongStateException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.uno.Exception: ``Exception``
        """
    def getLinkURL(self) -> str:
        """
        returns the URL of the link object.

        Raises:
            com.sun.star.embed.WrongStateException: ``WrongStateException``
            com.sun.star.uno.Exception: ``Exception``
        """
    def isLink(self) -> bool:
        """
        allows to detect whether the object is a linked one.
        
        Most of embedded objects will not support this interface, but some of them can do it, to allow conversion from link to object. After the conversion the object does not change, so interface set stays the same, but the object is not a link any more.

        Raises:
            com.sun.star.embed.WrongStateException: ``WrongStateException``
        """

__all__ = ['XLinkageSupport']

