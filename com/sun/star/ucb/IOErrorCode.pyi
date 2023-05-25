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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class IOErrorCodeProto(Protocol):
    """Protocol for IOErrorCode"""

    @property
    def typeName(self) -> Literal["com.sun.star.ucb.IOErrorCode"]:
        ...
    value: Any
    ABORT: IOErrorCodeProto
    ACCESS_DENIED: IOErrorCodeProto
    ALREADY_EXISTING: IOErrorCodeProto
    BAD_CRC: IOErrorCodeProto
    CANT_CREATE: IOErrorCodeProto
    CANT_READ: IOErrorCodeProto
    CANT_SEEK: IOErrorCodeProto
    CANT_TELL: IOErrorCodeProto
    CANT_WRITE: IOErrorCodeProto
    CURRENT_DIRECTORY: IOErrorCodeProto
    DEVICE_NOT_READY: IOErrorCodeProto
    DIFFERENT_DEVICES: IOErrorCodeProto
    GENERAL: IOErrorCodeProto
    INVALID_ACCESS: IOErrorCodeProto
    INVALID_CHARACTER: IOErrorCodeProto
    INVALID_DEVICE: IOErrorCodeProto
    INVALID_LENGTH: IOErrorCodeProto
    INVALID_PARAMETER: IOErrorCodeProto
    IS_WILDCARD: IOErrorCodeProto
    LOCKING_VIOLATION: IOErrorCodeProto
    MISPLACED_CHARACTER: IOErrorCodeProto
    NAME_TOO_LONG: IOErrorCodeProto
    NOT_EXISTING: IOErrorCodeProto
    NOT_EXISTING_PATH: IOErrorCodeProto
    NOT_SUPPORTED: IOErrorCodeProto
    NO_DIRECTORY: IOErrorCodeProto
    NO_FILE: IOErrorCodeProto
    OUT_OF_DISK_SPACE: IOErrorCodeProto
    OUT_OF_FILE_HANDLES: IOErrorCodeProto
    OUT_OF_MEMORY: IOErrorCodeProto
    PENDING: IOErrorCodeProto
    RECURSIVE: IOErrorCodeProto
    UNKNOWN: IOErrorCodeProto
    WRITE_PROTECTED: IOErrorCodeProto
    WRONG_FORMAT: IOErrorCodeProto
    WRONG_VERSION: IOErrorCodeProto

ABORT: IOErrorCodeProto
"""
An operation was aborted.
"""
ACCESS_DENIED: IOErrorCodeProto
"""
An object cannot be accessed due to insufficient user rights.
"""
ALREADY_EXISTING: IOErrorCodeProto
"""
An object already exists.
"""
BAD_CRC: IOErrorCodeProto
"""
A bad checksum.
"""
CANT_CREATE: IOErrorCodeProto
"""
An object could not be created.
"""
CANT_READ: IOErrorCodeProto
"""
Data could not be read from a file.
"""
CANT_SEEK: IOErrorCodeProto
"""
A seek operation could not be run.
"""
CANT_TELL: IOErrorCodeProto
"""
A tell operation could not be run.
"""
CANT_WRITE: IOErrorCodeProto
"""
Data could not be written to a file.
"""
CURRENT_DIRECTORY: IOErrorCodeProto
"""
A function is not possible because the path contains the current directory.
"""
DEVICE_NOT_READY: IOErrorCodeProto
"""
A device (drive) not ready.
"""
DIFFERENT_DEVICES: IOErrorCodeProto
"""
A function is not possible because the devices (drives) are not identical.
"""
GENERAL: IOErrorCodeProto
"""
A general input/output error.
"""
INVALID_ACCESS: IOErrorCodeProto
"""
An invalid attempt was made to access an object.
"""
INVALID_CHARACTER: IOErrorCodeProto
"""
A file name contains invalid characters.
"""
INVALID_DEVICE: IOErrorCodeProto
"""
A specified device is invalid.
"""
INVALID_LENGTH: IOErrorCodeProto
"""
Invalid data length.
"""
INVALID_PARAMETER: IOErrorCodeProto
"""
An operation was started with an invalid parameter.
"""
IS_WILDCARD: IOErrorCodeProto
"""
An operation cannot be run on file names containing wildcards.
"""
LOCKING_VIOLATION: IOErrorCodeProto
"""
A locking problem.
"""
MISPLACED_CHARACTER: IOErrorCodeProto
"""
An invalid file name.
"""
NAME_TOO_LONG: IOErrorCodeProto
"""
A file name is too long.
"""
NOT_EXISTING: IOErrorCodeProto
"""
A nonexistent object.
"""
NOT_EXISTING_PATH: IOErrorCodeProto
"""
The path to a file does not exist.
"""
NOT_SUPPORTED: IOErrorCodeProto
"""
An action is not supported.
"""
NO_DIRECTORY: IOErrorCodeProto
"""
An object is not a directory.
"""
NO_FILE: IOErrorCodeProto
"""
An object is not a file.
"""
OUT_OF_DISK_SPACE: IOErrorCodeProto
"""
No more space on a device.
"""
OUT_OF_FILE_HANDLES: IOErrorCodeProto
"""
No more file handles available.
"""
OUT_OF_MEMORY: IOErrorCodeProto
"""
An operation could not be run due to insufficient memory.
"""
PENDING: IOErrorCodeProto
"""
An operation is still pending.
"""
RECURSIVE: IOErrorCodeProto
"""
An object cannot be copied into itself.
"""
UNKNOWN: IOErrorCodeProto
"""
Unknown.

An unknown I/O error has occurred.
"""
WRITE_PROTECTED: IOErrorCodeProto
"""
A function is not possible because the object is write protected.
"""
WRONG_FORMAT: IOErrorCodeProto
"""
An incorrect file format.
"""
WRONG_VERSION: IOErrorCodeProto
"""
An incorrect file version.
"""
