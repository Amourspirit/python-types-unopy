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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_font_mapping_use_item import XFontMappingUseItem as XFontMappingUseItem_fc0a0dcb

class XFontMappingUse(XInterface_8f010a43):
    """
    This interface extends the XToolkit interface with support for tracking how requested fonts are mapped to actual fonts when laying out text.
    
    **since**
    
        LibreOffice 7.3

    See Also:
        `API XFontMappingUse <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XFontMappingUse.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XFontMappingUse']

    def finishTrackingFontMappingUse(self) -> 'typing.Tuple[XFontMappingUseItem_fc0a0dcb, ...]':
        """
        Stop tracking of how requested fonts are mapped to available fonts and return the mappings that took place since the call to startTrackingFontMappingUse().
        """
        ...
    def startTrackingFontMappingUse(self) -> None:
        """
        Activate tracking of how requested fonts are mapped to available fonts.
        """
        ...


