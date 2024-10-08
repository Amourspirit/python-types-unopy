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
# Namespace: com.sun.star.text
from __future__ import annotations
from .text_range import TextRange as TextRange_90540a5f
from ..util.x_sortable import XSortable as XSortable_8ff20a5a
from ..beans.x_multi_property_states import XMultiPropertyStates as XMultiPropertyStates_2a3e0f4d
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..beans.x_property_state import XPropertyState as XPropertyState_d55c0ccf
from ..document.x_document_insertable import XDocumentInsertable as XDocumentInsertable_4b911007
from .x_paragraph_cursor import XParagraphCursor as XParagraphCursor_e2fa0d39
from .x_sentence_cursor import XSentenceCursor as XSentenceCursor_d6590cd8
from .x_text_cursor import XTextCursor as XTextCursor_a60c0b48
from .x_word_cursor import XWordCursor as XWordCursor_a5e40b3f

class TextCursor(TextRange_90540a5f, XSortable_8ff20a5a, XSentenceCursor_d6590cd8, XParagraphCursor_e2fa0d39, XWordCursor_a5e40b3f, XTextCursor_a60c0b48, XPropertySet_bc180bfa, XPropertyState_d55c0ccf, XMultiPropertyStates_2a3e0f4d, XDocumentInsertable_4b911007):
    """
    Service Class

    A TextCursor is a TextRange which can be moved within a Text object.

    See Also:
        `API TextCursor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextCursor.html>`_
    """
    ...

