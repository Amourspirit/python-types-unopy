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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.util
import typing


class Endianness:
    """
    Const

    These constants describe the endianness of data structures.
    
    The endianness specifies the order in which the bytes of larger types are laid out in memory.
    
    **since**
    
        OOo 2.0

    See Also:
        `API Endianness <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1util_1_1Endianness.html>`_
    """
    LITTLE: int = ...
    """
    Little endian.
    
    The values are stored in little endian format, i.e. the bytes of the long word 0xAABBCCDD are laid out like 0xDD, 0xCC, 0xBB, 0xAA in memory. That is, data of arbitrary machine word lengths always starts with the least significant byte, and ends with the most significant one.
    """
    BIG: int = ...
    """
    Big endian.
    
    The values are stored in big endian format, i.e. the bytes of the long word 0xAABBCCDD are laid out like 0xAA, 0xBB, 0xCC, 0xDD in memory. That is, data of arbitrary machine word lengths always start with the most significant byte, and ends with the least significant one.
    """

