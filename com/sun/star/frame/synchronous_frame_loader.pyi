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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.frame
from __future__ import annotations
from ..container.x_named import XNamed as XNamed_a6520b08
from .x_synchronous_frame_loader import XSynchronousFrameLoader as XSynchronousFrameLoader_5a8d1058
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca

class SynchronousFrameLoader(XNamed_a6520b08, XSynchronousFrameLoader_5a8d1058, XInitialization_d46c0cca):
    """
    Service Class

    derivations of this abstract service are used to load components into Frames of the environment
    
    Concrete implementations of this service register, for example, for file name extensions or MIME types to load appropriate components. The components loaded are at least Controller. Instead of service FrameLoader this one use synchronous processes to load the component.

    See Also:
        `API SynchronousFrameLoader <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1SynchronousFrameLoader.html>`_
    """
    ...

