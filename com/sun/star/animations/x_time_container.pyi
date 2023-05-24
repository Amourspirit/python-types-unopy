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
# Namespace: com.sun.star.animations
from __future__ import annotations
import typing

from .x_animation_node import XAnimationNode as XAnimationNode_1cf10eb9


class XTimeContainer(XAnimationNode_1cf10eb9):
    """
    Supported modules.

    See Also:
        `API XTimeContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1animations_1_1XTimeContainer.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.animations.XTimeContainer'

    def appendChild(self, newChild: XAnimationNode_1cf10eb9) -> XAnimationNode_1cf10eb9:
        """

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def insertAfter(self, newChild: XAnimationNode_1cf10eb9, refChild: XAnimationNode_1cf10eb9) -> XAnimationNode_1cf10eb9:
        """

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def insertBefore(self, newChild: XAnimationNode_1cf10eb9, refChild: XAnimationNode_1cf10eb9) -> XAnimationNode_1cf10eb9:
        """

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def removeChild(self, oldChild: XAnimationNode_1cf10eb9) -> XAnimationNode_1cf10eb9:
        """

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def replaceChild(self, newChild: XAnimationNode_1cf10eb9, oldChild: XAnimationNode_1cf10eb9) -> XAnimationNode_1cf10eb9:
        """

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...


