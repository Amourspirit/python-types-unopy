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
# Namespace: com.sun.star.frame
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class XLoadable(XInterface_8f010a43):
    """
    offers a simple way to initialize a component or load it from a URL.
    
    In case an object supports the interface the object must be initialized with either initNew() or load() call before any usage. In case the object is already initialized the mentioned methods should throw DoubleInitializationException.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XLoadable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XLoadable.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.frame.XLoadable']

    def initNew(self) -> None:
        """
        creates a component from scratch

        Raises:
            DoubleInitializationException: ``DoubleInitializationException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.uno.Exception: ``Exception``
        """
    def load(self, lArguments: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        loads a component from a URL

        Raises:
            DoubleInitializationException: ``DoubleInitializationException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.uno.Exception: ``Exception``
        """

__all__ = ['XLoadable']

