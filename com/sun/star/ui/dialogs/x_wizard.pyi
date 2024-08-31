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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.ui.dialogs
from __future__ import annotations
import typing

from .x_executable_dialog import XExecutableDialog as XExecutableDialog_450f0fa1
if typing.TYPE_CHECKING:
    from ...awt.x_window import XWindow as XWindow_713b0924
    from .x_wizard_page import XWizardPage as XWizardPage_ed7c0d3d


class XWizard(XExecutableDialog_450f0fa1):
    """
    is the main interface implemented by the Wizard services.
    
    A wizard is a dialog which guides the user through a number of tasks (usually input of data), which the user can accomplish either sequentially or out-of-order. For this, a wizard is comprised of a number of tab pages, each page representing a single step.
    
    Sequential navigation in a wizard is done via a Next and a Back button. Non-sequential navigation is done via a roadmap, which is displayed on the left hand side of the wizard dialog, lists all available steps, and allows jumping to a certain step (where the creator of the wizard can restrict the available steps depending on the current situation in the wizard, see below).
    
    A sequence of steps in a wizard dialog is called a path. A given wizard can support one or multiple paths, which are declared at the time of construction of the wizard.
    
    In the simplest case, where the wizard supports only one path, all available steps are displayed in the roadmap, and the user can simply travel through them as desired.
    
    If the wizard is more complex, and supports multiple paths, things become more complicated. In a given situation of the wizard, where the user is at step k of the current path, the potential or conflicting paths are those whose first k steps are the same as in the current path. Obviously, there's at least one potential path in every situation: the current one. If there is more than one, then the future steps in the dialog are not finally decided. In such a case, the roadmap will display future steps up to the point where the potential paths diverge, and then an item ... indicating that the order of steps is undecided.
    
    An XWizardController can declare a certain path as active path by calling the activatePath() method. Usually, this is done depending on user input. For instance, your wizard could have radio buttons on the first page which effectively decide about which path to take in the wizard.
    
    Single steps in the wizard can be freely enabled and disabled, using the enablePage() method. Disabled pages are skipped during sequential traveling, and not selectable in the roadmap.
    
    The state of the Next button in the dialog will be automatically maintained in most situations, depending on the results of calls to the XWizardController.canAdvance() and XWizardPage.canAdvance() methods. More sophisticated wizard logic, however, will need manual calls to the enableButton() method. Also, the Finish button needs to be maintained by the wizard's controller, too, as it cannot be decided generically in which situations it should be enabled or disabled.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XWizard <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1XWizard.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.ui.dialogs.XWizard'

    def activatePath(self, PathIndex: int, Final: bool) -> None:
        """
        activates a path
        
        If the wizard has been created with multiple paths of control flow, then this method allows switching to another path.
        
        You can only activate a path which shares the first k pages with the path which is previously active (if any), where k is the index of the current page within the current path.
        
        Example: Say you have paths, (0,1,2,5) and (0,1,4,5) (with the numbers denoting page IDs). This means that after page 1, you either continue with page 2 or state 4,and after this, you finish in state 5.Now if the first path is active, and your current state is 1, then you can easily switch to the second path, since both paths start with (0,1).However, if your current state is 2, then you can not switch to the second path anymore.
        
        If TRUE, the path will be completely activated, even if it is a conflicting path (i.e. there is another path which shares the first k states with the to-be-activated path.)
        
        If FALSE, then the new path is checked for conflicts with other paths. If such conflicts exists, the path is not completely activated, but only up to the point where it does not conflict.
        
        In this latter case, you need another activatePath method (usually triggered by the user doing some decisions and entering some data on the reachable pages) before the wizard can actually be finished.
        
        With the paths in the example above, if you activate the second path, then only steps 0 and 1 are activated, since they are common to both paths. Steps 2, 4, and 5 are not reachable, yet.

        Raises:
            : ````
            com.sun.star.util.InvalidStateException: ``InvalidStateException``
        """
        ...
    def advanceTo(self, PageId: int) -> bool:
        """
        advances to the given page, if possible.
        
        Calling this method is equivalent to the user repeatedly pressing the Next button, until the given page is reached. Consequently, the method will fail if one of the intermediate pages does not allow advancing to the next page.
        """
        ...
    def enableButton(self, WizardButton: int, Enable: bool) -> None:
        """
        enables or disables a certain button in the wizard
        
        Normally, you will want to use this method for the Finish button only: The Next and Back buttons are usually maintained automatically, the Help and Cancel buttons are unlikely to ever being disabled.
        """
        ...
    def enablePage(self, PageID: int, Enable: bool) -> None:
        """
        enables or disables the given page
        
        You can use this method when not all pages of your wizard are necessarily needed in all cases. For instance, assume that your first wizard page contains a check box, which the user can check to enter additional data. If you place this data on the second page, then you will want to enable this second page if and only if the checkbox is checked.
        
        If a page is disabled, it can reached neither by clicking the respective item in the wizard's roadmap, nor by sequential traveling. Still, the page's item is displayed in the roadmap, though disabled.

        Raises:
            : ````
            com.sun.star.util.InvalidStateException: ``InvalidStateException``
        """
        ...
    def getCurrentPage(self) -> XWizardPage_ed7c0d3d:
        """
        provides access to the current page of the wizard
        """
        ...
    def goBackTo(self, PageId: int) -> bool:
        """
        goes back to the given page, if possible.
        
        Calling this method is equivalent to the user repeatedly pressing the Back button, until the given page is reached.
        """
        ...
    def setDefaultButton(self, WizardButton: int) -> None:
        """
        sets a button in the wizard as default button
        
        In general, the default button in a wizard is the one which is activated when the user presses the return key while the focus is in a control which does not handle this key itself (such as ordinary input controls).
        
        You can use this method, for instance, to make the Next button the default button on all pages except the last one, where Finish should be defaulted.
        """
        ...
    def travelNext(self) -> bool:
        """
        travels to the next page, if possible
        
        Calling this method is equivalent to the user pressing the Next button in the wizard. Consequently, the method will fail if in the current state of the wizard, it is not allowed to advance to a next page.
        """
        ...
    def travelPrevious(self) -> bool:
        """
        travels to the next page, if possible
        
        Calling this method is equivalent to the user pressing the Back button in the wizard.
        """
        ...
    def updateTravelUI(self) -> None:
        """
        updates the wizard elements which are related to traveling.
        
        For instance, the Next button is disabled if the current page's XWizardPage.canAdvance() method returns FALSE.
        
        You usually call this method from within a wizard page whose state changed in a way that it affects the user's ability to reach other pages.
        """
        ...

    @property
    def DialogWindow(self) -> XWindow_713b0924:
        """
        """
        ...
    @DialogWindow.setter
    def DialogWindow(self, value: XWindow_713b0924) -> None:
        ...
    @property
    def HelpURL(self) -> str:
        """
        is the help URL of the wizard's main window.
        """
        ...
    @HelpURL.setter
    def HelpURL(self, value: str) -> None:
        ...

