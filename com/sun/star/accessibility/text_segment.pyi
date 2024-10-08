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
# Namespace: com.sun.star.accessibility
# Libre Office Version: 2024.2
import typing


class TextSegment(object):
    """
    Struct Class

    This structure describes a text segment that is embedded in a larger portion of text.
    
    It is used for example by the XAccessibleText interface to describe a text portion that was inserted into or deleted from an accessible text.
    
    The indices TextSegment.SegmentStart and TextSegment.SegmentEnd refer to the enclosing text. The TextSegment.SegmentText member contains the text between these two indices including the start index but not the end index. With it you can use this structure without having to access the XAccessibleText interface that represents the enclosing text.
    
    An empty text segment is expressed by TextSegment.SegmentStart and TextSegment.SegmentEnd set to the same value. While a value of -1 signals an error (like the request for a word after the last character of a text) all other values define the empty string at that position.
    
    The SegmentText member is a copy of the corresponding text segment of the enclosing text. Modifying this structure does not alter the enclosing text.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API TextSegment <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1accessibility_1_1TextSegment.html>`_
    """
    typeName: str = 'com.sun.star.accessibility.TextSegment'

    def __init__(self, SegmentText: typing.Optional[str] = ..., SegmentStart: typing.Optional[int] = ..., SegmentEnd: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            SegmentText (str, optional): SegmentText value.
            SegmentStart (int, optional): SegmentStart value.
            SegmentEnd (int, optional): SegmentEnd value.
        """
        ...

    @property
    def SegmentText(self) -> str:
        """
        A copy of the text segment of the enclosing text delimited by the text indices TextSegment.SegmentStart and TextSegment.SegmentEnd.
        
        Modifying it does not alter the enclosing text.
        """
        ...
    @SegmentText.setter
    def SegmentText(self, value: str) -> None:
        ...
    @property
    def SegmentStart(self) -> int:
        """
        Index of the first character of the text segment represented by this structure.
        
        The index refers to the enclosing text.
        """
        ...
    @SegmentStart.setter
    def SegmentStart(self, value: int) -> None:
        ...
    @property
    def SegmentEnd(self) -> int:
        """
        Index of the character directly behind the last character of the text segment represented by this structure.
        
        The index refers to the enclosing text.
        """
        ...
    @SegmentEnd.setter
    def SegmentEnd(self, value: int) -> None:
        ...

