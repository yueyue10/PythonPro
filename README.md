# PythonPro

### python项目：爬取github的数据
### 项目运行步骤：
> * 1.安装Python应用并将其配置到环境变量中
> * 2.在\configs\DbConfig.py程序中，配置项目连接的MySql数据库，
      在\configs\ComConf.py程序中配置日志保存路径
> * 3.使用\doc\github_data.sql文件配置数据库的github_data表
> * 4.使用Intellij IDEA运行项目中的\spider\GithubSpider.py程序，
      运行完成即可在查看数据库爬取到的数据

<div>
<h5align="center">数据库配置</h5>
<img src="https://github.com/yueyue10/PythonPro/raw/master/doc/pic_sql_design.png" width="100%"  />
<img src="https://github.com/yueyue10/PythonPro/raw/master/doc/DbConfig.png" width="100%"  />
<h5 align="center">查看保存到数据库的数据</h5>
<img src="https://github.com/yueyue10/PythonPro/raw/master/doc/pic_sql.png" width="100%"  />
</div>