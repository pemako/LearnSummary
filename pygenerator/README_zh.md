# Pemako Python  项目生成器

[![GitHub stable](https://img.shields.io/badge/pygenerator-stable1.0.1-green.svg)](https://github.com/pemako/pygenerator/archive/v1.0.1.zip)

[英文目录](README.md)

使用脚本和项目模板自动生成一些有用的服务模型

## 依赖

必须安装软件 `rename`,`git`, `python`,`sed`,`gsed`

## 快速开始
使用 `pygen.sh` 创建自己的项目.

## 项目说明 
#### 1. 目录树
	
生成的项目结构如下:
		
    <your_project_name>
    |-bin
    |	\-<your_project_name>.sh --- script to start/stop/restart service |-conf
    |	|-<your_project_name>_logging.cfg --- main logging config file
    |	|-<your_project_name>_service.cfg --- service default config file
    |	\-<your_project_name>_worker_logging.cfg --- worker logging config file
    |-lib --- the same as "src", which you can put all your own source code in
    |	|-<your_project_name>.py --- config, logging and serivce import
    |	\-<your_project_name>_service.py --- implements your own functions
    \-build.sh --- build the project into rpm package

#### 2. 控制脚本
	
在生成项目的 `bin` 目录中有 `<your_project_name>.sh` 脚本文件，你可以如下使用
	
	<your_project_name>.sh [-d EXECUTION_PATH] {start|stop|restart|status}
			
脚本实际启动的 `lib/<your_project_name>.py` 的服务文件

#### 3. 打包脚本

在根目录下使用`build.sh`进行服务打包，运行会在生成如下的文件

	target/<your_project_name>-0.0.1-1.x86_64.rpm
	target/<your_project_name>-0.0.1.tar.gz"
	
`tar` 包供您在线下测试，rpm 包在线上服务部署（如果项目是使用 `puppet` 管理的）
	
#### 4. 日志配置
	
PYGEN 使用标准日志模块实现日志记录。所有的配置都都放置在`conf/` 目录中
	
默认日志按照小时级别切割，如下
	
	log/hourly/<your_project_name>.log

如果使用多进程模式，你不必担心"Logging into single file from multi-process", 项目的框架会进行处理它。主进程中只有一个线程记录日志文件，而其他进程只是通过套接字将它们的日志记录发送到这个线程。因此，只有一个线程会进行日志切割。
	
#### 5. 服务配置
	
PYGEN 使用 "ConfigParser" 实现配置加载。默认的配置文件如下
	
	conf/<your_project_name>_service.cfg

在这里您可以设置工作数量、主日志记录端口(从其它进程接收日志记录)、server 端口和数据库配置等。

	
#### 6. 信号控制
	
在`PYGEN`中实现缺省信号处理程序,处理信号SIGINT(2)和SIGTERM(15)。您可以在这个处理程序方法中做一些清理工作，这样您就可以很好地停止您的服务。

## 问题

1. 使用`Thrift` 多进程服务模式，生成的不能直接运行，因为`Thrift` 服务依赖`thrift` 接口生成的`gen-py`文件。

2. 在 `MacOS` 下直接运行 `<your_project_name>.sh stop` 有些问题，在下一个版本修复。
