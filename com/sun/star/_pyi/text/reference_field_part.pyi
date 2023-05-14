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
# Namespace: com.sun.star.text
from typing_extensions import Literal


class ReferenceFieldPart(object):
    """
    Const

    These constants define how the reference position is displayed in reference text fields.
    
    **since**
    
        OOo 3.0

    See Also:
        `API ReferenceFieldPart <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1ReferenceFieldPart.html>`_
    """
    PAGE: Literal[0]
    """
    The page number is displayed using Arabic numbers.
    """
    CHAPTER: Literal[1]
    """
    The number of the chapter is displayed.
    """
    TEXT: Literal[2]
    """
    The reference text is displayed.
    
    If the source of the reference is a sequence field, then the complete text of the paragraph is displayed. This is useful to reference to captions.
    """
    UP_DOWN: Literal[3]
    """
    The reference is displayed as one of the (localized) words, \"above\" or \"below\".
    """
    PAGE_DESC: Literal[4]
    """
    The page number is displayed using the numbering type defined in the page style of the reference position.
    """
    CATEGORY_AND_NUMBER: Literal[5]
    """
    The category and the number of a caption is displayed.
    
    This option is only valid if the source of the reference is a sequence field.
    """
    ONLY_CAPTION: Literal[6]
    """
    The caption text of a caption is displayed.
    
    This option is only valid if the source of the reference is a sequence field.
    """
    ONLY_SEQUENCE_NUMBER: Literal[7]
    """
    The number of a sequence field is displayed.
    
    This option is only valid if the source of the reference is a sequence field.
    """
    NUMBER: Literal[8]
    """
    The numbering label and depending of the reference field context numbering labels of superior list levels of the reference are displayed.
    
    This option is only valid, if the source of the reference is a bookmark or a set reference.
    
    The contents of the list label of the paragraph, at which the bookmark respectively the set reference starts - named \"referenced item\" in the following - is displayed. To unambiguous identify the referenced item at the document position of the reference text field, the content of all needed superior levels are added in front. The needed superior levels of the referenced item are the ones, which differ from the superior levels of the document position of the reference text field. Additional condition, which suppresses the addition of a superior level's list label content: The list label of the referenced item can already contain numbers of a superior levels. Assume X be the level of the most superior level, then no list label content of superior levels greater or equal than X are added. If the referenced item isn't numbered, nothing is displayed.
    
    **since**
    
        OOo 3.0
    """
    NUMBER_NO_CONTEXT: Literal[9]
    """
    The numbering label of the reference is displayed.
    
    This option is only valid, if the source of the reference is a bookmark or a set reference.
    
    The contents of the list label of the paragraph, at which the bookmark respectively the set reference starts, is displayed. If this paragraph isn't numbered, nothing is displayed.
    
    **since**
    
        OOo 3.0
    """
    NUMBER_FULL_CONTEXT: Literal[10]
    """
    The numbering label and numbering labels of superior list levels of the reference are displayed.
    
    This option is only valid, if the source of the reference is a bookmark or a set reference.
    
    The contents of the list label of the paragraph, at which the bookmark respectively the set reference starts - named \"referenced item\" in the following - is displayed and the contents of all list labels of superior levels are added in front of it. Additional condition, which suppresses the addition of a superior level's list label content: The list label of the referenced item can already contain numbers of a superior levels. Assume X be the level of the most superior level, then no list label content of superior levels greater or equal than X are added. If the referenced item is numbered nothing is displayed.
    
    **since**
    
        OOo 3.0
    """

