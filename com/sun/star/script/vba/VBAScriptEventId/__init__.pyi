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
# Namespace: com.sun.star.script.vba
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
"""
Const

Identifies a VBA script event fired via XVBACompatibility.broadcastVBAScriptEvent(), and received by XVBAScriptListener.notifyVBAScriptEvent().

See Also:
    `API VBAScriptEventId <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1script_1_1vba_1_1VBAScriptEventId.html>`_
"""
SCRIPT_STARTED: Literal[0]
"""
This event is fired when a VBA script in the current document has been started.

Several scripts may run simultaneously, e.g. when a running script triggers a document event that starts another script.

The number of running scripts can be obtained via XVBACompatibility.RunningVBAScripts. The number returned there will already contain the new script notified with this event.

The member VBAScriptEvent.ModuleName of the event object will contain the name of the code module that contains the started script.
"""
SCRIPT_STOPPED: Literal[1]
"""
This event is fired when a VBA script in the current document stops running.

Several scripts may run simultaneously, e.g. when a running script triggers a document event that starts another script.

The number of scripts still running can be obtained via XVBACompatibility.RunningVBAScripts. The number returned there will not contain the stopped script notified with this event anymore.

The member VBAScriptEvent.ModuleName of the event object will contain the name of the code module that contains the script that has been stopped.
"""
INITIALIZE_USERFORM: Literal[2]
"""
This event is fired when a VBA script in the current document tries to instantiate a userform.

The member VBAScriptEvent.ModuleName of the event object will contain the name of the userform module.
"""

