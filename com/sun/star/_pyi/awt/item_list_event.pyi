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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.4
from typing_extensions import Literal
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class ItemListEvent(EventObject_a3d70b03):
    """
    Struct Class

    is the event broadcasted by a XListItems implementation for changes in its item list.

    See Also:
        `API ItemListEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1ItemListEvent.html>`_
    """
    typeName: Literal['com.sun.star.awt.ItemListEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., ItemPosition: typing.Optional[int] = ..., ItemText: typing.Optional[object] = ..., ItemImageURL: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            ItemPosition (int, optional): ItemPosition value.
            ItemText (object, optional): ItemText value.
            ItemImageURL (object, optional): ItemImageURL value.
        """
        ...


    @property
    def ItemPosition(self) -> int:
        """
        specifies the position of the item which is affected by the event
        
        In case the event is not related to a single item, but to the complete list, the value of this member is undefined.
        """
        ...

    @ItemPosition.setter
    def ItemPosition(self, value: int) -> None:
        ...

    @property
    def ItemText(self) -> object:
        """
        the text of the item.
        
        If the event being notified did not touch the text of an item, this member is empty. For instance, upon invocation of XItemList.setItemImage(), only ItemImageURL will be set, and ItemText will be empty.
        """
        ...

    @ItemText.setter
    def ItemText(self, value: object) -> None:
        ...

    @property
    def ItemImageURL(self) -> object:
        """
        the URL of the image of the item
        
        If the event being notified did not touch the image of an item, this member is empty. For instance, upon invocation of XItemList.setItemText(), only ItemText will be set, and ItemImageURL will be empty.
        """
        ...

    @ItemImageURL.setter
    def ItemImageURL(self, value: object) -> None:
        ...

