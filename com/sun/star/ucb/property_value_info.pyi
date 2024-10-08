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
# Namespace: com.sun.star.ucb
# Libre Office Version: 2024.2
from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
from ..beans.property_state import PropertyState as PropertyState_c97b0c77
import typing
from .property_value_state import PropertyValueState as PropertyValueState_f1050da5


class PropertyValueInfo(PropertyValue_c9610c73):
    """
    Struct Class

    contains value and state of a com.sun.star.beans.Property.

    See Also:
        `API PropertyValueInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1PropertyValueInfo.html>`_
    """
    typeName: str = 'com.sun.star.ucb.PropertyValueInfo'

    def __init__(self, Name: typing.Optional[str] = ..., Handle: typing.Optional[int] = ..., Value: typing.Optional[object] = ..., State: typing.Optional[PropertyState_c97b0c77] = ..., ValueState: typing.Optional[PropertyValueState_f1050da5] = ...) -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Handle (int, optional): Handle value.
            Value (object, optional): Value value.
            State (PropertyState, optional): State value.
            ValueState (PropertyValueState, optional): ValueState value.
        """
        ...

    @property
    def ValueState(self) -> PropertyValueState_f1050da5:
        """
        the state of the property value.
        """
        ...
    @ValueState.setter
    def ValueState(self, value: PropertyValueState_f1050da5) -> None:
        ...

