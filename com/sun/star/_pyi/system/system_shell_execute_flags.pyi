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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.system
from typing_extensions import Literal
"""
Const

Different settings for the SystemShellExecute service.

**since**

    LibreOffice 3.6

See Also:
    `API SystemShellExecuteFlags <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1system_1_1SystemShellExecuteFlags.html>`_
"""
DEFAULTS: Literal[0]
"""
Uses the default settings for executing commands.
"""
NO_SYSTEM_ERROR_MESSAGE: Literal[1]
"""
Prevents the display of system error message boxes if the method com.sun.star.system.XSystemShellExecute.execute() fails.
"""
URIS_ONLY: Literal[2]
"""
Only allows opening of absolute URI references.

**since**

    LibreOffice 3.6
"""

