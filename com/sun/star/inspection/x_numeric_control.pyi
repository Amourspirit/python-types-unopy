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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.inspection
from __future__ import annotations
import typing

from .x_property_control import XPropertyControl as XPropertyControl_3f260fe2


class XNumericControl(XPropertyControl_3f260fe2):
    """
    defines the interface for an XPropertyControl which supports displaying and entering numerical values.
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API XNumericControl <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1inspection_1_1XNumericControl.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.inspection.XNumericControl'

    @property
    def DecimalDigits(self) -> int:
        """
        describes the number of decimal digits to use for the value
        """
        ...
    @DecimalDigits.setter
    def DecimalDigits(self, value: int) -> None:
        ...
    @property
    def DisplayUnit(self) -> int:
        """
        describes a com.sun.star.util.MeasureUnit to be applied for displaying values.
        
        Only a certain set of com.sun.star.util.MeasureUnit values is supported. In particular, every value which denotes a fraction of another unit (like 100th millimeters) cannot be used as DisplayUnit.
        """
        ...
    @DisplayUnit.setter
    def DisplayUnit(self, value: int) -> None:
        ...
    @property
    def MaxValue(self) -> object:
        """
        describes the maximum value which is allowed to be entered in the control
        """
        ...
    @MaxValue.setter
    def MaxValue(self, value: object) -> None:
        ...
    @property
    def MinValue(self) -> object:
        """
        describes the minimum value which is allowed to be entered in the control
        """
        ...
    @MinValue.setter
    def MinValue(self, value: object) -> None:
        ...
    @property
    def ValueUnit(self) -> int:
        """
        describes a com.sun.star.util.MeasureUnit to be applied for transferring values.
        
        The core measurement unit for a property value might differ from the unit which is used by the control to display it. For instance, your property value might require that your values denote 100th millimeters, but to the user, you want to present the value as, say, inches. In this case, a numeric control can automatically handle the value conversion for you, if you give it a ValueUnit different from the DisplayUnit.
        """
        ...
    @ValueUnit.setter
    def ValueUnit(self, value: int) -> None:
        ...

