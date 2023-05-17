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


class CommandGroup(object):
    """
    Const

    provides information about a supported command
    
    **since**
    
        OOo 2.0

    See Also:
        `API CommandGroup <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1frame_1_1CommandGroup.html>`_
    """
    INTERNAL: Literal[0]
    """
    specifies internal commands.
    """
    APPLICATION: Literal[1]
    """
    specifies application based commands.
    """
    VIEW: Literal[2]
    """
    specifies view specific commands.
    """
    DOCUMENT: Literal[3]
    """
    specifies document specific commands.
    """
    EDIT: Literal[4]
    """
    specifies edit specific commands.
    """
    MACRO: Literal[5]
    """
    specifies commands used by the built-in Basic.
    """
    OPTIONS: Literal[6]
    """
    specifies commands to change options.
    """
    MATH: Literal[7]
    """
    specifies math specific commands.
    """
    NAVIGATOR: Literal[8]
    """
    specifies navigate commands.
    """
    INSERT: Literal[9]
    """
    specifies insert commands.
    """
    FORMAT: Literal[10]
    """
    specifies commands that are related to formats.
    """
    TEMPLATE: Literal[11]
    """
    specifies commands that are related to templates.
    """
    TEXT: Literal[12]
    """
    specifies text specific commands.
    """
    FRAME: Literal[13]
    """
    specifies frame specific commands.
    """
    GRAPHIC: Literal[14]
    """
    specifies commands that are related to graphical data.
    """
    TABLE: Literal[15]
    """
    specifies commands that are related to tables.
    """
    ENUMERATION: Literal[16]
    """
    specifies commands that are related to bullets and numbering.
    """
    DATA: Literal[17]
    """
    specifies commands that are related to data.
    """
    SPECIAL: Literal[18]
    """
    specifies special commands.
    """
    IMAGE: Literal[19]
    """
    specifies commands that are related to images.
    """
    CHART: Literal[20]
    """
    specifies chart specific commands.
    """
    EXPLORER: Literal[21]
    """
    specifies explorer specific commands.
    """
    CONNECTOR: Literal[22]
    """
    specifies commands that are related to connectors.
    """
    MODIFY: Literal[23]
    """
    specifies commands that are related to modifications.
    """
    DRAWING: Literal[24]
    """
    specifies commands that are related to drawing.
    """
    CONTROLS: Literal[25]
    """
    specifies commands that are related to controls.
    """

