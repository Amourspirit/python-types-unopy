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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
import typing


class ImageStatus:
    """
    Const

    These values are used to specify to which degree an image is available.

    See Also:
        `API ImageStatus <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1ImageStatus.html>`_
    """
    IMAGESTATUS_ERROR: int = ...
    """
    This conveys that an error was encountered while producing the image.
    """
    IMAGESTATUS_SINGLEFRAMEDONE: int = ...
    """
    This conveys that one frame of the image is complete but there are more frames to be delivered.
    """
    IMAGESTATUS_STATICIMAGEDONE: int = ...
    """
    This conveys that the image is complete and there are no more pixels or frames to be delivered.
    """
    IMAGESTATUS_ABORTED: int = ...
    """
    This conveys that the image creation process was deliberately aborted.
    """

