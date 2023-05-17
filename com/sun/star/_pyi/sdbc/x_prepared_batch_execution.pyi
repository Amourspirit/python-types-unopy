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
# Namespace: com.sun.star.sdbc
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

import uno
from ..uno.x_interface import XInterface as XInterface_8f010a43


class XPreparedBatchExecution(XInterface_8f010a43):
    """
    is used for batch execution on PreparedStatements.
    
    A com.sun.star.sdbc.PreparedStatement uses one precompiled SQL Statement. In batch execution it is possible to set collection of parameter settings, which are executed in one batch job.

    See Also:
        `API XPreparedBatchExecution <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XPreparedBatchExecution.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sdbc.XPreparedBatchExecution']

    def addBatch(self) -> None:
        """
        adds a set of parameters to the batch.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def clearBatch(self) -> None:
        """
        makes the set of commands in the current batch empty.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def executeBatch(self) -> uno.ByteSequence:
        """
        submits a batch of commands to the database for execution.

        Raises:
            SQLException: ``SQLException``
        """
        ...


