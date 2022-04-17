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
# Libre Office Version: 7.3
# Namespace: com.sun.star.embed
from typing_extensions import Literal
"""
Const

The constant set contains possible modes to open an element.

The modes can be combined by \"or\" operation. ElementModes.READ and ElementModes.WRITE are base modes. A result mode must include one of base modes.

See Also:
    `API ElementModes <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1embed_1_1ElementModes.html>`_
"""
READ: Literal[1]
"""
specifies opening of an element for reading.
"""
SEEKABLE: Literal[2]
"""
specifies opening of a seekable element.

This mode is ignored for Storage elements. This flag makes sense only in combination with ElementModes.READ and/or ElementModes.WRITE.
"""
SEEKABLEREAD: Literal[3]
"""
specifies opening of a seekable element for reading.

This is just a combination of the previous two values. For storages it is the same as ElementModes.READ.
"""
WRITE: Literal[4]
"""
specifies opening of an element for writing.
"""
READWRITE: Literal[7]
"""
specifies opening of an element for reading and writing.

For a stream element is also specifies that it must be seekable.
"""
TRUNCATE: Literal[8]
"""
lets the document be truncated immediately after opening.

This flag makes sense only in combination with ElementModes.WRITE.
"""
NOCREATE: Literal[16]
"""
restricts creation of a new element on opening in case a requested one does not exist.

This flag makes sense only in combination with ElementModes.WRITE.
"""

