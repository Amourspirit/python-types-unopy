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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.ucb
import typing


class ContentAction:
    """
    Const

    specifies actions which can be transported with content events.
    
    The situations under which contents will send ContentEvents of the various action types are described below. The description is broken into a list of useful definitions, a list of events that happen to contents, and a list of reactions taken by contents in response to those events.
    
    The definitions are as follows:
    
    The events that can happen to contents (and that are of interest in this context) are listed next. Note that \"event\" here does not mean an ContentEvent, but rather some event that occurs either because some content processes a command, or because a content gets informed about a relevant change in the underlying system it represents.
    
    Finally, the list of reactions taken by contents in response to the above events gives a description of what kinds of ContentEvents are sent in which situations:

    See Also:
        `API ContentAction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb_1_1ContentAction.html>`_
    """
    INSERTED: int = ...
    """
    A content was inserted into a folder content (i.e., while updating the folder).
    
    This action must be notified at the listeners of the folder content.
    """
    REMOVED: int = ...
    """
    A content was removed from a folder content, but not physically destroyed (i.e., due to rules just applied to the folder).
    
    This action must be notified at the listeners of the folder content.
    """
    DELETED: int = ...
    """
    A content was physically destroyed.
    
    Events containing this action may be generated at any time. So a content event listener should be prepared to get notified the \"death\" of the related content!
    
    This action must be notified at the listeners of the deleted content.
    """
    EXCHANGED: int = ...
    """
    This Action indicates that a content has changed its identity (i.e.
    
    after renaming a file system folder).
    
    This action must be notified at the listeners of the exchanged content.
    """
    SEARCH_MATCHED: int = ...
    """
    This is obsolete and should no longer be used.
    """

