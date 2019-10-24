# 下载抖音视频的工具类
可以下载抖音用户上传的视频，以及收藏的视频
down.py里面新增判断视频已经下载就不再请求视频下载地址以及下载文件操作

运行过程：
---
> 这些功能都是在[参考地址][1]里面研究，得到的成果
> 
> 整体的思路:使用 Chrome DevelopTools 调试抖音个人中心网页版的接口，获取接口的参数和返回值。
>> 使用python模拟user-agent为浏览器的请求，爬取接口数据并下载视频。
>> 
>> 抖音个人中心网页版地址：https://www.iesdouyin.com/share/user/104713356413 {id:104713356413是我的抖音网页版id，获取方式在下面的步骤里面即m_user_id}

* 运行videos.py得到视频的id和名称** 里面有些参数不同用户是有区别的 **
    * m_user_id 是在抖音个人中心网页版下的id。获取方式为：用户使用抖音APP分享自己的个人链接，在浏览器复制打开就可以找到
    * 其他参数：_dytk、cursors、aid可以通过Chrome浏览器Developer Tools获取到，个人测试是不变的，videos.py里面也有描述
    * m_signstr、Cookie也可以从浏览器获取但有时效性，可能是几分钟吧。
    ![ic_tk_html.png](https://github.com/yueyue10/PythonPro/blob/master/appium_demo/doc/ic_tk_html.png?raw=true)
    ![ic_videos.png](https://raw.githubusercontent.com/yueyue10/PythonPro/master/appium_demo/doc/ic_videos.png)
* 运行down.py下载视频** 里面有些参数不同用户是有区别的 **
    * PreDownload._reg_video_url里面的mid是测试发现分享其他的视频用同一个即可。也因为这个的原因导致一部分视频的分享地址错误
    * DownloadRobot.m_save_path里面定义视频下载地址
    ![ic_down.png](https://github.com/yueyue10/PythonPro/blob/master/appium_demo/doc/ic_down.png?raw=true)
    ![ic_down_videos.png](https://github.com/yueyue10/PythonPro/blob/master/appium_demo/doc/ic_down_videos.png?raw=true)

> 其中遇到的问题：
>
> 使用多线程下载视频时(20个线程同时下载视频)，只有第一个视频是正常的，其他视频都出现问题了。
    * 解决方法：去掉下载视频方法中的断点续传

    
文件夹说明：
---
* helper_txt下是前期研究的文件，包括抖音接口测试及数据返回等。
* test下是从网上找的“使用python下载抖音视频”的一些方法[参考地址][1]
* down_text下是网上找的多线程下载文件的方法(这里实际上没用到)

[1]:https://blog.csdn.net/fei347795790/article/details/96432139
[2]:http://3g.gljlw.com/diy/douyin.php