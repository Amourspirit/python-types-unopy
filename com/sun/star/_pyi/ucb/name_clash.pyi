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
# Namespace: com.sun.star.ucb
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class NameClash(object):
    """
    Const

    These are the possible values for TransferInfo.NameClash.

    See Also:
        `API NameClash <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb_1_1NameClash.html>`_
    """
    ERROR: Literal[0]
    """
    Means to set an error and cancel the operation.
    """
    OVERWRITE: Literal[1]
    """
    Means to overwrite the object in the target folder with the object to transfer.
    """
    RENAME: Literal[2]
    """
    Means to rename the object to transfer to solve the clash.
    
    The implementation needs to supply and set a suitable new name.
    """
    KEEP: Literal[3]
    """
    Deprecated.
    
    Do not use!
    """
    ASK: Literal[4]
    """
    Means to use a NameClashResolveRequest in order to solve the name clash.
    """

