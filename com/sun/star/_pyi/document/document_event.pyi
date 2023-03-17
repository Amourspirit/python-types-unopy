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
# Namespace: com.sun.star.document
# Libre Office Version: 7.4
from typing_extensions import Literal
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from ..frame.x_controller2 import XController2 as XController2_bbcf0bc1


class DocumentEvent(EventObject_a3d70b03):
    """
    Struct Class

    describes an event happening in an OfficeDocument
    
    The com.sun.star.lang.EventObject.Source member of the base type refers to the document which broadcasts the event.
    
    This type is the successor of the EventObject type, which should not be used anymore.
    
    **since**
    
        OOo 3.1

    See Also:
        `API DocumentEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1document_1_1DocumentEvent.html>`_
    """
    typeName: Literal['com.sun.star.document.DocumentEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., EventName: typing.Optional[str] = ..., ViewController: typing.Optional[XController2_bbcf0bc1] = ..., Supplement: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            EventName (str, optional): EventName value.
            ViewController (XController2, optional): ViewController value.
            Supplement (object, optional): Supplement value.
        """
        ...


    @property
    def EventName(self) -> str:
        """
        specifies the name of the event.
        
        It's the responsibility of the component supporting the XDocumentEventBroadcaster interface to specify which events it supports.
        """
        ...


    @property
    def ViewController(self) -> XController2_bbcf0bc1:
        """
        denotes the view respectively controller which the event applies to.
        
        Might be NULL if the event is not related to a concrete view of the document.
        """
        ...


    @property
    def Supplement(self) -> object:
        """
        contains supplemental information about the event which is being notified
        
        The semantics of this additional information needs to be specified by the broadcaster of the event.
        """
        ...


