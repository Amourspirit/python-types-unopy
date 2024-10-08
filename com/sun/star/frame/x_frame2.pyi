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
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing

from .x_dispatch_information_provider import XDispatchInformationProvider as XDispatchInformationProvider_afb6126c
from .x_dispatch_provider import XDispatchProvider as XDispatchProvider_fc690de6
from .x_dispatch_provider_interception import XDispatchProviderInterception as XDispatchProviderInterception_c2a512da
from .x_frames_supplier import XFramesSupplier as XFramesSupplier_e12a0d1d
from ..task.x_status_indicator_factory import XStatusIndicatorFactory as XStatusIndicatorFactory_49e4100c
if typing.TYPE_CHECKING:
    from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
    from .x_dispatch_recorder_supplier import XDispatchRecorderSupplier as XDispatchRecorderSupplier_79301125
    from ..uno.x_interface import XInterface as XInterface_8f010a43


class XFrame2(XDispatchInformationProvider_afb6126c, XDispatchProvider_fc690de6, XDispatchProviderInterception_c2a512da, XFramesSupplier_e12a0d1d, XStatusIndicatorFactory_49e4100c):
    """
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API XFrame2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XFrame2.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.frame.XFrame2'

    @property
    def DispatchRecorderSupplier(self) -> XDispatchRecorderSupplier_79301125:
        """
        provides access to the dispatch recorder of the frame
        
        Such recorder can be used to record dispatch requests. The supplier contains a dispatch recorder and provide the functionality to use it for any dispatch object from outside which supports the interface XDispatch. A supplier is available only, if recording was enabled. That means: if someone wishes to enable recoding on a frame he must set a supplier with a recorder object inside of it. Every user of dispatches has to check then if such supplier is available at this frame property. If value of this property is NULL he must call XDispatch.dispatch() on the original dispatch object. If it's a valid value he must use the supplier by calling his method XDispatchRecorderSupplier.dispatchAndRecord() with the original dispatch object as argument.
        
        Note:It's not recommended to cache an already gotten supplier. Because there exist no possibility to check for enabled/disabled recording then.
        
        **since**
        
            OOo 1.1.2
        """
        ...
    @DispatchRecorderSupplier.setter
    def DispatchRecorderSupplier(self, value: XDispatchRecorderSupplier_79301125) -> None:
        ...
    @property
    def LayoutManager(self) -> XInterface_8f010a43:
        """
        Provides access to the LayoutManager of the frame.
        
        This is actually of type XLayoutManager, but this API is still experimental (unpublished).
        """
        ...
    @LayoutManager.setter
    def LayoutManager(self, value: XInterface_8f010a43) -> None:
        ...
    @property
    def Title(self) -> str:
        """
        if possible it sets/gets the UI title on/from the frame container window
        
        It depends from the type of the frame container window. If it is a system task window all will be OK. Otherwise the title can't be set. Setting/getting of the pure value of this property must be possible in every case. Only showing on the UI can be fail.
        """
        ...
    @Title.setter
    def Title(self, value: str) -> None:
        ...
    @property
    def UserDefinedAttributes(self) -> XNameContainer_cb90e47:
        """
        contains user defined attributes.
        """
        ...
    @UserDefinedAttributes.setter
    def UserDefinedAttributes(self, value: XNameContainer_cb90e47) -> None:
        ...

