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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.system
from typing_extensions import Literal
"""
Const

These constants are used to specify how the SimpleMailClient Service should behave.

See Also:
    `API SimpleMailClientFlags <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1system_1_1SimpleMailClientFlags.html>`_
"""
DEFAULTS: Literal[0]
"""
Uses the default settings when sending a mail, e.g.

launches the current configured system mail client.
"""
NO_USER_INTERFACE: Literal[1]
"""
Does not show the current configured system mail client, but sends the mail without any further user interaction.

If this flag is specified, a recipient address must have been specified for the given XSimpleMailMessage object given to the method com.sun.star.system.XSimpleMailClient.sendSimpleMailMessage().
"""
NO_LOGON_DIALOG: Literal[2]
"""
No logon dialog should be displayed to prompt the user for logon information if necessary.

When this flag is specified and the user needs to logon in order to send a simple mail message via the method com.sun.star.system.XSimpleMailClient.sendSimpleMailMessage(), an Exception will be thrown.
"""

