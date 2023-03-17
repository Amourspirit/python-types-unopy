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
# Libre Office Version: 7.4
# Namespace: com.sun.star.accessibility
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.key_stroke import KeyStroke as KeyStroke_84cb09f5

class XAccessibleKeyBinding(XInterface_8f010a43):
    """
    This interface can be used to represent any number of key bindings which then can be associated to a certain action.
    
    There can be zero, one, or more key bindings. Each key binding consists of a sequence of com.sun.star.awt.KeyStroke objects. The association of an action with a key binding is established by the XAccessibleAction interface returning an XAccessibleKeyBinding object.
    
    A key binding describes alternative ways how to invoke an action with pressing one or more keys after each other. Each individual sequence of key strokes
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessibleKeyBinding <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleKeyBinding.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.accessibility.XAccessibleKeyBinding']

    def getAccessibleKeyBinding(self, nIndex: int) -> 'typing.Tuple[KeyStroke_84cb09f5, ...]':
        """
        The returned sequence of key strokes describes one method to invoke the associated action (the one from which you obtained the object at which you called this method) by pressing keys.
        
        The keys specified by each of the returned key strokes have to be pressed at the same time (the Control-key and the A-key for example). The keys of one key stroke have to be released before pressing those of the next. The order of the key strokes in the sequence define the order in which to press them.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def getAccessibleKeyBindingCount(self) -> int:
        """
        Return the number of available key bindings.
        """
        ...


