# Python相关命令

### 查看安装的Python插件

> pip list

### 生成安装的第三方插件requirements.txt

 > 1. pip freeze >requirements.txt
生成python环境安装的插件列表的cmd命令
 > 2. 在当前cmd命令所在目录(默认是C:\Users\zhaoyuejun)下会生成requirements.txt的文本文档

### virtualenv虚拟环境配置：

> 1.安装虚拟环境 pip install virtualenv
> 2.创建一个独立环境 virtualenv myenv
> 3.进入myenv的Scripts文件夹中，输入activate来激活环境
> 4.使用deactivate退出

### 集中式虚拟环境管理工具：

> 1.安装工具命令(window环境) pip install virtualenvwrapper-win
> 1.1 在环境变量中配置( WORKON_HOME是虚拟环境的目录地址)：
> WORKON_HOME：E:\Users\Python\Libs
> 2.快速创建虚拟环境并激活 mkvirtualenv venv1
> 3.快速在多个虚拟环境中切换 workon venv2
> 4.快速关闭虚拟环境 deactivate
> 5.快速删除虚拟环境 rmvirtualenv PythonPro
> 6.查看所有创建的虚拟环境 lsvirtualenv

### 配置好虚拟环境以后需要给项目设置对应的虚拟环境，具体方法如下图所示：

<div>
<h4 align="center">配置好的虚拟环境</h4>
<img src="https://github.com/yueyue10/PythonPro/raw/master/doc/virtualenv_.png" width="60%"  />
<h4 align="center">项目配置虚拟的python环境</h4>
<img src="https://github.com/yueyue10/PythonPro/raw/master/doc/project_settings.png" width="45%"  />
<img src="https://github.com/yueyue10/PythonPro/raw/master/doc/virtualenv_setting.png" width="45%"  />
</div>