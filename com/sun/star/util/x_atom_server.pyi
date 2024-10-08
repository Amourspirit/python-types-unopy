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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.util
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .atom_class_request import AtomClassRequest as AtomClassRequest_e2a60d36
    from .atom_description import AtomDescription as AtomDescription_d6080cdb


class XAtomServer(XInterface_8f010a43):
    """
    an interface to map between strings and ids
    
    a note on atoms:Atoms are abbreviations for strings. When a string gets registered, it is assigned a numeric id so that said string can always be referred to by this id. This way strings have to be transported only once over remote connections. Valid ids are (in this implementation) non zero, signed 32 bit values. An atom of 0 means that the string in question is not registered
    
    Additionally there is the abstraction of atom class:Atoms are grouped into classes, so that an id can be assigned to multiple strings, depending on the class context. The main advantage of this is that atoms in one class may be kept to small numbers, so that bandwidth can be reduced by sending the atoms only as 16 bit values. Note that it is up to the user in this case to handle overflows.

    See Also:
        `API XAtomServer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XAtomServer.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.util.XAtomServer'

    def getAtom(self, atomClass: int, description: str, create: bool) -> int:
        """
        registers or searches for a string
        """
        ...
    def getAtomDescriptions(self, atoms: typing.Tuple[AtomClassRequest_e2a60d36, ...]) -> typing.Tuple[str, ...]:
        """
        returns the strings for an arbitrary amount of atoms of multiple classes
        """
        ...
    def getClass(self, atomClass: int) -> typing.Tuple[AtomDescription_d6080cdb, ...]:
        """
        returns a whole atom class
        """
        ...
    def getClasses(self, atomClasses: typing.Tuple[int, ...]) -> typing.Tuple[typing.Tuple[AtomDescription_d6080cdb, ...], ...]:
        """
        returns multiple atom classes
        """
        ...
    def getRecentAtoms(self, atomClass: int, atom: int) -> typing.Tuple[AtomDescription_d6080cdb, ...]:
        """
        returns the atoms that have been registered to a class after an already known atom
        
        Hint to implementor: using ascending atoms is the easiest way to decide, which atoms are recent.
        """
        ...


