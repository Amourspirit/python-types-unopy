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
# Namespace: com.sun.star.beans
# Libre Office Version: 7.2
from typing_extensions import Literal
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .property_state import PropertyState as PropertyState_c97b0c77


class PropertyStateChangeEvent(EventObject_a3d70b03):
    """
    Struct Class

    is delivered whenever the state of a \"bound\" property is changed.
    
    It is sent as an argument to the method of XPropertyStateChangeListener.
    
    Normally these events are accompanied by the name, and the old and new values of the changed property.
    
    Void values may be provided for the old and new values if their true values are not known.

    See Also:
        `API PropertyStateChangeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1PropertyStateChangeEvent.html>`_
    """
    typeName: Literal['com.sun.star.beans.PropertyStateChangeEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., PropertyName: typing.Optional[str] = ..., PropertyHandle: typing.Optional[int] = ..., OldValue: typing.Optional[PropertyState_c97b0c77] = ..., NewValue: typing.Optional[PropertyState_c97b0c77] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            PropertyName (str, optional): PropertyName value.
            PropertyHandle (int, optional): PropertyHandle value.
            OldValue (PropertyState, optional): OldValue value.
            NewValue (PropertyState, optional): NewValue value.
        """


    @property
    def PropertyName(self) -> str:
        """
        specifies the name of the property which changes its value.
        
        This name identifies the property uniquely within an XPropertySet. Upper and lower case are distinguished.
        """


    @property
    def PropertyHandle(self) -> int:
        """
        contains the implementation handle for the property.
        
        It may be -1 if the implementation has no handle. You can use this handle to get values from the XFastPropertySet interface.
        """


    @property
    def OldValue(self) -> PropertyState_c97b0c77:
        """
        contains the old value of the property.
        """


    @property
    def NewValue(self) -> PropertyState_c97b0c77:
        """
        contains the new value of the property.
        """



__all__ = ['PropertyStateChangeEvent']
