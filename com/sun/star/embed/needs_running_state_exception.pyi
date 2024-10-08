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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.embed
# Libre Office Version: 2024.2
from typing_extensions import Literal
import typing
from .wrong_state_exception import WrongStateException as WrongStateException_19f60ec2
from ..uno.x_interface import XInterface as XInterface_8f010a43

class NeedsRunningStateException(WrongStateException_19f60ec2):
    """
    Exception Class

    This exception can be thrown in case a list of accepted verbs of states is requested and the object is in loaded state and this information can be retrieved only when the object is in running state.
    
    This exception means that the object supports at least running state in addition to the loaded state. Other states and possible verbs can be detected only after object is switched to running state.

    See Also:
        `API NeedsRunningStateException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1embed_1_1NeedsRunningStateException.html>`_
    """

    typeName: Literal['com.sun.star.embed.NeedsRunningStateException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
        """
        ...

__all__ = ['NeedsRunningStateException']

