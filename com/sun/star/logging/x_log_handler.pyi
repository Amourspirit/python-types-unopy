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

from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from .log_record import LogRecord as LogRecord_b0c20b70
    from .x_log_formatter import XLogFormatter as XLogFormatter_e23d0d1d


class XLogHandler(XComponent_98dc0ab5):
    """
    provides possibilities to send LogRecords to an arbitrary output channel.
    
    **since**
    
        OOo 2.3

    See Also:
        `API XLogHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1logging_1_1XLogHandler.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.logging.XLogHandler'

    def flush(self) -> None:
        """
        flushes all buffered output of the handler
        
        Log handlers are allowed to buffer their output. Upon flush being called, they must flush all their buffers.
        """
        ...
    def publish(self, Record: LogRecord_b0c20b70) -> bool:
        """
        publish the given log record at the handler's output channel.
        """
        ...

    @property
    def Encoding(self) -> str:
        """
        specifies MIME charset name for the encoding to be used by this handler
        
        It depends on the concrete handler implementation whether or not this parameter is needed.
        """
        ...
    @Encoding.setter
    def Encoding(self, value: str) -> None:
        ...
    @property
    def Formatter(self) -> XLogFormatter_e23d0d1d:
        """
        specifies the formatter to be used by this handler.
        """
        ...
    @Formatter.setter
    def Formatter(self, value: XLogFormatter_e23d0d1d) -> None:
        ...
    @property
    def Level(self) -> int:
        """
        specifies the log level of this handler
        
        Different handlers can have different log levels, which again might be different from the log level of the XLogger for which the handlers are used.
        """
        ...
    @Level.setter
    def Level(self, value: int) -> None:
        ...

