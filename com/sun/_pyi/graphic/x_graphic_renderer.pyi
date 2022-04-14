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
# Libre Office Version: 7.2
# Namespace: com.sun.star.graphic
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_graphic import XGraphic as XGraphic_a4da0afc

class XGraphicRenderer(XInterface_8f010a43):
    """
    This interfaces exposes just one method to render a XGraphic container.

    See Also:
        `API XGraphicRenderer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1graphic_1_1XGraphicRenderer.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.graphic.XGraphicRenderer']

    def render(self, Graphic: 'XGraphic_a4da0afc') -> None:
        """
        Renders the XGraphic container.
        """

__all__ = ['XGraphicRenderer']

