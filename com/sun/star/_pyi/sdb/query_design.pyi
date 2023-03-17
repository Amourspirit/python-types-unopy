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
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdb
from ..frame.x_controller import XController as XController_b00e0b8f
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca

class QueryDesign(XController_b00e0b8f, XInitialization_d46c0cca):
    """
    Service Class

    implements a component which allows the creation of SQL statements.
    
    This service implements a user interface for creating SQL statements either through a graphical design interface or simply to enter the SQL statement directly.
    
    The design view of the QueryDesign is divided into two parts. The first part contains the table windows where columns can be selected for the SQL statement. The second part contains the columns which should appear in the selection of the SQL statement or criteria which narrow the query.
    
    A QueryDesign component has 3 operation modes, which control what kind of object is edited:
    
    Initialization is done using the com.sun.star.lang.XInitialization interface, which expects a sequence of objects being either com.sun.star.beans.NamedValues or com.sun.star.beans.PropertyValues. The following parameters are supported at initialization time:
    
    There's a number of legacy settings which are recognized for compatibility reasons, though you're discouraged from using them:
    
    **since**
    
        OOo 2.4

    See Also:
        `API QueryDesign <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1QueryDesign.html>`_
    """
    @property
    def ActiveCommand(self) -> str:
        """
        reflects the designed SQL command at the moment it was last saved by the user.
        """
        ...
    @property
    def EscapeProcessing(self) -> bool:
        """
        specifies whether the user enabled escape processing for the statement being designed.
        
        **since**
        
            OOo 2.4
        """
        ...

