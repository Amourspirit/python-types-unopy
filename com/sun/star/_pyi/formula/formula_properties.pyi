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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.formula
from abc import ABC

class FormulaProperties(ABC):
    """
    Service Class

    The formula properties provide access to the properties of a formula in a formula generator.
    
    **since**
    
        OOo 3.4

    See Also:
        `API FormulaProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1formula_1_1FormulaProperties.html>`_
    """
    @property
    def Alignment(self) -> int:
        """
        contains the alignment of the formula.
        """
        ...
    @property
    def BaseFontHeight(self) -> int:
        """
        contains the base font height in point the formula will be formatted in.
        
        All properties containing relative values are related to this value.
        """
        ...
    @property
    def BaseLine(self) -> int:
        """
        contains the baselines offset in respect to the top of the formula rectangle
        
        **since**
        
            OOo 3.4
        """
        ...
    @property
    def BottomMargin(self) -> int:
        """
        contains the metric value of the bottom margin of the formula.
        """
        ...
    @property
    def CustomFontNameFixed(self) -> str:
        """
        customized name for fixed font.
        """
        ...
    @property
    def CustomFontNameSans(self) -> str:
        """
        customized name for sans serif font
        """
        ...
    @property
    def CustomFontNameSerif(self) -> str:
        """
        customized name for serif font
        """
        ...
    @property
    def FontFixedIsBold(self) -> bool:
        """
        determines if the customized fixed font is bold.
        """
        ...
    @property
    def FontFixedIsItalic(self) -> bool:
        """
        determines if the customized fixed font is italic.
        """
        ...
    @property
    def FontFunctionsIsBold(self) -> bool:
        """
        determines if the font that is used to display functions is bold.
        """
        ...
    @property
    def FontFunctionsIsItalic(self) -> bool:
        """
        determines if the font that is used to display functions is italic.
        """
        ...
    @property
    def FontNameFunctions(self) -> str:
        """
        contains the name of the font that is used to display functions contained in the formula.
        """
        ...
    @property
    def FontNameNumbers(self) -> str:
        """
        contains the name of the font that is used to display numbers contained in the formula.
        """
        ...
    @property
    def FontNameText(self) -> str:
        """
        contains the name of the font that is used to display text contained in the formula.
        """
        ...
    @property
    def FontNameVariables(self) -> str:
        """
        contains the name of the font that is used to display variables contained in the formula.
        """
        ...
    @property
    def FontNumbersIsBold(self) -> bool:
        """
        determines if the font that is used to display numbers is bold.
        """
        ...
    @property
    def FontNumbersIsItalic(self) -> bool:
        """
        determines if the font that is used to display numbers is italic.
        """
        ...
    @property
    def FontSansIsBold(self) -> bool:
        """
        determines if the customized sans serif font is bold.
        """
        ...
    @property
    def FontSansIsItalic(self) -> bool:
        """
        determines if the customized sans serif font is italic.
        """
        ...
    @property
    def FontSerifIsBold(self) -> bool:
        """
        determines if the customized serif font is bold.
        """
        ...
    @property
    def FontSerifIsItalic(self) -> bool:
        """
        determines if the customized serif font is italic.
        """
        ...
    @property
    def FontTextIsBold(self) -> bool:
        """
        determines if the font that is used to display text is bold.
        """
        ...
    @property
    def FontTextIsItalic(self) -> bool:
        """
        determines if the font that is used to display text is italic.
        """
        ...
    @property
    def FontVariablesIsBold(self) -> bool:
        """
        determines if the font that is used to display variables is bold.
        """
        ...
    @property
    def FontVariablesIsItalic(self) -> bool:
        """
        determines if the font that is used to display variables is italic.
        """
        ...
    @property
    def Formula(self) -> str:
        """
        contains the command string of the formula
        """
        ...
    @property
    def IsScaleAllBrackets(self) -> bool:
        """
        decides if all brackets (even those without \"left\"/\"right\" modifier) are scaled.
        """
        ...
    @property
    def IsTextMode(self) -> bool:
        """
        switches into text mode.
        
        This is a mode where formulas are displayed the same height as a line of text.
        """
        ...
    @property
    def LeftMargin(self) -> int:
        """
        contains the metric value of the left margin of the formula.
        """
        ...
    @property
    def RelativeBracketDistance(self) -> int:
        """
        contains the relative distance of brackets.
        """
        ...
    @property
    def RelativeBracketExcessSize(self) -> int:
        """
        contains the relative excess size of brackets.
        """
        ...
    @property
    def RelativeFontHeightFunctions(self) -> int:
        """
        contains the relative height of the font for functions.
        
        The values unit is percent of the com.sun.star.formula.FormulaProperties.BaseFontHeight
        """
        ...
    @property
    def RelativeFontHeightIndices(self) -> int:
        """
        contains the relative height of the font for indices.
        
        The values unit is percent of the com.sun.star.formula.FormulaProperties.BaseFontHeight
        """
        ...
    @property
    def RelativeFontHeightLimits(self) -> int:
        """
        contains the relative height of the font for limits.
        
        The values unit is percent of the com.sun.star.formula.FormulaProperties.BaseFontHeight
        """
        ...
    @property
    def RelativeFontHeightOperators(self) -> int:
        """
        contains the relative height of the font for operators.
        
        The values unit is percent of the com.sun.star.formula.FormulaProperties.BaseFontHeight
        """
        ...
    @property
    def RelativeFontHeightText(self) -> int:
        """
        contains the relative height of the font for text.
        
        The values unit is percent of the com.sun.star.formula.FormulaProperties.BaseFontHeight
        """
        ...
    @property
    def RelativeFractionBarExcessLength(self) -> int:
        """
        contains the relative excess length of a fraction bar.
        """
        ...
    @property
    def RelativeFractionBarLineWeight(self) -> int:
        """
        contains the relative line weight of a fraction bar.
        """
        ...
    @property
    def RelativeFractionDenominatorDepth(self) -> int:
        """
        contains the relative depth of the denominator of a fraction
        """
        ...
    @property
    def RelativeFractionNumeratorHeight(self) -> int:
        """
        contains the relative height of the numerator of a fraction.
        """
        ...
    @property
    def RelativeIndexSubscript(self) -> int:
        """
        contains the relative superscript of indices.
        """
        ...
    @property
    def RelativeIndexSuperscript(self) -> int:
        """
        contains the relative subscript of indices.
        """
        ...
    @property
    def RelativeLineSpacing(self) -> int:
        """
        contains the relative line spacing.
        """
        ...
    @property
    def RelativeLowerLimitDistance(self) -> int:
        """
        contains the relative distance of lower limits.
        """
        ...
    @property
    def RelativeMatrixColumnSpacing(self) -> int:
        """
        contains the relative column spacing of matrices.
        """
        ...
    @property
    def RelativeMatrixLineSpacing(self) -> int:
        """
        contains the relative line spacing of matrices.
        """
        ...
    @property
    def RelativeOperatorExcessSize(self) -> int:
        """
        contains the relative excess of operators.
        """
        ...
    @property
    def RelativeOperatorSpacing(self) -> int:
        """
        contains the relative spacing of operators.
        """
        ...
    @property
    def RelativeRootSpacing(self) -> int:
        """
        contains the relative root spacing
        """
        ...
    @property
    def RelativeScaleBracketExcessSize(self) -> int:
        """
        contains the relative scaling of the bracket excess.
        """
        ...
    @property
    def RelativeSpacing(self) -> int:
        """
        contains the relative spacing.
        """
        ...
    @property
    def RelativeSymbolMinimumHeight(self) -> int:
        """
        contains the relative minimum height of the formula.
        """
        ...
    @property
    def RelativeSymbolPrimaryHeight(self) -> int:
        """
        contains the relative primary height of symbols.
        """
        ...
    @property
    def RelativeUpperLimitDistance(self) -> int:
        """
        contains the relative distance of upper limits
        """
        ...
    @property
    def RightMargin(self) -> int:
        """
        contains the metric value of the right margin of the formula.
        """
        ...
    @property
    def TopMargin(self) -> int:
        """
        contains the metric value of the top margin of the formula.
        """
        ...


