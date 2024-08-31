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
# Namespace: com.sun.star.script
# Libre Office Version: 2024.2
import typing


class ArrayWrapper(object):
    """
    Struct Class

    Allows a UNO sequence that is passed between different language boundaries to indicate it prefers to be represented as a multidimensional array with 0 or 1 based indices.
    
    UNO does not natively represent Multi-Dimensional arrays, instead a sequence can have elements that are themselves sequences (an array of arrays ).
    
    Some languages ( example BASIC ) can natively represent both Multi-Dimensional arrays and array of arrays. Those languages could represent a sequence of sequences as either a Multi-Dimensional array or array of arrays. This structure allows a preference for a Multi-Dimensional array representation to be specified.

    See Also:
        `API ArrayWrapper <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1ArrayWrapper.html>`_
    """
    typeName: str = 'com.sun.star.script.ArrayWrapper'

    def __init__(self, IsZeroIndex: typing.Optional[bool] = ..., Array: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            IsZeroIndex (bool, optional): IsZeroIndex value.
            Array (object, optional): Array value.
        """
        ...

    @property
    def IsZeroIndex(self) -> bool:
        """
        Indicates whether the Array should be have 1 or 0 based indexing.
        """
        ...
    @IsZeroIndex.setter
    def IsZeroIndex(self, value: bool) -> None:
        ...
    @property
    def Array(self) -> object:
        """
        Contains the Array to be passed.
        
        Multi-dimensional arrays can only be represented as a sequence where the elements of the sequence are themselves sequences. N-Levels of indirection are possible, where N is the number of dimensions. Note: its perfectly legal to use this structure with a single dimensioned array just to indicate the array indexing.
        """
        ...
    @Array.setter
    def Array(self, value: object) -> None:
        ...

