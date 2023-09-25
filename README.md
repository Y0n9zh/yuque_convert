- 最近也是遇到了语雀图片上传阿里 OSS 报错的问题，找了一个大佬的工具感觉不错简单修改一下代码。
- 原版工具地址（感谢大佬）：https://github.com/misaki7in/yuque

# Tool introduction

- 语雀导出的 `Markdown` 格式的文档，无法利用 `Hexo`、`CSDN` 对其渲染。主要是因为语雀含有防盗链机制，导致图片无法加载上传。
- 该脚本可以批量获取语雀中 `Markdown` 中的图片链接，将其自动下载到脚本的同级目录的 `image` 目录下，并生成新的 `md` 文档，替换掉原有的图片链接。

> 注：替换图片链接的功能需要自己将下载后的图片上传至指定图床（OSS），或者自己的 Web 服务器上，并且文件名称不要改变，本工具不会自动帮你上传文件。
>

# Tool use
> 注：Python 版本使用的是 Python 3。

- 安装 `Python` 运行库：

```shell
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
```

- 执行脚本文件，输入新的 `OSS` 或 `WebServer` 路径，注意后面要加`/`：

![image-20230925145717974](http://yongz-typro.oss-cn-beijing.aliyuncs.com/img/image-20230925145717974.png)

- 如下所示，生成 `images` 目录，里面含有下载的图片，并且目录下生成了对应的 `_new` 文件：

![image-20230925150354801](http://yongz-typro.oss-cn-beijing.aliyuncs.com/img/image-20230925150354801.png)

- 比较新文档和原文档，可以发现图片链接已经自动改变：

![image-20230925150206402](http://yongz-typro.oss-cn-beijing.aliyuncs.com/img/image-20230925150206402.png)
