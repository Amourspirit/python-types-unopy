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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
import typing
from .filter_connection import FilterConnection as FilterConnection_f01f0d97


class TableFilterField2(object):
    """
    Struct Class

    describes a single condition in a filter descriptor.
    
    This struct has the FilterOperator2 constants group as member, whereas the TableFilterField struct uses the FilterOperator enum.
    
    **since**
    
        OOo 3.2

    See Also:
        `API TableFilterField2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1TableFilterField2.html>`_
    """
    typeName: str = 'com.sun.star.sheet.TableFilterField2'

    def __init__(self, Connection: typing.Optional[FilterConnection_f01f0d97] = ..., Field: typing.Optional[int] = ..., Operator: typing.Optional[int] = ..., IsNumeric: typing.Optional[bool] = ..., NumericValue: typing.Optional[float] = ..., StringValue: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Connection (FilterConnection, optional): Connection value.
            Field (int, optional): Field value.
            Operator (int, optional): Operator value.
            IsNumeric (bool, optional): IsNumeric value.
            NumericValue (float, optional): NumericValue value.
            StringValue (str, optional): StringValue value.
        """
        ...

    @property
    def Connection(self) -> FilterConnection_f01f0d97:
        """
        specifies how the condition is connected to the previous condition.
        """
        ...
    @Connection.setter
    def Connection(self, value: FilterConnection_f01f0d97) -> None:
        ...
    @property
    def Field(self) -> int:
        """
        specifies which field (column) is used for the condition.
        """
        ...
    @Field.setter
    def Field(self, value: int) -> None:
        ...
    @property
    def Operator(self) -> int:
        """
        specifies the type of the condition as defined in FilterOperator2.
        """
        ...
    @Operator.setter
    def Operator(self, value: int) -> None:
        ...
    @property
    def IsNumeric(self) -> bool:
        """
        selects whether the TableFilterField2.NumericValue or the TableFilterField2.StringValue is used.
        """
        ...
    @IsNumeric.setter
    def IsNumeric(self, value: bool) -> None:
        ...
    @property
    def NumericValue(self) -> float:
        """
        specifies a numeric value for the condition.
        """
        ...
    @NumericValue.setter
    def NumericValue(self, value: float) -> None:
        ...
    @property
    def StringValue(self) -> str:
        """
        specifies a string value for the condition.
        """
        ...
    @StringValue.setter
    def StringValue(self, value: str) -> None:
        ...
