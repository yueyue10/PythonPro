# PythonPro

## Python项目：爬取github的数据
### 项目运行步骤：

> 1. 安装Python应用并将其配置到环境变量中

> 2. 在\configs\DbConfig.py程序中，配置项目连接的MySql数据库，
      在\configs\ComConf.py程序中配置日志保存路径
> 3. 使用\doc\github_data.sql脚本文件"配置"数据库的github_data表
      (具体操作就是使用navicat工具运行脚本文件即可)。
> 4. 安装第三方插件依赖(可以选择配置python虚拟环境防止不同项目第三方插件版本冲突，[查看文档][1])

    ```pip install -r requirements.txt```

> 5. 使用Intellij IDEA运行项目中的\spider\GithubSpider.py程序，
      运行完成即可在查看数据库爬取到的数据

  [1]: https://github.com/yueyue10/PythonPro/blob/master/Python.md


<div>
<h4 align="center">数据库配置</h4>
<img src="https://github.com/yueyue10/PythonPro/raw/master/doc/pic_sql_design.png" width="45%"  />
<img src="https://github.com/yueyue10/PythonPro/raw/master/doc/DbConfig.png" width="45%"  />
<h5 align="center">查看保存到数据库的数据</h5>
<img align="center" src="https://github.com/yueyue10/PythonPro/raw/master/doc/pic_sql.png" width="50%"  />
</div>