#!/usr/bin/env python
#coding=utf-8
#功能 ：获取sql中的所有表和视图名
#日期 ：2021-10-15 
#作者：Dark-Athena
#EMAIL:darkathena@qq.com
"""
Copyright DarkAthena(darkathena@qq.com)
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import os
import re,json
from antlr4 import *
#file_name=r'test.sql'
tb_list=[]
grammar='PlSql'
start_rule='sql_script'

def get_table_position( node):
    if isinstance(node, ParserRuleContext):
        class_name = str(type(node))
        if str(class_name)=="<class 'PlSqlParser.PlSqlParser.Tableview_nameContext'>":
            tb_list.append([re.split(r'[,:]',str(node.start))[1],re.split(r'[:=]',str(node.stop))[1]])
    if hasattr(node, 'children'):
        for child in getattr(node, 'children'):
            get_table_position(child)

def get_table(i_sql):
    lexerName = grammar + 'Lexer'
    parserName = grammar + 'Parser'
    module_lexer = __import__(lexerName, globals(), locals(), lexerName)
    class_lexer = getattr(module_lexer, lexerName)
    module_parser = __import__(parserName, globals(), locals(), parserName)
    class_parser = getattr(module_parser, parserName)
    #input_stream = FileStream(file_name)
    input_stream = InputStream(i_sql.upper())
    lexer = class_lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    parser = class_parser(token_stream)
    parser.buildParseTrees = True
    func_start_rule = getattr(parser, start_rule)
    parser_ret = func_start_rule()
    return parser_ret


def list_table_sql(i_data):
    global tb_list
    tb_list=[]
    ret={}
    json_data = json.loads(i_data)
    if 'sql' not in json_data:
        ret['msg']=["sql is not defined!"]
        return ret
    i_sql=json_data['sql']
    i_mode=json_data['mode']
    get_table_position(get_table(i_sql))
    
    if i_mode=='P':
        ret['position'] =tb_list
    elif i_mode=='T':
        ret['tablename']=[str(i_sql)[int(i[0]):int(i[1])+1] for i in tb_list]
    else:
        ret['msg']=["mode "+i_mode+" is not defined!"]
    return ret
    

