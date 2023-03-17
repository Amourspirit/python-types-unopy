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
# Namespace: com.sun.star.util
from typing_extensions import Literal
from .x_modifiable import XModifiable as XModifiable_a4f60b0a

class XModifiable2(XModifiable_a4f60b0a):
    """
    allows to control modifiable state change.
    
    This interface allows to prevent changing of the modified state of the object. It is introduced for performance optimizations, to allow to prevent unnecessary updates, for example while importing a document. Please use this interface very carefully.

    See Also:
        `API XModifiable2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XModifiable2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.util.XModifiable2']

    def disableSetModified(self) -> bool:
        """
        disable possibility to change modified state of the document
        """
        ...
    def enableSetModified(self) -> bool:
        """
        enable possibility to change modified state of the document
        """
        ...
    def isSetModifiedEnabled(self) -> bool:
        """
        allows to detect whether the modified state change is enabled
        """
        ...


