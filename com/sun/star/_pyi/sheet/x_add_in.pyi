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
# Namespace: com.sun.star.sheet
from typing_extensions import Literal
from ..lang.x_localizable import XLocalizable as XLocalizable_aee00b64

class XAddIn(XLocalizable_aee00b64):
    """
    gives access to function descriptions and user-visible names.

    See Also:
        `API XAddIn <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XAddIn.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XAddIn']

    def getArgumentDescription(self, aProgrammaticFunctionName: str, nArgument: int) -> str:
        """
        returns the description of the specified argument.
        
        The argument description is shown to the user when prompting for arguments. It may be translated to the current language of the AddIn.
        """
        ...
    def getDisplayArgumentName(self, aProgrammaticFunctionName: str, nArgument: int) -> str:
        """
        returns the user-visible name of the specified argument.
        
        The argument name is shown to the user when prompting for arguments. It should be a single word and may be translated to the current language of the AddIn.
        """
        ...
    def getDisplayCategoryName(self, aProgrammaticFunctionName: str) -> str:
        """
        returns the user-visible name of the category the function belongs to.
        
        This is used when category names are shown to the user.
        """
        ...
    def getDisplayFunctionName(self, aProgrammaticName: str) -> str:
        """
        returns the user-visible function name for an internal name.
        
        The user-visible name of a function is the name shown to the user. It may be translated to the current language of the AddIn, so it is never stored in files. It should be a single word and is used when entering or displaying formulas.
        """
        ...
    def getFunctionDescription(self, aProgrammaticName: str) -> str:
        """
        returns the description of a function.
        
        The description is shown to the user when selecting functions. It may be translated to the current language of the AddIn.
        """
        ...
    def getProgrammaticCategoryName(self, aProgrammaticFunctionName: str) -> str:
        """
        returns the programmatic name of the category the function belongs to.
        
        The category name is used to group similar functions together. The programmatic category name should always be in English, it is never shown to the user. It should be one of the following names if the function falls into the corresponding category.
        """
        ...
    def getProgrammaticFuntionName(self, aDisplayName: str) -> str:
        """
        returns the internal function name for an user-visible name.
        
        The user-visible name of a function is the name shown to the user. It may be translated to the current language of the AddIn, so it is never stored in files. It should be a single word and is used when entering or displaying formulas.
        
        Attention: The method name contains a spelling error. Due to compatibility reasons the name cannot be changed.
        """
        ...


