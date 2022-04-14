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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.chart2
from typing_extensions import Literal
import typing
from ..frame.x_model import XModel as XModel_7a6e095c
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
    from .x_chart_type_manager import XChartTypeManager as XChartTypeManager_6330df3
    from .x_diagram import XDiagram as XDiagram_96fe0a59
    from .data.x_data_provider import XDataProvider as XDataProvider_122f0e31

class XChartDocument(XModel_7a6e095c):
    """

    See Also:
        `API XChartDocument <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1XChartDocument.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.chart2.XChartDocument']

    def createDefaultChart(self) -> None:
        """
        Creates a default chart type for a brand-new chart object.
        """
    def createInternalDataProvider(self, bCloneExistingData: bool) -> None:
        """
        creates an internal com.sun.star.chart2.XDataProvider that is handled by the chart document itself.
        
        When the model is stored, the data provider will also be stored in a sub-storage.

        Raises:
            com.sun.star.util.CloseVetoException: ``CloseVetoException``
        """
    def getChartTypeManager(self) -> 'XChartTypeManager_6330df3':
        """
        retrieves the component that is able to create different chart type templates (components of type ChartTypeTemplate)
        """
    def getDataProvider(self) -> 'XDataProvider_122f0e31':
        """
        Returns the currently set data provider.
        
        This may be an internal one, if createInternalDataProvider() has been called before, or an external one if XDataReceiver.attachDataProvider() has been called.
        """
    def getFirstDiagram(self) -> 'XDiagram_96fe0a59':
        """
        Notes: this is preliminary, we need an API that supports more than one diagram. The method name getDiagram exists in the css.chart API, so there is would be no way to chose either this or the other method from Basic (it would chose one or the other by random).
        """
    def getPageBackground(self) -> 'XPropertySet_bc180bfa':
        """
        Gives access to the page background appearance.
        
        The area's extent is equal to the document size. If you want to access properties of the background area of a single diagram (the part where data points are actually plotted in), you have to get its wall. You can get the wall by calling XDiagram.getWall().
        """
    def hasInternalDataProvider(self) -> bool:
        """
        This is the case directly after createInternalDataProvider() has been called, but this is not necessary. The chart can also create an internal data provider by other means, e.g. a call to com.sun.star.frame.XModel.initNew().
        """
    def setChartTypeManager(self, xNewManager: 'XChartTypeManager_6330df3') -> None:
        """
        sets a new component that is able to create different chart type templates (components of type ChartTypeTemplate)
        """
    def setFirstDiagram(self, xDiagram: 'XDiagram_96fe0a59') -> None:
        """
        Notes: this is preliminary, we need an API that supports more than one diagram. The method name setDiagram exists in the css.chart API, so there is would be no way to chose either this or the other method from Basic (it would chose one or the other by random).
        """

__all__ = ['XChartDocument']

