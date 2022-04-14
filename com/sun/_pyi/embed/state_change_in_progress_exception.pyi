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
# Namespace: com.sun.star.embed
# Libre Office Version: 7.2
from typing_extensions import Literal
from ooo.oenv.env_const import UNO_NONE
import typing
from .wrong_state_exception import WrongStateException as WrongStateException_19f60ec2
from ..uno.x_interface import XInterface as XInterface_8f010a43

class StateChangeInProgressException(WrongStateException_19f60ec2):
    """
    Exception Class

    This exception can be thrown in case the object does not allow to call requested functionality currently because the object is changing state.

    See Also:
        `API StateChangeInProgressException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1embed_1_1StateChangeInProgressException.html>`_
    """

    typeName: Literal['com.sun.star.embed.StateChangeInProgressException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., TargetState: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            TargetState (int, optional): TargetState value.
        """
    @property
    def TargetState(self) -> int:
        """
        contains the target state the object tries to reach currently.
        
        Contains a value from EmbedStates constant set.
        """


__all__ = ['StateChangeInProgressException']

