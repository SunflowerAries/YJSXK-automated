## 环境配置

**本项目仅在 Ubuntu 20.04 环境下验证通过，其他环境尚未验证功能是否完整**
运行本项目前请先确认本地是否安装 python 环境及 pip

```bash
sudo apt-get install python-pip
```
pip 安装后请下载项目所需依赖包
```bash
pip install lmdb torch torchvision filelock beautifulsoup4 lxml
```
以及 OpenCV 
```bash
sudo apt-get install python3-opencv
```

```
git clone git@github.com:SunflowerAries/yjsxk-automated.git
cd yjsxk-automated
git submodule update --init
```

从 [Baidu Netdisk](https://pan.baidu.com/s/1pLbeCND) 下载预训练模型到 `crnn/data` 文件夹下

## 功能配置

本脚本所有配置项均可以在 `config.py` 中配置，

- 其中 1-2 行 `uid` 和 `psw` 对应你的学号，密码（学号、密码本地保留，所有代码均已开源、可审计）。

- 第 4 行 `sleep_time` 为刷新频率，单位为秒

- 15-22 行 `yjsxk_wanted_class` 为你想抢的课程，例如如下配置表示希望抢政治理论课模块下的《自然辨证法概论》，学位基础课模块下的《神经网络与深度学习》、《高级数据库》，其他可选课模块下的《前沿网络技术》

  ```python
  yjsxk_wanted_class = { '政治理论课': ['自然辨证法概论'],
                          '第一外国语': [],
                          '专业外语': [],
                          '学位基础课': ['神经网络与深度学习', '高级数据库'],
                          '学位专业课': [],
                          '专业选修课': [],
                          '公共选修课': [],
                          '其他可选课': ['前沿网络技术'] }
  ```

- 24 行 `qtxxk_dept` 对应其他可选课程中开课院系，一般与自己所属院系对应

  <img src="pics/dept.png">

- 其他配置信息不影响用户使用本脚本，如果希望进一步了解剩余配置信息或对本项目实现感兴趣可参考[实现文档](docs/项目实现.md)

## 运行项目

完成上述操作后，即可运行脚本自动帮你抢课（从此可以安心入睡

```
python3 main.py
```

请确认屏幕中显示 `已进入选课模式`，若出现常见错误 1 则按指示进行操作

## 常见报错

- 出现如下报错则说明多次识别验证码错误，需要等待 5 分钟方可选课。

  ```bash
  Traceback (most recent call last):
    File "XXX/main.py", line 145, in <module>
      yjsxk_fudan.login()
    File "XXX/main.py", line 86, in login
      resp = json.loads(post.text)
    File "/usr/lib/python3.9/json/__init__.py", line 346, in loads
      return _default_decoder.decode(s)
    File "/usr/lib/python3.9/json/decoder.py", line 337, in decode
      obj, end = self.raw_decode(s, idx=_w(s, 0).end())
    File "/usr/lib/python3.9/json/decoder.py", line 355, in raw_decode
      raise JSONDecodeError("Expecting value", s, err.value) from None
  json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
  ```

- 如果出现其他错误请通过本项目下的 github issue 告知开发者，或发送邮件至 sunflowerinaries@gmail.com，并附上报错信息截图及必要的文字说明。

## 后续方向

- 完善文档
- 提升模型性能
- 将整个项目打包成 docker，做到简单配置即可使用

## 说明

- 本项目仅供复旦大学研究生选课或（其他对自动化选课脚本感兴趣的人）学习，不得用于任何商业目的。

- 当前脚本通过 [rcnn](https://github.com/SunflowerAries/crnn.pytorch) 识别验证码完成登陆，受模型自身能力限制，可能会出现连续多次（大约 20 次）尝试失败。此时选课系统提醒登陆失败，按照提示间隔 5 分钟重新运行脚本即可。

  <img src="pics/error.png" width=30%>

- 如果你想支持本项目，

  - 在 dataset 下创建一个文本文件 **code.txt**，将 dataset 中未识别成功的图片按顺序逐个标注，完成后将 dataset 文件夹打包发送到 sunflowerinaries@gmail.com，或者在 [rcnn](https://github.com/SunflowerAries/crnn.pytorch) 项目下提出 PR 直接添加数据—— `alldata` 下为训练集图片，`alldata-val` 下为测试集图片，`log-train` 为训练集对应标签，`log-val` 为测试集对应标签
  - 提出更好的模型，并利用 [rcnn](https://github.com/SunflowerAries/crnn.pytorch) 项目下的 `alldata（训练集）` 和 `alldata-val（测试集）` 进行测试，当前模型的正确率大约为 13%。

  
