在create table 的时候用 nvarchar 才能显示Unicode Character包括中文

用python建立链接, 在config 中必须加上'charset':'utf8'才能显示中文

python 执行语句必须cnx.commit()， 在SQLyog 中不需要

如果有string input，比如下面第二个variable 是string type
	`cursor.execute("INSERT INTO top250 VALUES (%s, %s,%s)", row)` 或者
	`cursor.execute("INSERT INTO top250 VALUES (%s, '%s',%s)"%row)`

一些有用的语句：
- truncate tablename 清空
- update tablename 




