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
# Singleton Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.util
# Libre Office Version: 2024.2
from .x_macro_expander import XMacroExpander as XMacroExpander_c8360c47


class theMacroExpander(XMacroExpander_c8360c47):
    """
    Singleton Class

    A service that has to deal with macrofied strings will preprocess those strings using the macro expander singleton.
    
    The macro expander singleton is deployed with the application.
    
    This feature is currently used macrofying loader urls with macros defined in uno.ini/unorc bootstrap files. The component loader uses the macro expander singleton to expand those macros. This is a flexible way preprocessing loader urls.

    See Also:
        `API theMacroExpander <https://api.libreoffice.org/docs/idl/ref/singletoncom_1_1sun_1_1star_1_1util_1_1theMacroExpander.html>`_
    """
    ...


