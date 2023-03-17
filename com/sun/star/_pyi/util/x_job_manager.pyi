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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.util
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_cancellable import XCancellable as XCancellable_afc30b64

class XJobManager(XInterface_8f010a43):
    """
    Manage cancelable jobs.

    See Also:
        `API XJobManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XJobManager.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.util.XJobManager']

    def cancelAllJobs(self) -> None:
        """
        cancel all registered jobs.
        """
        ...
    def registerJob(self, Job: 'XCancellable_afc30b64') -> None:
        """
        registers a cancelable job.
        """
        ...
    def releaseJob(self, Job: 'XCancellable_afc30b64') -> None:
        """
        deregisters a cancelable jobs.
        """
        ...


