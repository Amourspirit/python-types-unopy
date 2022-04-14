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
# Namespace: com.sun.star.sdb.application
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class NamedDatabaseObject(object):
    """
    Struct Class

    denotes a named database object, or a named folder of database objects
    
    **since**
    
        OOo 3.0

    See Also:
        `API NamedDatabaseObject <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sdb_1_1application_1_1NamedDatabaseObject.html>`_
    """
    typeName: Literal['com.sun.star.sdb.application.NamedDatabaseObject']

    def __init__(self, Type: typing.Optional[int] = ..., Name: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Type (int, optional): Type value.
            Name (str, optional): Name value.
        """


    @property
    def Type(self) -> int:
        """
        denotes the type of the object.
        
        This member is one of the DatabaseObject or DatabaseObjectContainer constants.
        """


    @property
    def Name(self) -> str:
        """
        denotes the name of the object
        
        In case of forms, reports, form folders and report folders, this is the hierarchical path to the object, where the path elements are separated by a slash (/).
        
        In case of tables, this is the fully qualified name of the table, as required by the database's table name composition rules.
        
        In case of queries, this is the name of the query.
        
        In case of virtual folders denoted by DatabaseObjectContainer.CATALOG and DatabaseObjectContainer.SCHEMA, it is
        
        In case of the virtual folders denoted by DatabaseObjectContainer.TABLES, DatabaseObjectContainer.QUERIES, DatabaseObjectContainer.DATA_SOURCE, DatabaseObjectContainer.FORMS or DatabaseObjectContainer.REPORTS, this denotes the name of the data source (as denoted by com.sun.star.sdb.DataSource.Name)
        """



__all__ = ['NamedDatabaseObject']
