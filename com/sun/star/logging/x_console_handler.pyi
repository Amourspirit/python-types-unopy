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
# Namespace: com.sun.star.logging
from __future__ import annotations
import typing

from .x_log_handler import XLogHandler as XLogHandler_c7f80c27


class XConsoleHandler(XLogHandler_c7f80c27):
    """
    implemented by a log handler whose output channel is the processes console.
    
    Note that a console handler will ignore its formatter's head and tail, since it cannot decided whether they should be emitted on stdout or stderr.
    
    **since**
    
        OOo 2.3

    See Also:
        `API XConsoleHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1logging_1_1XConsoleHandler.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.logging.XConsoleHandler'

    @property
    def Threshold(self) -> int:
        """
        denotes the LogLevel threshold used to determine to which console the events should be logged.
        
        Events with a level greater or equal to Threshold will be logged to stderr, all others to stdout.
        
        The default value for this attribute is LogLevel.SEVERE.
        """
        ...
    @Threshold.setter
    def Threshold(self, value: int) -> None:
        ...

