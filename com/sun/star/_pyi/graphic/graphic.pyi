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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.graphic
from .graphic_descriptor import GraphicDescriptor as GraphicDescriptor_1a520ec3
from .x_graphic import XGraphic as XGraphic_a4da0afc

class Graphic(GraphicDescriptor_1a520ec3, XGraphic_a4da0afc):
    """
    Service Class

    This service acts as a container for graphics.
    
    The main interface that has to be implemented for this service is the XGraphic interface, which itself exposes only a few methods. Beside this, a Graphic service incorporates the GraphicDescriptor to give access to the attributes of the graphic.

    See Also:
        `API Graphic <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1graphic_1_1Graphic.html>`_
    """
    ...


