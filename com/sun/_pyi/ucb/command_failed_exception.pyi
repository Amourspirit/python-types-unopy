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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from typing_extensions import Literal
from ooo.oenv.env_const import UNO_NONE
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class CommandFailedException(Exception_85530a09):
    """
    Exception Class

    This exception is thrown if an exception situation occurred during the processing of a command and an com.sun.star.task.XInteractionHandler was able to handle the request for the error condition and the requesting code decided to abort the command execution according to the selection made by the interaction handler.

    See Also:
        `API CommandFailedException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1CommandFailedException.html>`_
    """

    typeName: Literal['com.sun.star.ucb.CommandFailedException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., Reason: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Reason (object, optional): Reason value.
        """
    @property
    def Reason(self) -> object:
        """
        contains the exception that was passed to the com.sun.star.task.XInteractionHandler.
        """


__all__ = ['CommandFailedException']

