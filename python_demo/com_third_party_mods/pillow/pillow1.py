from PIL import Image, ImageFilter

print('''---------------------Pillow---------------------
''')

# PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。

# *********** 操作图像 ***********

# 来看看最常见的图像缩放操作，只需三四行代码：
#
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w // 2, h // 2))
print('Resize image to: %sx%s' % (w // 2, h // 2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')

# 应用模糊滤镜:
im2 = Image.open('test.jpg')
im3 = im2.filter(ImageFilter.BLUR)
im3.save('blur.jpg', 'jpeg')
