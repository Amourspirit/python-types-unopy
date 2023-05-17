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
# Namespace: com.sun.star.frame
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class WindowArrange(object):
    """
    Const

    these constants are used to specify a style of window arrangement

    See Also:
        `API WindowArrange <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1frame_1_1WindowArrange.html>`_
    """
    TILE: Literal[1]
    """
    arranges the windows in tiles
    """
    VERTICAL: Literal[2]
    """
    arranges the windows vertically
    """
    HORIZONTAL: Literal[3]
    """
    arranges the windows horizontally
    """
    CASCADE: Literal[4]
    """
    cascades the windows
    """
    MAXIMIZE: Literal[5]
    """
    maximizes all windows
    """
    MINIMIZE: Literal[6]
    """
    minimizes all windows
    """

