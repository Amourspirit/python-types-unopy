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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.embed
from typing_extensions import Literal


class EmbedUpdateModes(object):
    """
    Const

    The constant set specifies possible modes of object update.

    See Also:
        `API EmbedUpdateModes <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1embed_1_1EmbedUpdateModes.html>`_
    """
    ALWAYS_UPDATE: Literal[0]
    """
    An object representation should be updated as often as possible.
    
    Any time object detects that it is changed the representation of the object is updated.
    """
    EXPLICIT_UPDATE: Literal[1]
    """
    An object representation should be updated only in case of request.
    
    The representation of the object is updated only by explicit request.
    """

