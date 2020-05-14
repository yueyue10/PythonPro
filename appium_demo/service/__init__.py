"""
启动appium服务模块
"""

print("service 模块初始化")

desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    # 'deviceName': 'emulator-5554',
    'deviceName': '3SC7N16B07000927',
    'platformVersion': '8.0',
    'appPackage': 'com.ennova.dreamlf',
    'appActivity': 'com.ennova.dreamlf.module.main.splash.SplashActivity',
    'noReset': "True",
    'autoGrantPermissions': "True",
    'launchTimeout': "2000",  # 假设它挂起和失败会话之前以ms毫秒为单位等待仪器的时间
    'deviceReadyTimeout': "2",  # 在等待设备准备就绪的几秒钟内超时
    'androidDeviceReadyTimeout': "2",  # 用于等待设备在启动后准备就绪的秒数
    'androidInstallTimeout': "2000",  # 用于等待apk安装到设备的超时（以毫秒为单位）。默认为90000
    'avdLaunchTimeout': "2000",  # avd启动并连接到ADB需要多长时间（默认值120000）
    'avdReadyTimeout': "2000",  # avd完成启动动画需要多长时间（默认120000）
    'newCommandTimeout': "320"  # 在假定客户端退出并结束会话之前，Appium将等待来自客户端的新命令（以秒为单位）
}

douyin_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator1',
    # 'deviceName': 'emulator-5555',
    # 'deviceName': '3SC7N16B07000927',
    # 'platformVersion': '8.0',
    'deviceName': '5705b13e',
    'platformVersion': '7.1.2',
    'appPackage': 'ctrip.android.view',
    'appActivity': 'ctrip.business.splash.CtripSplashActivity',
    'noReset': "True",
    'autoGrantPermissions': "True",
    'launchTimeout': "1999",  # 假设它挂起和失败会话之前以ms毫秒为单位等待仪器的时间
    'deviceReadyTimeout': "1",  # 在等待设备准备就绪的几秒钟内超时
    'androidDeviceReadyTimeout': "1",  # 用于等待设备在启动后准备就绪的秒数
    'androidInstallTimeout': "1999",  # 用于等待apk安装到设备的超时（以毫秒为单位）。默认为90000
    'avdLaunchTimeout': "1999",  # avd启动并连接到ADB需要多长时间（默认值120000）
    'avdReadyTimeout': "1999",  # avd完成启动动画需要多长时间（默认120000）
    'newCommandTimeout': "319",  # 在假定客户端退出并结束会话之前，Appium将等待来自客户端的新命令（以秒为单位）
    'unicodeKeyboard': 'True'  # 使用默认键盘
}


class AppConfig:
    element_path = "ctrip.android.view"
    phone_num = "18810126510"
    service_path = 'http://127.0.0.1:4723/wd/hub'

# aapt dump badging E:\Users\AS_Project\tibetoperation\app\release\release.apk
# aapt dump badging E:\Users\AS_Project\tibetoperation\app\release\122.apk
# ctrip.android.view
# ctrip.business.splash.CtripSplashActivity
# com.squareup.leakcanary.internal.DisplayLeakActivity
