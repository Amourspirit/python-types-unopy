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
# Libre Office Version: 7.3
# Namespace: com.sun.star.text
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_flat_paragraph import XFlatParagraph as XFlatParagraph_c8310c42

class XFlatParagraphIterator(XInterface_8f010a43):
    """
    provides functionality to ...
    
    **since**
    
        OOo 3.0

    See Also:
        `API XFlatParagraphIterator <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XFlatParagraphIterator.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.text.XFlatParagraphIterator']

    def getFirstPara(self) -> 'XFlatParagraph_c8310c42':
        """
        get the first flat paragraph to be checked or an empty reference if there are no more paragraphs to check.
        """
        ...
    def getLastPara(self) -> 'XFlatParagraph_c8310c42':
        """
        get the last flat paragraph
        """
        ...
    def getNextPara(self) -> 'XFlatParagraph_c8310c42':
        """
        get the next flat paragraph to be checked or an empty reference if there are no more paragraphs to check.
        """
        ...
    def getParaAfter(self, xPara: 'XFlatParagraph_c8310c42') -> 'XFlatParagraph_c8310c42':
        """
        get the flat paragraph just following this one

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getParaBefore(self, xPara: 'XFlatParagraph_c8310c42') -> 'XFlatParagraph_c8310c42':
        """
        get the flat paragraph before this one

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...


