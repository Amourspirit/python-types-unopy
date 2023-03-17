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
# Namespace: com.sun.star.i18n
from typing_extensions import Literal


class KNumberFormatUsage(object):
    """
    Const

    Category of number format code.

    See Also:
        `API KNumberFormatUsage <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1KNumberFormatUsage.html>`_
    """
    DATE: Literal[1]
    """
    Date format, for example, \"YYYY-MM-DD\".
    """
    TIME: Literal[2]
    """
    Time format, for example, \"HH:MM:SS\".
    """
    DATE_TIME: Literal[3]
    """
    Mixed date/time format, for example, \"YYYY-MM-DD HH:MM:SS\".
    """
    FIXED_NUMBER: Literal[4]
    """
    Numeric format, for example, \"#,##0.00\".
    """
    FRACTION_NUMBER: Literal[5]
    """
    Fractional format, for example, \"# ??/??\".
    """
    PERCENT_NUMBER: Literal[6]
    """
    Percent format, for example, \"0.00%\".
    """
    SCIENTIFIC_NUMBER: Literal[7]
    """
    Scientific format, for example, \"0.00E+00\".
    """
    CURRENCY: Literal[8]
    """
    Currency format, for example, \"#,##0.00 [$EUR]\".
    """

