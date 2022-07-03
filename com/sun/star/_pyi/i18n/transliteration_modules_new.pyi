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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class TransliterationModulesNew(Enum):
    """
    Enum

    

    See Also:
        `API TransliterationModulesNew <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n.html#a436afb2c972c4d40d888b71482e93020>`_
    """
    typeName: str = 'com.sun.star.i18n.TransliterationModulesNew'

    CharToNumHangul_ko: 'uno.Enum'
    """
    Transliterate a Korean Hangul number string to ASCII number string.
    """
    CharToNumLower_ko: 'uno.Enum'
    """
    Transliterate a Korean Hanja lower case number string to ASCII number string.
    """
    CharToNumLower_zh_CN: 'uno.Enum'
    """
    Transliterate a Simplified Chinese lower case number string to ASCII number string.
    """
    CharToNumLower_zh_TW: 'uno.Enum'
    """
    Transliterate a Traditional Chinese lower case number string to ASCII number string.
    """
    CharToNumUpper_ko: 'uno.Enum'
    """
    Transliterate a Korean Hanja upper case number string to ASCII number string.
    """
    CharToNumUpper_zh_CN: 'uno.Enum'
    """
    Transliterate a Simplified Chinese upper case number string to ASCII number string.
    """
    CharToNumUpper_zh_TW: 'uno.Enum'
    """
    Transliterate a Traditional Chinese upper case number string to ASCII number string.
    """
    END_OF_MODULE: 'uno.Enum'
    """
    """
    FULLWIDTH_HALFWIDTH: 'uno.Enum'
    """
    Transliterate a string from full width character to half width character.
    """
    HALFWIDTH_FULLWIDTH: 'uno.Enum'
    """
    Transliterate a string from half width character to full width character.
    """
    HIRAGANA_KATAKANA: 'uno.Enum'
    """
    Transliterate a Japanese string from Hiragana to Katakana.
    """
    IGNORE_CASE: 'uno.Enum'
    """
    Ignore case when comparing strings by transliteration service.
    """
    IGNORE_KANA: 'uno.Enum'
    """
    Ignore Hiragana and Katakana when comparing strings by transliteration service.
    """
    IGNORE_WIDTH: 'uno.Enum'
    """
    Ignore full width and half width character when comparing strings by transliteration service.
    
    Ignore full width and half width characters when comparing strings by transliteration service.
    """
    KATAKANA_HIRAGANA: 'uno.Enum'
    """
    Transliterate a Japanese string from Katakana to Hiragana.
    """
    LOWERCASE_UPPERCASE: 'uno.Enum'
    """
    Transliterate a string from lower case to upper case.
    """
    NumToCharFullwidth: 'uno.Enum'
    """
    Transliterate a half width number string to full width number string.
    """
    NumToCharHangul_ko: 'uno.Enum'
    """
    Transliterate an ASCII number string to Korean Hangul number string.
    """
    NumToCharKanjiShort_ja_JP: 'uno.Enum'
    """
    Transliterate an ASCII number string to Japanese Kanji number string.
    """
    NumToCharLower_ko: 'uno.Enum'
    """
    Transliterate an ASCII number string to Korean Hanja lower case number string.
    """
    NumToCharLower_zh_CN: 'uno.Enum'
    """
    Transliterate an ASCII number string to Simplified Chinese lower case number string.
    """
    NumToCharLower_zh_TW: 'uno.Enum'
    """
    Transliterate an ASCII number string to Traditional Chinese lower case number string.
    """
    NumToCharUpper_ko: 'uno.Enum'
    """
    Transliterate an ASCII number string to Korean Hanja upper case number string.
    """
    NumToCharUpper_zh_CN: 'uno.Enum'
    """
    Transliterate an ASCII number string to Simplified Chinese upper case number string.
    """
    NumToCharUpper_zh_TW: 'uno.Enum'
    """
    Transliterate an ASCII number string to Traditional Chinese upper case number string.
    """
    NumToTextFormalHangul_ko: 'uno.Enum'
    """
    Transliterate an ASCII number string to formal Korean Hangul number string in spellout format.
    """
    NumToTextFormalLower_ko: 'uno.Enum'
    """
    Transliterate an ASCII number string to formal Korean Hanja lower case number string in spellout format.
    """
    NumToTextFormalUpper_ko: 'uno.Enum'
    """
    Transliterate an ASCII number string to formal Korean Hanja upper case number string in spellout format.
    """
    NumToTextInformalHangul_ko: 'uno.Enum'
    """
    Transliterate an ASCII number string to informal Korean Hangul number string in spellout format.
    """
    NumToTextInformalLower_ko: 'uno.Enum'
    """
    Transliterate an ASCII number string to informal Korean Hanja lower case number string in spellout format.
    """
    NumToTextInformalUpper_ko: 'uno.Enum'
    """
    Transliterate an ASCII number string to informal Korean Hanja upper case number string in spellout format.
    """
    NumToTextLower_zh_CN: 'uno.Enum'
    """
    Transliterate an ASCII number string to Simplified Chinese lower case number string in spellout format.
    """
    NumToTextLower_zh_TW: 'uno.Enum'
    """
    Transliterate an ASCII number string to Traditional Chinese lower case number string in spellout format.
    """
    NumToTextUpper_zh_CN: 'uno.Enum'
    """
    Transliterate an ASCII number string to Simplified Chinese upper case number string in spellout format.
    """
    NumToTextUpper_zh_TW: 'uno.Enum'
    """
    Transliterate an ASCII number string to Traditional Chinese upper case number string in spellout format.
    """
    TextToNumFormalHangul_ko: 'uno.Enum'
    """
    Transliterate a Korean formal Hangul number string (spellout) to ASCII number string.
    """
    TextToNumFormalLower_ko: 'uno.Enum'
    """
    Transliterate a Korean formal Hanja lower case number string (spellout) to ASCII number string.
    """
    TextToNumFormalUpper_ko: 'uno.Enum'
    """
    Transliterate a Korean formal Hanja upper case number string (spellout) to ASCII number string.
    """
    TextToNumInformalHangul_ko: 'uno.Enum'
    """
    Transliterate a Korean informal Hangul number string (spellout) to ASCII number string.
    """
    TextToNumInformalLower_ko: 'uno.Enum'
    """
    Transliterate a Korean informal Hanja lower case number string (spellout) to ASCII number string.
    """
    TextToNumInformalUpper_ko: 'uno.Enum'
    """
    Transliterate a Korean informal Hanja upper case number string (spellout) to ASCII number string.
    """
    TextToNumLower_zh_CN: 'uno.Enum'
    """
    Transliterate a Simplified Chinese lower case number string (spellout) to ASCII number string.
    """
    TextToNumLower_zh_TW: 'uno.Enum'
    """
    Transliterate a Traditional Chinese lower case number string (spellout) to ASCII number string.
    """
    TextToNumUpper_zh_CN: 'uno.Enum'
    """
    Transliterate a Simplified Chinese upper case number string (spellout) to ASCII number string.
    """
    TextToNumUpper_zh_TW: 'uno.Enum'
    """
    Transliterate a Traditional Chinese upper case number string (spellout) to ASCII number string.
    """
    UPPERCASE_LOWERCASE: 'uno.Enum'
    """
    Transliterate a string from upper case to lower case.
    """
    ignoreBaFa_ja_JP: 'uno.Enum'
    """
    Ignore Katakana and Hiragana Ba/Gua and Ha/Fa in Japanese fuzzy search.
    """
    ignoreHyuByu_ja_JP: 'uno.Enum'
    """
    Ignore Katakana and Hiragana Hyu/Fyu and Byu/Gyu in Japanese fuzzy search.
    """
    ignoreIandEfollowedByYa_ja_JP: 'uno.Enum'
    """
    Ignore Katakana YA/A which follows the character in either I or E row in Japanese fuzzy search.
    
    Ignore Katakana YA/A following the character in either I or E row in Japanese fuzzy search.
    """
    ignoreIterationMark_ja_JP: 'uno.Enum'
    """
    Ignore Hiragana and Katakana iteration mark in Japanese fuzzy search.
    """
    ignoreKiKuFollowedBySa_ja_JP: 'uno.Enum'
    """
    Ignore Katakana KI/KU which follows the character in SA column in Japanese fuzzy search.
    
    Ignore Katakana KI/KU following the character in SA column in Japanese fuzzy search.
    """
    ignoreMiddleDot_ja_JP: 'uno.Enum'
    """
    Ignore middle dot in Japanese fuzzy search.
    """
    ignoreMinusSign_ja_JP: 'uno.Enum'
    """
    Ignore dash or minus sign in Japanese fuzzy search.
    """
    ignoreProlongedSoundMark_ja_JP: 'uno.Enum'
    """
    Ignore Japanese prolonged sound mark in Japanese fuzzy search.
    """
    ignoreSeZe_ja_JP: 'uno.Enum'
    """
    Ignore Katakana and Hiragana Se/Sye and Ze/Je in Japanese fuzzy search.
    """
    ignoreSeparator_ja_JP: 'uno.Enum'
    """
    Ignore separator punctuations in Japanese fuzzy search.
    """
    ignoreSize_ja_JP: 'uno.Enum'
    """
    Ignore Japanese normal and small sized character in Japanese fuzzy search.
    """
    ignoreSpace_ja_JP: 'uno.Enum'
    """
    Ignore white space characters, include space, TAB, return, etc. in Japanese fuzzy search.
    """
    ignoreTiJi_ja_JP: 'uno.Enum'
    """
    Ignore Katakana and Hiragana Tsui/Tea/Ti and Dyi/Ji in Japanese fuzzy search.
    """
    ignoreTraditionalKana_ja_JP: 'uno.Enum'
    """
    Ignore Japanese traditional Katakana and Hiragana character in Japanese fuzzy search.
    
    Ignore Japanese traditional Katakana and Hiragana characters in Japanese fuzzy search.
    """
    ignoreTraditionalKanji_ja_JP: 'uno.Enum'
    """
    Ignore Japanese traditional Kanji character in Japanese fuzzy search.
    
    Ignore Japanese traditional Kanji characters in Japanese fuzzy search.
    """
    ignoreZiZu_ja_JP: 'uno.Enum'
    """
    Ignore Katakana and Hiragana Zi/Zi and Zu/Zu in Japanese fuzzy search.
    """
    largeToSmall_ja_JP: 'uno.Enum'
    """
    transliterate Japanese normal sized character to small sized character
    """
    smallToLarge_ja_JP: 'uno.Enum'
    """
    transliterate Japanese small sized character to normal sized character
    """

