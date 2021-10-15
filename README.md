# list_table_sql-py
使用python命令获得sql中的所有表或视图名称  
get all table's or view's name from a sql

这个程序及其所使用的文件基于antlr4(v4.8) 和 grammar-v4 构建  
this program and requirements was based on antlr4(v4.8) and grammar-v4 

https://github.com/antlr/antlr4    
https://github.com/antlr/grammars-v4/tree/master/sql/plsql

你可以使用它从一个合法的sql脚本中获得其表和视图名称得清单  
you can use it to get a list of table’s and view's name  from a legal sql_script  

在使用前，你必须先安装 "antlr4-python3-runtime"   
before use it ,you must install "antlr4-python3-runtime"  

```bat
pip install antlr4-python3-runtime  
```
然后下载本仓库的所有文件并解压  
and then download the folder of list_table_sql-py and unzip it

现在，可以开始使用了  
now ,enjoy like this :  

```python
from  list_table_sql import list_table_sql as t
print (t('{"sql":"select abc from def,ghi j,k.lmn o","mode":"P"}'))
print (t('{"sql":"select abc from def,ghi j,k.lmn o","mode":"T"}'))
```

{"position": [["16", "18"], ["20", "22"], ["26", "30"]]}  

{'tablename': ['def', 'ghi', 'k.lmn']}  


the "mode" parameter defined:  
- T-table_list  
- P-table_position  
