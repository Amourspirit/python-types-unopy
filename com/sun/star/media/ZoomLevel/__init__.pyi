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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.media
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from com.sun.star._pyi.media.zoom_level import ZoomLevel as PyiZoomLevel
"""
Enum

ENUM ZoomLevel

See Also:
    `API ZoomLevel <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1media.html#aa2569917c2883c1d1c0c0ee02e671ac6>`_
"""
typeName: str = 'com.sun.star.media.ZoomLevel'

FIT_TO_WINDOW: PyiZoomLevel = ...
"""
specifies that the video should be zoomed to window size
"""
FIT_TO_WINDOW_FIXED_ASPECT: PyiZoomLevel = ...
"""
specifies that the video should be zoomed to window size with using a fixed aspect ratio
"""
FULLSCREEN: PyiZoomLevel = ...
"""
specifies that the video should be displayed in fullscreen mode, if available
"""
NOT_AVAILABLE: PyiZoomLevel = ...
"""
specifies that the video window itself is not available at all, e.g.

in cases of pure audio playback
"""
ORIGINAL: PyiZoomLevel = ...
"""
specifies that the video should be displayed with its original size
"""
ZOOM_1_TO_2: PyiZoomLevel = ...
"""
specifies that the video should be zoomed to a factor of 1:2
"""
ZOOM_1_TO_4: PyiZoomLevel = ...
"""
specifies that the video should be zoomed to a factor of 1:4
"""
ZOOM_2_TO_1: PyiZoomLevel = ...
"""
specifies that the video should be zoomed to a factor of 2:1
"""
ZOOM_4_TO_1: PyiZoomLevel = ...
"""
specifies that the video should be zoomed to a factor of 4:1
"""

