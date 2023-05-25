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


class FocusChangeReason:
    """
    Const

    A combination of these values can be used to specify the reason for a focus change.

    See Also:
        `API FocusChangeReason <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1FocusChangeReason.html>`_
    """
    TAB: int = ...
    """
    Focus changed because TAB was pressed.
    """
    CURSOR: int = ...
    """
    Focus changed because Key Left/Right/Up/Down was pressed.
    """
    MNEMONIC: int = ...
    """
    Focus changed because mnemonic key was pressed.
    """
    FORWARD: int = ...
    """
    Changed Focus to the next control.
    """
    BACKWARD: int = ...
    """
    Changed Focus to the previous control.
    """
    AROUND: int = ...
    """
    Changed Focus forward from last to first or backward from first to last.
    """
    UNIQUEMNEMONIC: int = ...
    """
    Focus changed because mnemonic key was pressed and this mnemonic is unique.
    """
