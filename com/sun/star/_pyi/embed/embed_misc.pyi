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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.embed
from typing_extensions import Literal


class EmbedMisc(object):
    """
    Const

    The constant set contains flags describing miscellaneous characteristics of embedded objects.
    
    The constant values can be combined with \"or\" operation. The first 32 bits are reserved for MS values, they are added because this API is going to be used to embed MS OLE objects into OOo documents, so there should be a possibility to transfer all the possible MS flags to container. In case own specific values should be added those bits can not be used.

    See Also:
        `API EmbedMisc <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1embed_1_1EmbedMisc.html>`_
    """
    MS_EMBED_RECOMPOSEONRESIZE: Literal[1]
    """
    means that the object wish to regenerate view representation if it's view in the container is resized.
    """
    MS_EMBED_ONLYICONIC: Literal[2]
    """
    The object has no view representation except icon.
    """
    MS_EMBED_INSERTNOTREPLACE: Literal[4]
    """
    If the object is generated from a selection, the selection should not be removed, the object should be inserted beside the selection.
    """
    MS_EMBED_STATIC: Literal[8]
    """
    The object is a static object that contains only representation.
    """
    MS_EMBED_CANTLINKINSIDE: Literal[16]
    MS_EMBED_CANLINKBYOLE1: Literal[32]
    MS_EMBED_ISLINKOBJECT: Literal[64]
    MS_EMBED_INSIDEOUT: Literal[128]
    MS_EMBED_ACTIVATEWHENVISIBLE: Literal[256]
    MS_EMBED_RENDERINGISDEVICEINDEPENDENT: Literal[512]
    MS_EMBED_INVISIBLEATRUNTIME: Literal[1024]
    MS_EMBED_ALWAYSRUN: Literal[2048]
    MS_EMBED_ACTSLIKEBUTTON: Literal[4096]
    MS_EMBED_ACTSLIKELABEL: Literal[8192]
    MS_EMBED_NOUIACTIVATE: Literal[16384]
    MS_EMBED_ALIGNABLE: Literal[32768]
    MS_EMBED_SIMPLEFRAME: Literal[65536]
    MS_EMBED_SETCLIENTSITEFIRST: Literal[131072]
    MS_EMBED_IMEMODE: Literal[262144]
    MS_EMBED_IGNOREACTIVATEWHENVISIBLE: Literal[524288]
    MS_EMBED_WANTSTOMENUMERGE: Literal[1048576]
    MS_EMBED_SUPPORTSMULTILEVELUNDO: Literal[2097152]
    EMBED_ACTIVATEIMMEDIATELY: Literal[4294967296]
    EMBED_NEVERRESIZE: Literal[8589934592]
    EMBED_NEEDSSIZEONLOAD: Literal[17179869184]
    """
    The object needs the size to be provided from the container after it is loaded to function in optimal way.
    """

