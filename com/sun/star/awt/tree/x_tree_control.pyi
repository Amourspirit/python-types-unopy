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
# Namespace: com.sun.star.awt.tree
from __future__ import annotations
import typing

from ...view.x_multi_selection_supplier import XMultiSelectionSupplier as XMultiSelectionSupplier_4b0d1020
if typing.TYPE_CHECKING:
    from ..rectangle import Rectangle as Rectangle_84b109e9
    from .x_tree_edit_listener import XTreeEditListener as XTreeEditListener_25e10ee6
    from .x_tree_expansion_listener import XTreeExpansionListener as XTreeExpansionListener_78511115
    from .x_tree_node import XTreeNode as XTreeNode_baaf0ba0


class XTreeControl(XMultiSelectionSupplier_4b0d1020):
    """
    An interface to a control that displays a set of hierarchical data as an outline.

    See Also:
        `API XTreeControl <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1tree_1_1XTreeControl.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.awt.tree.XTreeControl'

    def addTreeEditListener(self, Listener: XTreeEditListener_25e10ee6) -> None:
        """
        Adds a XTreeEditListener.
        """
        ...
    def addTreeExpansionListener(self, Listener: XTreeExpansionListener_78511115) -> None:
        """
        Adds a listener for TreeExpansion events.
        """
        ...
    def cancelEditing(self) -> None:
        """
        Cancels the current editing session.
        
        Has no effect if the tree isn't being edited.
        """
        ...
    def collapseNode(self, Node: XTreeNode_baaf0ba0) -> None:
        """
        Ensures that Node is collapsed.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            ExpandVetoException: ``ExpandVetoException``
        """
        ...
    def expandNode(self, Node: XTreeNode_baaf0ba0) -> None:
        """
        Ensures that Node is expanded and visible.
        
        If Node is a leaf node, this will have no effect.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            ExpandVetoException: ``ExpandVetoException``
        """
        ...
    def getClosestNodeForLocation(self, x: int, y: int) -> XTreeNode_baaf0ba0:
        """
        Returns the node that is closest to x,y.
        
        If no nodes are currently viewable, or there is no model, returns null, otherwise it always returns a valid node. To test if the node is exactly at x, y, use getNodeForLocation().
        """
        ...
    def getNodeForLocation(self, x: int, y: int) -> XTreeNode_baaf0ba0:
        """
        Returns the node at the specified location.
        """
        ...
    def getNodeRect(self, Node: XTreeNode_baaf0ba0) -> Rectangle_84b109e9:
        """
        returns the rectangle occupied by the visual representation of the given node

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def isEditing(self) -> bool:
        """
        Returns TRUE if one of tree's nodes is being currently edited.
        
        The node that is being edited can be obtained using com.sun.star.view.XSelectionSupplier.getSelection().
        """
        ...
    def isNodeCollapsed(self, Node: XTreeNode_baaf0ba0) -> bool:
        """
        Returns TRUE if Node is currently collapsed.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def isNodeExpanded(self, Node: XTreeNode_baaf0ba0) -> bool:
        """
        Returns TRUE if Node is currently expanded.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def isNodeVisible(self, Node: XTreeNode_baaf0ba0) -> bool:
        """
        Returns TRUE if Node is currently visible.
        
        Visible means it is either the root or all of its parents are expanded.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def makeNodeVisible(self, Node: XTreeNode_baaf0ba0) -> None:
        """
        Ensures that Node is currently visible.
        
        This includes expanding all parent nodes and scroll the control so this node is visible in the controls display area.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            ExpandVetoException: ``ExpandVetoException``
        """
        ...
    def removeTreeEditListener(self, Listener: XTreeEditListener_25e10ee6) -> None:
        """
        Removes a XTreeEditListener.
        """
        ...
    def removeTreeExpansionListener(self, Listener: XTreeExpansionListener_78511115) -> None:
        """
        Removes a listener for TreeExpansion events.
        """
        ...
    def startEditingAtNode(self, Node: XTreeNode_baaf0ba0) -> None:
        """
        Selects Node and initiates editing.
        
        If TreeControlModel.Editable is FALSE or if there are no registered XTreeEditListener, this call has no effect.
        
        Calling this method also ensures that Node will become visible.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def stopEditing(self) -> bool:
        """
        Ends the current editing session.
        
        All registered XTreeEditListener are notified if an editing session was in progress
        
        Has no effect if the tree isn't being edited.
        """
        ...

    @property
    def DefaultCollapsedGraphicURL(self) -> str:
        """
        If the given URL points to a loadable graphic, the graphic is rendered before collapsed non leaf nodes.
        
        This can be overridden for individual nodes by XTreeNode.getCollapsedGraphicURL()
        """
        ...
    @DefaultCollapsedGraphicURL.setter
    def DefaultCollapsedGraphicURL(self, value: str) -> None:
        ...
    @property
    def DefaultExpandedGraphicURL(self) -> str:
        """
        If the given URL points to a loadable graphic, the graphic is rendered before expanded non leaf nodes.
        
        This can be overridden for individual nodes by XTreeNode.getExpandedGraphicURL()
        """
        ...
    @DefaultExpandedGraphicURL.setter
    def DefaultExpandedGraphicURL(self, value: str) -> None:
        ...

