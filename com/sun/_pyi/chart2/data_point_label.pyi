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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class DataPointLabel(object):
    """
    Struct Class

    
    **since**
    
        LibreOffice 7.1

    See Also:
        `API DataPointLabel <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1DataPointLabel.html>`_
    """
    typeName: Literal['com.sun.star.chart2.DataPointLabel']

    def __init__(self, ShowNumber: typing.Optional[bool] = ..., ShowNumberInPercent: typing.Optional[bool] = ..., ShowCategoryName: typing.Optional[bool] = ..., ShowLegendSymbol: typing.Optional[bool] = ..., ShowCustomLabel: typing.Optional[bool] = ..., ShowSeriesName: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            ShowNumber (bool, optional): ShowNumber value.
            ShowNumberInPercent (bool, optional): ShowNumberInPercent value.
            ShowCategoryName (bool, optional): ShowCategoryName value.
            ShowLegendSymbol (bool, optional): ShowLegendSymbol value.
            ShowCustomLabel (bool, optional): ShowCustomLabel value.
            ShowSeriesName (bool, optional): ShowSeriesName value.
        """


    @property
    def ShowNumber(self) -> bool:
        """
        if TRUE, the value that is represented by a data point is displayed next to it.
        """


    @property
    def ShowNumberInPercent(self) -> bool:
        """
        This is only effective, if ShowNumber is TRUE.
        
        If this member is also TRUE, the numbers are displayed as percentages of a category.
        
        That means, if a data point is the first one of a series, the percentage is calculated by using the first data points of all available series.
        """


    @property
    def ShowCategoryName(self) -> bool:
        """
        The caption contains the category name of the category to which a data point belongs.
        """


    @property
    def ShowLegendSymbol(self) -> bool:
        """
        The symbol of data series is additionally displayed in the caption.
        """


    @property
    def ShowCustomLabel(self) -> bool:
        """
        The caption contains a custom label text, which belongs to a data point label.
        
        **since**
        
            LibreOffice 7.1
        """


    @property
    def ShowSeriesName(self) -> bool:
        """
        The name of the data series is additionally displayed in the caption.
        
        **since**
        
            LibreOffice 7.2
        """



__all__ = ['DataPointLabel']
