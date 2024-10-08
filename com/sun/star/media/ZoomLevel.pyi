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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.media
# Libre Office Version: 2024.2
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class ZoomLevelProto(Protocol):
    """Protocol for ZoomLevel"""

    @property
    def typeName(self) -> Literal["com.sun.star.media.ZoomLevel"]:
        ...
    value: Any
    FIT_TO_WINDOW: ZoomLevelProto
    FIT_TO_WINDOW_FIXED_ASPECT: ZoomLevelProto
    FULLSCREEN: ZoomLevelProto
    NOT_AVAILABLE: ZoomLevelProto
    ORIGINAL: ZoomLevelProto
    ZOOM_1_TO_2: ZoomLevelProto
    ZOOM_1_TO_4: ZoomLevelProto
    ZOOM_2_TO_1: ZoomLevelProto
    ZOOM_4_TO_1: ZoomLevelProto

FIT_TO_WINDOW: ZoomLevelProto
"""
specifies that the video should be zoomed to window size
"""
FIT_TO_WINDOW_FIXED_ASPECT: ZoomLevelProto
"""
specifies that the video should be zoomed to window size with using a fixed aspect ratio
"""
FULLSCREEN: ZoomLevelProto
"""
specifies that the video should be displayed in fullscreen mode, if available
"""
NOT_AVAILABLE: ZoomLevelProto
"""
specifies that the video window itself is not available at all, e.g.

in cases of pure audio playback
"""
ORIGINAL: ZoomLevelProto
"""
specifies that the video should be displayed with its original size
"""
ZOOM_1_TO_2: ZoomLevelProto
"""
specifies that the video should be zoomed to a factor of 1:2
"""
ZOOM_1_TO_4: ZoomLevelProto
"""
specifies that the video should be zoomed to a factor of 1:4
"""
ZOOM_2_TO_1: ZoomLevelProto
"""
specifies that the video should be zoomed to a factor of 2:1
"""
ZOOM_4_TO_1: ZoomLevelProto
"""
specifies that the video should be zoomed to a factor of 4:1
"""

