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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
"""
Enum



See Also:
    `API IOErrorCode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#ab0378c2985abaca86838ed9936c3a2d5>`_
"""
typeName: str = 'com.sun.star.ucb.IOErrorCode'

ABORT: 'uno.Enum'
"""
An operation was aborted.
"""
ACCESS_DENIED: 'uno.Enum'
"""
An object cannot be accessed due to insufficient user rights.
"""
ALREADY_EXISTING: 'uno.Enum'
"""
An object already exists.
"""
BAD_CRC: 'uno.Enum'
"""
A bad checksum.
"""
CANT_CREATE: 'uno.Enum'
"""
An object could not be created.
"""
CANT_READ: 'uno.Enum'
"""
Data could not be read from a file.
"""
CANT_SEEK: 'uno.Enum'
"""
A seek operation could not be run.
"""
CANT_TELL: 'uno.Enum'
"""
A tell operation could not be run.
"""
CANT_WRITE: 'uno.Enum'
"""
Data could not be written to a file.
"""
CURRENT_DIRECTORY: 'uno.Enum'
"""
A function is not possible because the path contains the current directory.
"""
DEVICE_NOT_READY: 'uno.Enum'
"""
A device (drive) not ready.
"""
DIFFERENT_DEVICES: 'uno.Enum'
"""
A function is not possible because the devices (drives) are not identical.
"""
GENERAL: 'uno.Enum'
"""
A general input/output error.
"""
INVALID_ACCESS: 'uno.Enum'
"""
An invalid attempt was made to access an object.
"""
INVALID_CHARACTER: 'uno.Enum'
"""
A file name contains invalid characters.
"""
INVALID_DEVICE: 'uno.Enum'
"""
A specified device is invalid.
"""
INVALID_LENGTH: 'uno.Enum'
"""
Invalid data length.
"""
INVALID_PARAMETER: 'uno.Enum'
"""
An operation was started with an invalid parameter.
"""
IS_WILDCARD: 'uno.Enum'
"""
An operation cannot be run on file names containing wildcards.
"""
LOCKING_VIOLATION: 'uno.Enum'
"""
A locking problem.
"""
MISPLACED_CHARACTER: 'uno.Enum'
"""
An invalid file name.
"""
NAME_TOO_LONG: 'uno.Enum'
"""
A file name is too long.
"""
NOT_EXISTING: 'uno.Enum'
"""
A nonexistent object.
"""
NOT_EXISTING_PATH: 'uno.Enum'
"""
The path to a file does not exist.
"""
NOT_SUPPORTED: 'uno.Enum'
"""
An action is not supported.
"""
NO_DIRECTORY: 'uno.Enum'
"""
An object is not a directory.
"""
NO_FILE: 'uno.Enum'
"""
An object is not a file.
"""
OUT_OF_DISK_SPACE: 'uno.Enum'
"""
No more space on a device.
"""
OUT_OF_FILE_HANDLES: 'uno.Enum'
"""
No more file handles available.
"""
OUT_OF_MEMORY: 'uno.Enum'
"""
An operation could not be run due to insufficient memory.
"""
PENDING: 'uno.Enum'
"""
An operation is still pending.
"""
RECURSIVE: 'uno.Enum'
"""
An object cannot be copied into itself.
"""
UNKNOWN: 'uno.Enum'
"""
Unknown.

An unknown I/O error has occurred.
"""
WRITE_PROTECTED: 'uno.Enum'
"""
A function is not possible because the object is write protected.
"""
WRONG_FORMAT: 'uno.Enum'
"""
An incorrect file format.
"""
WRONG_VERSION: 'uno.Enum'
"""
An incorrect file version.
"""

