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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class GeneralFunction2(object):
    """
    Const

    used to specify a function to be calculated from values.
    
    **since**
    
        LibreOffice 5.3

    See Also:
        `API GeneralFunction2 <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1GeneralFunction2.html>`_
    """
    NONE: Literal[0]
    """
    nothing is calculated.
    """
    AUTO: Literal[1]
    """
    function is determined automatically.
    
    If the values are all numerical, SUM is used, otherwise COUNT.
    """
    SUM: Literal[2]
    """
    sum of all numerical values is calculated.
    """
    COUNT: Literal[3]
    """
    all values, including non-numerical values, are counted.
    """
    AVERAGE: Literal[4]
    """
    average of all numerical values is calculated.
    """
    MAX: Literal[5]
    """
    maximum value of all numerical values is calculated.
    """
    MIN: Literal[6]
    """
    minimum value of all numerical values is calculated.
    """
    PRODUCT: Literal[7]
    """
    product of all numerical values is calculated.
    """
    COUNTNUMS: Literal[8]
    """
    numerical values are counted.
    """
    STDEV: Literal[9]
    """
    standard deviation is calculated based on a sample.
    """
    STDEVP: Literal[10]
    """
    standard deviation is calculated based on the entire population.
    """
    VAR: Literal[11]
    """
    variance is calculated based on a sample.
    """
    VARP: Literal[12]
    """
    variance is calculated based on the entire population.
    """
    MEDIAN: Literal[13]
    """
    median of all numerical values is calculated.
    
    **since**
    
        LibreOffice 5.3
    """

