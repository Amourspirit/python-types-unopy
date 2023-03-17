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
# Namespace: com.sun.star.sheet
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .localized_name import LocalizedName as LocalizedName_c89d0c39

class XCompatibilityNames(XInterface_8f010a43):
    """
    gives access to the sequence of compatibility names for an Addin function.

    See Also:
        `API XCompatibilityNames <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XCompatibilityNames.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XCompatibilityNames']

    def getCompatibilityNames(self, aProgrammaticName: str) -> 'typing.Tuple[LocalizedName_c89d0c39, ...]':
        """
        returns the compatibility names of the specified function.
        
        Compatibility names are localized names of AddIn functions that are used to import files from other applications.
        
        If on import a localized function name is read, this list of compatibility names is used to find the internal name of the function. The current locale may differ from the locale used in the imported file, so the method XAddIn.getProgrammaticFuntionName() cannot be used here.
        
        The order inside the sequence of compatibility names is used to prioritize the names. Initially the first compatibility name of each function is compared to the imported name (each function may provide a sequence of compatibility names - the first entry of all sequences is used). If no entry is equal, the second entry of each sequence is used and so on.
        
        If a locale is not present in the sequence of compatibility names, the first entry of the sequence is used. So the method should return a sequence which contains first the entry representing the current locale.TRUE
        """
        ...


