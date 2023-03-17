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
# Namespace: com.sun.star.awt
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .size import Size as Size_576707ef

class XLayoutConstrains(XInterface_8f010a43):
    """
    specifies the layout constraints for a surrounding container.

    See Also:
        `API XLayoutConstrains <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XLayoutConstrains.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XLayoutConstrains']

    def calcAdjustedSize(self, aNewSize: 'Size_576707ef') -> 'Size_576707ef':
        """
        calculates the adjusted size for a given maximum size.
        """
        ...
    def getMinimumSize(self) -> 'Size_576707ef':
        """
        returns the minimum size for this component.
        """
        ...
    def getPreferredSize(self) -> 'Size_576707ef':
        """
        returns the preferred size for this component.
        """
        ...


