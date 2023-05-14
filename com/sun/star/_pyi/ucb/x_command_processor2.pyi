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
# Namespace: com.sun.star.ucb
from typing_extensions import Literal
from .x_command_processor import XCommandProcessor as XCommandProcessor_dfe80d19

class XCommandProcessor2(XCommandProcessor_dfe80d19):
    """
    An improved version of a com.sun.star.ucb.XCommandProcessor that helps avoid ever-increasing resource consumption.

    See Also:
        `API XCommandProcessor2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XCommandProcessor2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ucb.XCommandProcessor2']

    def releaseCommandIdentifier(self, CommandId: int) -> None:
        """
        releases a command identifier obtained through XCommandProcessor.createCommandIdentifier() when it is no longer used.
        
        After this call the command identifier cannot be used any longer in calls to XCommandProcessor.execute() and XCommandProcessor.abort(). (But it can happen that a call to XCommandProcessor.createCommandIdentifier() reuses this identifier.)
        """
        ...


