# AutoSTDU - Campus Network Auto Login Tool

[![GitHub Release](https://img.shields.io/github/v/release/9bishi/autostdu)](https://github.com/9bishi/autostdu/releases)
[![GitHub Contributors](https://img.shields.io/github/contributors/9bishi/autostdu)](https://github.com/9bishi/autostdu/graphs/contributors)
[![GitHub Stars](https://img.shields.io/github/stars/9bishi/autostdu?style=social)](https://github.com/9bishi/autostdu)
[![GitHub Watchers](https://img.shields.io/github/watchers/9bishi/autostdu?style=social)](https://github.com/9bishi/autostdu)
[![Downloads](https://img.shields.io/github/downloads/9bishi/autostdu/total)](https://github.com/9bishi/autostdu/releases)

### 项目简介
**AutoSTDU** 是一个用于自动登录石家庄铁道大学校园网的 Python 工具，设计为每天首次开机时自动运行。通过 Edge 浏览器模拟自动化操作，AutoSTDU 在用户端打开浏览器并自动填写用户名和密码，实现无缝校园网登录。

---
### 声明
该项目使用了AI技术。但不得不说，用Chatgpt写小型项目是真方便。
理论上简单类型的校园网均可使用该python脚本，可以直接fork更改。
**欢迎来Star**
## 功能
- 自动化校园网登录
- 支持每天首次开机时自动运行
- 配置文件便捷管理登录信息

## 环境要求
- Python 3.10 或以上版本
- Edge 浏览器/Chrome
## 安装指南
### 一.直接下载release打包好的zip
### 二.自行编译
### 1. 克隆项目
```bash
git clone https://github.com/9bishi/autostdu.git
cd autostdu
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置 `config.ini`
在项目目录下编辑 `config.ini`，填入校园网用户名和密码：

```ini
[login]
username = your_username
password = your_password
```

### 4. 运行程序
执行以下命令以运行程序：
```bash
python campus_login.py
```

### 5. 打包为 EXE 文件
如需打包为 `.exe` 文件，使用以下命令：
```bash
pyinstaller --onefile --windowed --icon=icon.ico campus_login.py
```

---

## 使用说明

1. 将打包后的 `.exe` 文件和 `config.ini` 文件放置在同一目录下。
2. 设置 Windows 任务计划程序，让程序在每天首次开机时自动运行。

### 设置 Windows 任务计划程序
- 在搜索中搜索计算机管理
- 打开“任务计划程序” > 点击“创建基本任务”。
- 设置触发器为“登录时”。
- 操作中选择 `.exe` 文件的路径。
- **一定将起始于这个参数设置为该文件夹的路径，否则无法运行**
---

## 贡献者
感谢所有为本项目贡献的开发者！

[![Contributors](https://contrib.rocks/image?repo=9bishi/autostdu)](https://github.com/9bishi/autostdu/graphs/contributors)

---

## 许可证
本项目遵循 [MIT 许可证](LICENSE)。

---

## 版本历史
查看 [发布版本](https://github.com/9bishi/autostdu/releases) 获取更多更新信息。

---

## 支持
如遇问题或有改进建议，欢迎提交 [issue](https://github.com/9bishi/autostdu/issues)。


