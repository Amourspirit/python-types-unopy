# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.configuration.backend.xml
from ..x_layer import XLayer as XLayer_4cd50fcb
from ....io.x_active_data_sink import XActiveDataSink as XActiveDataSink_b8d00ba3
from ....lang.x_initialization import XInitialization as XInitialization_d46c0cca

class LayerParser(XLayer_4cd50fcb, XActiveDataSink_b8d00ba3, XInitialization_d46c0cca):
    """
    Service Class

    represents a configuration data layer that is stored in a stream in OOR Update XML format.
    
    The configuration layer XML from a given stream is parsed and fed to a com.sun.star.configuration.backend.XLayerHandler.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API LayerParser <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1xml_1_1LayerParser.html>`_
    """
    ...

