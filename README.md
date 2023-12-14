# tiny-zhihu-web

![GitHub Repo stars](https://img.shields.io/github/stars/lunarwhite/tiny-zhihu-web?color=orange)
![GitHub watchers](https://img.shields.io/github/watchers/lunarwhite/tiny-zhihu-web?color=yellow)
![GitHub forks](https://img.shields.io/github/forks/lunarwhite/tiny-zhihu-web?color=green)
![GitHub top language](https://img.shields.io/github/languages/top/lunarwhite/tiny-zhihu-web)
![GitHub License](https://img.shields.io/github/license/lunarwhite/tiny-zhihu-web?color=white)

仿知乎写的 web 社区论坛

更多细节请看 [design doc](https://lunarwhite.notion.site/Web-Design-doc-0caa15a1e6e240e7bf94a51de015b61c) 和 [development doc](https://lunarwhite.notion.site/Web-Dev-doc-46f17ec280d049669b589db9f8dbb02b)

```
.
├── config.py # 配置数据库
├── dbOper.py # 操作数据库
├── env
│   ├── bin
│   ├── include
│   ├── lib
│   ├── lib64 -> lib
│   ├── pyvenv.cfg
│   └── share
├── initdb.sql # 数据库脚本
├── izhihu.ini # 项目初始化
├── izhihu.py # 项目主入口
├── izhihu.sock # 配置 Nginx
├── LICENSE
├── log
│   ├── access.log # 访问日志
│   └── error.log # 错误日志
├── README.md
├── requirements.txt # Python 依赖库
├── static
│   ├── css
│   └── images
├── templates
│   ├── about.html # 关于
│   ├── answer.html # 回答
│   ├── base.html # 父界面
│   ├── changeInfo.html # 修改信息
│   ├── comment.html # 评论
│   ├── error.html # 提示错误
│   ├── index.html # 主界面
│   ├── login.html # 登录
│   ├── question.html # 问题
│   ├── regist.html # 注册
│   └── user.html # 用户个人
└── wsgi.py
```

## 1 Overview

- Ubuntu Server `18.04`
- SQL Server `2019 (RTM-CU10)`
- Python `3.6.9`
- Flask `1.1.2`
- Nginx `1.14.0 (Ubuntu)`

## 2 Setup

- clone repo：`git clone https://github.com/lunarwhite/tiny-zhihu-web.git`
- 更新 pip：`pip3 install --upgrade pip`
- 为项目创建虚拟环境：`conda create --name <env_name> python=3.6`
- 激活 env：`conda activate <env_name>`
- 安装 Python 库依赖：`pip3 install -r requirements.txt`
- 数据库创建：执行 `initdb.sql` SQL 脚本

## 3 Deploy

- 数据库连接：修改 `config.py` 文件参数
  ```python
  HOSTNAME = '127.0.0.1' # 主机内网 ip
  PORT     = '1433' # 端口
  DATABASE = 'izhihu' # 数据库名称
  USERNAME = 'sa' # 用户名
  PASSWORD = <password> # 密码
  ```
- 刷新 Nginx
  ```bash
  sudo systemctl restart nginx
  ```
- 启动 uwsgi
  ```python
  uwsgi izhihu.ini
  ```

## 4 Reference

- [Flask Tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask)
- [Python SQL 驱动程序 - pymssql](https://docs.microsoft.com/zh-cn/sql/connect/python/pymssql/python-sql-driver-pymssql?view=sql-server-ver15)
- [快速入门：安装 SQL Server 并在 Ubuntu 上创建数据库](https://docs.microsoft.com/zh-cn/sql/linux/quickstart-install-connect-ubuntu?view=sql-server-ver15)
- [使用 Windows 上的 SQL Server Management Studio 管理 Linux 上的 SQL Server](https://docs.microsoft.com/zh-cn/sql/linux/sql-server-linux-manage-ssms?view=sql-server-ver15)
- [Nginx 服务器 SSL 证书安装部署](https://cloud.tencent.com/document/product/400/35244)
