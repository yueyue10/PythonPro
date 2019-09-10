# save-log
项目介绍

## Python项目：将指定目录下的log日志保存到数据库

> 此项目还包含一个对时间的处理工具类 [DateUtils][1]

### 项目运行步骤：

* 配置数据库
    * 在configs/DbConfig.py里面配置数据库
    * 使用doc/logs.sql文件在数据库新建数据表logs
* 运行SaveLogs.py程序
    * 配置扫描log文件的路径path
    * 运行SaveLogs.py程序的main方法

<div>
<h4 align="center">数据库配置</h4>
<img src="https://github.com/yueyue10/PythonPro/blob/master/save-log/doc/db_logs.png" width="45%"  />
<img src="https://github.com/yueyue10/PythonPro/blob/master/save-log/doc/db_logs0.png" width="45%"  />

<h5 align="center">查看保存到数据库的数据</h5>
<img src="https://github.com/yueyue10/PythonPro/blob/master/save-log/doc/db_logs1.png" width="45%"  />
<img src="https://github.com/yueyue10/PythonPro/blob/master/save-log/doc/db_logs2.png" width="45%"  />
</div>

[1]:https://github.com/yueyue10/PythonPro/blob/master/save-log/utils/DateUtils.py