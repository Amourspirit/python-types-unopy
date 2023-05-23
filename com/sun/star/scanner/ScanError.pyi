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
# Namespace: com.sun.star.scanner
# Libre Office Version: 7.4
from __future__ import annotations
from typing import cast
from com.sun.star import UnoEnumProto

class ScanErrorProto(UnoEnumProto):
    InvalidContext: UnoEnumProto
    ScanCanceled: UnoEnumProto
    ScanErrorNone: UnoEnumProto
    ScanFailed: UnoEnumProto
    ScanInProgress: UnoEnumProto
    ScannerNotAvailable: UnoEnumProto

InvalidContext: ScanErrorProto
"""
InvalidContext: a device was requested that does not exist.
"""
ScanCanceled: ScanErrorProto
"""
ScanCanceled: the scan was canceled by the user.
"""
ScanErrorNone: ScanErrorProto
"""
ScanErrorNone: no error occurred.
"""
ScanFailed: ScanErrorProto
"""
ScanFailed: an error occurred during scanning.
"""
ScanInProgress: ScanErrorProto
"""
ScanInProgress: a scan is already in progress on this device that has to end before a new one can be started.
"""
ScannerNotAvailable: ScanErrorProto
"""
ScannerNotAvailable: the requested device could not be opened.
"""

