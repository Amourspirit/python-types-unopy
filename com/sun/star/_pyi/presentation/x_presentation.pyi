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
# Libre Office Version: 7.3
# Namespace: com.sun.star.presentation
from typing_extensions import Literal
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XPresentation(XInterface_8f010a43):
    """
    With this interface you can control any object that implements a Presentation.

    See Also:
        `API XPresentation <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1presentation_1_1XPresentation.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.presentation.XPresentation']

    def end(self) -> None:
        """
        The presentation is stopped and the full-screen mode will end.
        """
        ...
    def rehearseTimings(self) -> None:
        """
        Starts the presentation from the beginning and shows the actual running time to the user.
        """
        ...
    def start(self) -> None:
        """
        The presentation is shown in full-screen and started from the beginning.
        """
        ...


