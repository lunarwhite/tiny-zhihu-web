# tiny-zhihu-web

![tiny-zhihu-web](https://socialify.git.ci/lunarwhite/tiny-zhihu-web/image?description=1&descriptionEditable=%E4%BB%BF%E7%85%A7%E7%9F%A5%E4%B9%8E%E5%86%99%E7%9A%84web%E8%AE%BA%E5%9D%9B%E7%B3%BB%E7%BB%9F%EF%BC%8C%E5%90%8E%E7%AB%AF%E9%80%89%E6%8B%A9%E7%AE%80%E6%98%93%E7%9A%84flask%2Bpython%EF%BC%8C%E5%89%8D%E7%AB%AF%E9%80%89%E6%8B%A9jQuery%EF%BC%8C%E6%95%B0%E6%8D%AE%E5%BA%93%E9%80%89%E6%8B%A9SQL-Server%EF%BC%8C%E9%83%A8%E7%BD%B2%E5%88%B0Ubuntu%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A&font=Raleway&forks=1&issues=1&language=1&logo=https%3A%2F%2Fflask.palletsprojects.com%2Fen%2F2.0.x%2F_images%2Fflask-logo.png&owner=1&pattern=Plus&pulls=1&stargazers=1&theme=Light)

> 设计文档[在这里](https://lunarwhite.github.io/zh/dev/2assign/fvrltijkh/)，开发文档[在这里](https://lunarwhite.github.io/zh/dev/2assign/o7m0xddlu/)
>
> 欢迎交流拍砖~

```
.
├── config.py # 配置数据库
├── dbOper.py # 操作数据库
├── env # 环境
│   ├── bin
│   ├── include
│   ├── lib
│   ├── lib64 -> lib
│   ├── pyvenv.cfg
│   └── share
├── initdb.sql # 数据库脚本
├── izhihu.ini # 项目初始化
├── izhihu.py # 项目主入口
├── izhihu.sock # 配置Nginx
├── LICENSE # 开源条款
├── log # 日志文件
│   ├── access.log # 访问日志
│   └── error.log # 错误日志
├── README.md # 说明文件
├── requirements.txt # python依赖库
├── static # 前端css文件、img文件
│   ├── css
│   └── images
├── templates # HTML文件
│   ├── about.html # 关于
│   ├── answer.html # 回答界面
│   ├── base.html # 父界面，由其他界面继承
│   ├── changeInfo.html # 修改信息界面
│   ├── comment.html # 评论界面
│   ├── error.html # 提示错误界面
│   ├── index.html # 主界面
│   ├── login.html # 登陆界面
│   ├── question.html # 问题界面
│   ├── regist.html # 注册界面
│   └── user.html # 用户个人界面
└── wsgi.py # 运行

12 directories, 27 files
```

## 1 概览

- 工具链
  - Ubuntu-Server 18.04
  - SQL-Server 2019 (RTM-CU10)
  - VSCode 1.55
  - Git 2.17.1
  - Python 3.6.9
  - Flask 1.1.2
  - Nginx 1.14.0 (Ubuntu)

## 2 部署

- 克隆repo：`git clone https://github.com/lunarwhite/tiny-zhihu-web.git`
- 更新pip：`pip3 install --upgrade pip`
- 为项目创建虚拟环境：`conda create --name <env_name> python=3.6`
- 激活env：`conda activate <env_name>`
- 安装python库依赖：`pip3 install -r requirements.txt`
- 数据库创建：可以用

## 3 启动

- 数据库连接：修改`config.py`文件的参数

  ```python
  HOSTNAME = '127.0.0.1' # 主机内网ip
  PORT     = '1433' # 端口
  DATABASE = 'izhihu' # 数据库名称
  USERNAME = 'sa' # 用户名
  PASSWORD = <password> # 密码
  ```

- 刷新Nginx

  ```bash
  sudo systemctl restart nginx
  ```

- 启动uwsgi

  ```python
  uwsgi izhihu.ini
  ```

## 4 后续

- todo：打包程序，方便部署
- todo：软件测试，结合软工
- todo：前端UI美化，迁移框架
- todo：提高系统健壮性、网页运行安全性

## 5 参考
- [Nginx 服务器 SSL 证书安装部署](https://cloud.tencent.com/document/product/400/35244)
- [快速入门：安装 SQL Server 并在 Ubuntu 上创建数据库](https://docs.microsoft.com/zh-cn/sql/linux/quickstart-install-connect-ubuntu?view=sql-server-ver15)
- [使用 Windows 上的 SQL Server Management Studio 管理 Linux 上的 SQL Server](https://docs.microsoft.com/zh-cn/sql/linux/sql-server-linux-manage-ssms?view=sql-server-ver15)
- [Python SQL 驱动程序 - pymssql](https://docs.microsoft.com/zh-cn/sql/connect/python/pymssql/python-sql-driver-pymssql?view=sql-server-ver15)
- [Flask Tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask)
