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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.chart
from __future__ import annotations
import typing
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_axis import XAxis as XAxis_71210907
from ..drawing.line_properties import LineProperties as LineProperties_f13f0da9
from ..style.character_properties import CharacterProperties as CharacterProperties_1d4f0ef3
from ..xml.user_defined_attributes_supplier import UserDefinedAttributesSupplier as UserDefinedAttributesSupplier_9fbe1222
if typing.TYPE_CHECKING:
    from .time_increment import TimeIncrement as TimeIncrement_c7e70c4e
    from com.sun.star.chart.ChartAxisArrangeOrderType import ChartAxisArrangeOrderTypeProto  # type: ignore
    from com.sun.star.chart.ChartAxisPosition import ChartAxisPositionProto  # type: ignore
    from com.sun.star.chart.ChartAxisLabelPosition import ChartAxisLabelPositionProto  # type: ignore
    from com.sun.star.chart.ChartAxisMarkPosition import ChartAxisMarkPositionProto  # type: ignore

class ChartAxis(LineProperties_f13f0da9, CharacterProperties_1d4f0ef3, UserDefinedAttributesSupplier_9fbe1222, XPropertySet_bc180bfa, XAxis_71210907):
    """
    Service Class

    Specifies the axes in a diagram.
    
    Note: The text properties correlate to all axis description elements, not to just a single text element.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API ChartAxis <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1ChartAxis.html>`_
    """
    @property
    def ArrangeOrder(self) -> ChartAxisArrangeOrderTypeProto:
        """
        The axis description may be arranged in a special order for a better placement.
        """
        ...
    @ArrangeOrder.setter
    def ArrangeOrder(self, value: ChartAxisArrangeOrderTypeProto) -> None:
        ...
    @property
    def AutoMax(self) -> bool:
        """
        The maximum value of the axis scale is calculated by the chart if this property is TRUE.
        """
        ...
    @AutoMax.setter
    def AutoMax(self, value: bool) -> None:
        ...
    @property
    def AutoMin(self) -> bool:
        """
        The minimum value of the axis scale is calculated by the chart if this property is TRUE.
        """
        ...
    @AutoMin.setter
    def AutoMin(self, value: bool) -> None:
        ...
    @property
    def AutoOrigin(self) -> bool:
        """
        The origin is calculated by the chart if this property is TRUE.
        """
        ...
    @AutoOrigin.setter
    def AutoOrigin(self, value: bool) -> None:
        ...
    @property
    def AutoStepHelp(self) -> bool:
        """
        The number of help intervals within a main interval is calculated by the chart if this property is TRUE.
        """
        ...
    @AutoStepHelp.setter
    def AutoStepHelp(self, value: bool) -> None:
        ...
    @property
    def AutoStepMain(self) -> bool:
        """
        The distance between the main tick marks is calculated by the chart if this property is TRUE.
        """
        ...
    @AutoStepMain.setter
    def AutoStepMain(self, value: bool) -> None:
        ...
    @property
    def AxisType(self) -> int:
        """
        determines which type of axis this is, e.g.
        
        a date-axis or a category-axis
        
        **since**
        
            OOo 3.4
        """
        ...
    @AxisType.setter
    def AxisType(self, value: int) -> None:
        ...
    @property
    def CrossoverPosition(self) -> ChartAxisPositionProto:
        """
        Determines where the axis crosses the other axis.
        """
        ...
    @CrossoverPosition.setter
    def CrossoverPosition(self, value: ChartAxisPositionProto) -> None:
        ...
    @property
    def CrossoverValue(self) -> float:
        """
        Determines the scale value on the other axis when CrossoverPosition is set to VALUE.
        """
        ...
    @CrossoverValue.setter
    def CrossoverValue(self, value: float) -> None:
        ...
    @property
    def DisplayLabels(self) -> bool:
        """
        Properties for axes labels:
        
        Determines whether to display text at the axis or not.
        """
        ...
    @DisplayLabels.setter
    def DisplayLabels(self, value: bool) -> None:
        ...
    @property
    def GapWidth(self) -> int:
        """
        Specifies the width of the gaps between each set of data points in a bar chart.
        
        The value is given in percent of the width of a bar; the valid range is 0 to 600%.
        """
        ...
    @GapWidth.setter
    def GapWidth(self, value: int) -> None:
        ...
    @property
    def HelpMarks(self) -> int:
        """
        Determines the type of the help marks.
        """
        ...
    @HelpMarks.setter
    def HelpMarks(self, value: int) -> None:
        ...
    @property
    def LabelPosition(self) -> ChartAxisLabelPositionProto:
        """
        Determines where the axis labels are placed.
        """
        ...
    @LabelPosition.setter
    def LabelPosition(self, value: ChartAxisLabelPositionProto) -> None:
        ...
    @property
    def LinkNumberFormatToSource(self) -> bool:
        """
        determines whether to use the number format given by the container application, e.g.
        
        a spreadsheet document, or from the own property NumberFormat.
        """
        ...
    @LinkNumberFormatToSource.setter
    def LinkNumberFormatToSource(self, value: bool) -> None:
        ...
    @property
    def Logarithmic(self) -> bool:
        """
        Determines if the axis is scaled logarithmically or not (linear).
        """
        ...
    @Logarithmic.setter
    def Logarithmic(self, value: bool) -> None:
        ...
    @property
    def MarkPosition(self) -> ChartAxisMarkPositionProto:
        """
        Determines where the interval marks are placed.
        """
        ...
    @MarkPosition.setter
    def MarkPosition(self, value: ChartAxisMarkPositionProto) -> None:
        ...
    @property
    def Marks(self) -> int:
        """
        Properties for interval marks:
        
        Determines the type of the marks.
        """
        ...
    @Marks.setter
    def Marks(self, value: int) -> None:
        ...
    @property
    def Max(self) -> float:
        """
        Properties for scaling:
        
        Contains the maximum value for the axis scale.
        """
        ...
    @Max.setter
    def Max(self, value: float) -> None:
        ...
    @property
    def Min(self) -> float:
        """
        Contains the minimum value for the axis scale.
        """
        ...
    @Min.setter
    def Min(self, value: float) -> None:
        ...
    @property
    def NumberFormat(self) -> int:
        """
        Contains the type id for the number formatter of the axis.
        """
        ...
    @NumberFormat.setter
    def NumberFormat(self, value: int) -> None:
        ...
    @property
    def Origin(self) -> float:
        """
        Indicates the reference value where bars or areas have their grounding.
        
        This property has only an effect when the used ODF file format does not allow for further axis positioning or the axis is a secondary y-axis.
        """
        ...
    @Origin.setter
    def Origin(self, value: float) -> None:
        ...
    @property
    def Overlap(self) -> int:
        """
        Properties related to bar charts:
        
        Determines the overlap of the bars in a bar-type chart.
        
        The value is given in percent of the width of the bars. The valid range is -100% to +100%. +100% means full overlap, -100% indicates a distance of one bar between 2 neighboring bars.
        """
        ...
    @Overlap.setter
    def Overlap(self, value: int) -> None:
        ...
    @property
    def ReverseDirection(self) -> bool:
        """
        Determines if the axis orientation is mathematical or reversed.
        """
        ...
    @ReverseDirection.setter
    def ReverseDirection(self, value: bool) -> None:
        ...
    @property
    def StepHelp(self) -> float:
        """
        """
        ...
    @StepHelp.setter
    def StepHelp(self, value: float) -> None:
        ...
    @property
    def StepHelpCount(self) -> int:
        """
        Contains the number of help intervals within a main interval.
        
        E.g. a StepHelpCount of 5 divides the main interval into 5 pieces and thus produces 4 help tick marks.
        """
        ...
    @StepHelpCount.setter
    def StepHelpCount(self, value: int) -> None:
        ...
    @property
    def StepMain(self) -> float:
        """
        Contains the distance between the main tick marks.
        """
        ...
    @StepMain.setter
    def StepMain(self, value: float) -> None:
        ...
    @property
    def TextBreak(self) -> bool:
        """
        Determines if long text is broken into multiple lines.
        """
        ...
    @TextBreak.setter
    def TextBreak(self, value: bool) -> None:
        ...
    @property
    def TextCanOverlap(self) -> bool:
        """
        Determines if certain labels are hidden, if they would otherwise overlap.
        
        In this case, the value of this property must be set to FALSE.
        """
        ...
    @TextCanOverlap.setter
    def TextCanOverlap(self, value: bool) -> None:
        ...
    @property
    def TextRotation(self) -> int:
        """
        Determines the rotation of the text elements (axis description) in 100th degrees.
        """
        ...
    @TextRotation.setter
    def TextRotation(self, value: int) -> None:
        ...
    @property
    def TimeIncrement(self) -> TimeIncrement_c7e70c4e:
        """
        if the current axis is a date-axis the intervals are chosen as given with TimeIncrement
        
        **since**
        
            OOo 3.4
        """
        ...
    @TimeIncrement.setter
    def TimeIncrement(self, value: TimeIncrement_c7e70c4e) -> None:
        ...