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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.script
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XDirectInvocation(XInterface_8f010a43):
    """
    provides access to an object's methods and properties.

    See Also:
        `API XDirectInvocation <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XDirectInvocation.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.script.XDirectInvocation']

    def directInvoke(self, aName: str, aParams: 'typing.Tuple[object, ...]') -> typing.Any:
        """
        provides access to methods and properties exposed by an object.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.script.CannotConvertException: ``CannotConvertException``
            com.sun.star.reflection.InvocationTargetException: ``InvocationTargetException``
        """
        ...
    def hasMember(self, aName: str) -> bool:
        """
        returns TRUE if the method or property with the specified name exists, else FALSE.
        """
        ...


