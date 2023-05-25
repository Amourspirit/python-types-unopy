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
# Namespace: com.sun.star.ucb
from __future__ import annotations
import typing

from ..lang.x_component import XComponent as XComponent_98dc0ab5
from .x_command_processor2 import XCommandProcessor2 as XCommandProcessor2_ed330d4b
from .x_content_identifier_factory import XContentIdentifierFactory as XContentIdentifierFactory_56b91050
from .x_content_provider import XContentProvider as XContentProvider_d4150cc0
from .x_content_provider_manager import XContentProviderManager as XContentProviderManager_37e00f7b


class XUniversalContentBroker(XComponent_98dc0ab5, XCommandProcessor2_ed330d4b, XContentIdentifierFactory_56b91050, XContentProvider_d4150cc0, XContentProviderManager_37e00f7b):
    """
    
    **since**
    
        LibreOffice 4.0

    See Also:
        `API XUniversalContentBroker <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XUniversalContentBroker.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.ucb.XUniversalContentBroker'



