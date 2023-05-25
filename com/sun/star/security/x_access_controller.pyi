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
# Namespace: com.sun.star.security
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_access_control_context import XAccessControlContext as XAccessControlContext_6d6a10f0
    from .x_action import XAction as XAction_a72e0b36


class XAccessController(XInterface_8f010a43):
    """
    Interface for checking permissions and invoking privileged or restricted actions.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessController <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1security_1_1XAccessController.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.security.XAccessController'

    def checkPermission(self, perm: typing.Any) -> None:
        """
        Determines whether the access request indicated by the specified permission should be allowed or denied, based on the security policy currently in effect.
        
        The semantics are equivalent to the security permission classes of the Java platform.
        
        You can also pass a sequence of permissions (sequence< any >) to check a set of permissions, e.g. for performance reasons. This method quietly returns if the access request is permitted, or throws a suitable AccessControlException otherwise.

        Raises:
            AccessControlException: ``AccessControlException``
        """
        ...
    def doPrivileged(self, action: XAction_a72e0b36, restriction: XAccessControlContext_6d6a10f0) -> typing.Any:
        """
        Perform the specified action adding a set of permissions defined by the given XAccessControlContext.
        
        The action is performed with the union of the permissions of the currently installed XAccessControlContext, the given XAccessControlContext and the security policy currently in effect. The latter includes static security, e.g. based on user credentials.
        
        If the given XAccessControlContext is null, then the action is performed only with the permissions of the security policy currently in effect.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    def doRestricted(self, action: XAction_a72e0b36, restriction: XAccessControlContext_6d6a10f0) -> typing.Any:
        """
        Perform the specified action restricting permissions to the given XAccessControlContext.
        
        The action is performed with the intersection of the permissions of the currently installed XAccessControlContext, the given XAccessControlContext and the security policy currently in effect. The latter includes static security, e.g. based on user credentials.
        
        If the specified XAccessControlContext is null, then the action is performed with unmodified permissions, i.e. the call makes no sense.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    def getContext(self) -> XAccessControlContext_6d6a10f0:
        """
        This method takes a \"snapshot\" of the current calling context and returns it.
        
        This context may then be checked at a later point, possibly in another thread.
        """
        ...



