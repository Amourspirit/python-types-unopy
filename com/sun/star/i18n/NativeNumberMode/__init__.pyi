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
# Libre Office Version: 7.2
# Namespace: com.sun.star.i18n
from typing_extensions import Literal
"""
Const

Constants to use with XExtendedCalendar.getDisplayString() and the XNativeNumberSupplier methods.

The constants have different meanings if used with different locales. However, NATNUM1 always tries to convert to a string matching the native number mode of the corresponding locale.

Where available, the corresponding Microsoft Excel (tm) DBNum number format code modifier is listed.

Modifiers supported by XExtendedCalendar.getDisplayString() are marked with CAL: for the specific language and the corresponding DBNum modifier and the NatNum values used for Y/M/D are listed

**since**

    OOo 1.1.2

See Also:
    `API NativeNumberMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1NativeNumberMode.html>`_
"""
NATNUM0: Literal[0]
"""
Transliteration to ASCII Arabic digits.

Try to convert any native number string to ASCII. If already ASCII it remains ASCII.
"""
NATNUM1: Literal[1]
"""
Transliteration in Chinese: Chinese lower case characters; CAL: 1/7/7 [DBNum1] Japanese: short Kanji characters [DBNum1]; CAL: 1/4/4 [DBNum1] Korean: Korean lower case characters [DBNum1]; CAL: 1/7/7 [DBNum1] Hebrew: Hebrew characters Arabic: Arabic-Indic characters Thai: Thai characters Hindi: Indic-Devanagari characters Odia: Odia (Oriya) charactersMarathi: Indic-Devanagari charactersBengali: Bengali charactersPunjabi: Punjabi (Gurmukhi) charactersGujarati: Gujarati charactersTamil: Tamil charactersTelugu: Telugu charactersKannada: Kannada charactersMalayalam: Malayalam charactersLao: Lao charactersTibetan: Tibetan charactersBurmese: Burmese (Myanmar) charactersKhmer: Khmer (Cambodian) charactersMongolian: Mongolian charactersNepali: Indic-Devanagari charactersDzongkha: Tibetan charactersFarsi: East Arabic-Indic charactersChurch Slavic: Cyrillic characters.
"""
NATNUM2: Literal[2]
"""
Transliteration in Chinese: Chinese upper case characters; CAL: 2/8/8 [DBNum2] Japanese: traditional Kanji characters; CAL: 2/5/5 [DBNum2] Korean: Korean upper case characters [DBNum2]; CAL: 2/8/8 [DBNum2] Hebrew: Hebrew numbering.
"""
NATNUM3: Literal[3]
"""
Transliteration in Chinese: fullwidth Arabic digits; CAL: 3/3/3 [DBNum3] Japanese: fullwidth Arabic digits; CAL: 3/3/3 [DBNum3] Korean: fullwidth Arabic digits [DBNum3]; CAL: 3/3/3 [DBNum3].
"""
NATNUM4: Literal[4]
"""
Transliteration in Chinese: lower case text [DBNum1] Japanese: modern long Kanji text [DBNum2] Korean: formal lower case text.
"""
NATNUM5: Literal[5]
"""
Transliteration in Chinese: Chinese upper case text [DBNum2] Japanese: traditional long Kanji text [DBNum3] Korean: formal upper case text.
"""
NATNUM6: Literal[6]
"""
Transliteration in Chinese: fullwidth text [DBNum3] Japanese: fullwidth text Korean: fullwidth text.
"""
NATNUM7: Literal[7]
"""
Transliteration in Chinese: short lower case text Japanese: modern short Kanji text Korean: informal lower case text.
"""
NATNUM8: Literal[8]
"""
Transliteration in Chinese: short upper case text Japanese: traditional short Kanji text [DBNum4] Korean: informal upper case text.
"""
NATNUM9: Literal[9]
"""
Transliteration in Korean: Hangul characters.
"""
NATNUM10: Literal[10]
"""
Transliteration in Korean: formal Hangul text [DBNum4]; CAL: 9/11/11 [DBNum4].
"""
NATNUM11: Literal[11]
"""
Transliteration in Korean: informal Hangul text.
"""
NATNUM12: Literal[12]
"""
Transliteration to cardinal number names (one, two, three, ...), ordinal number names (first, second, third, ...), ordinal indicators (1st, 2nd, 3rd, ...), etc.

Uses NatNum params string
"""

