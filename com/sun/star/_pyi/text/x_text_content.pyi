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
# Libre Office Version: 7.2
# Namespace: com.sun.star.text
from typing_extensions import Literal
import typing
from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from .x_text_range import XTextRange as XTextRange_9a910ab7

class XTextContent(XComponent_98dc0ab5):
    """
    enables objects to be inserted into a text and to provide their location in a text once they are inserted into it.

    See Also:
        `API XTextContent <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XTextContent.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.text.XTextContent']

    def attach(self, xTextRange: 'XTextRange_9a910ab7') -> None:
        """
        is called when this object gets embedded in a text.
        
        This acts like a multi-phase construction, thus the object may be invalid until it is attached to a text position. Usually this method is called from within XText.insertTextContent().
        
        Both text objects and text content objects may only be connected to each other if they are created by the same component. When implementing new components, this behavior is deprecated.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getAnchor(self) -> 'XTextRange_9a910ab7':
        """
        Note: The anchor of the actual implementation for text tables does not have a position in the text. Thus that anchor can not be used for some operation like attach() for example or com.sun.star.text.insertTextContent or other function that require the object to have a position in the text.
        
        The reason why a text table still needs an anchor is that for example tables should be insertable via com.sun.star.text.insertTextContent and that interface uses a parameter of that type.
        """
        ...


