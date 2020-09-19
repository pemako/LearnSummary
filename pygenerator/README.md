# Pemako Python Project Generator

[![GitHub stable](https://img.shields.io/badge/pygenerator-stable1.0.1-green.svg)](https://github.com/pemako/pygenerator/archive/v1.0.1.zip)

[中文目录](README_zh.md)

Script and project templates to generate some useful service model automatically.

## Depend

- Your must install `rename`,`git`, `python`,`sed`,`gsed`

## Quik Start
Use `pygen.sh` to create your own py project.

## What PYGEN Does
#### 1. Project Directory Tree
	
A new generated project's directory tree is like this:
		
    <your_project_name>
    |-bin
    |	\-<your_project_name>.sh --- script to start/stop/restart service
    |-conf
    |	|-<your_project_name>_logging.cfg --- main logging config file
    |	|-<your_project_name>_service.cfg --- service default config file
    |	\-<your_project_name>_worker_logging.cfg --- worker logging config file
    |-lib --- the same as "src", which you can put all your own source code in
    |	|-<your_project_name>.py --- config, logging and serivce import
    |	\-<your_project_name>_service.py --- implements your own functions
    \-build.sh --- build the project into rpm package

#### 2. Control Script
	
As you can see in the "bin" directory, there is a "<your_project_name>.sh" script file. You can use it like 
	
	<your_project_name>.sh [-d EXECUTION_PATH] {start|stop|restart|status}
			
It actually use "lib/<your_project_name>.py" to run your service.

#### 3. Release Script

There is a build.sh in project's root directory. Just run it and you will have your project as 

	target/<your_project_name>-0.0.1-1.x86_64.rpm
	target/<your_project_name>-0.0.1.tar.gz"
	
The tar package is for you to test offline. And the rpm package is to deploy online(If your project is under the puppet management).
	
#### 4. Logging Config
	
PYGEN implements logging with the standard module "logging". And all the main config and worker config is in "conf/".
	
The default log rotation is to rotate(cut) log hourly, as you can see in 
	
	log/hourly/<your_project_name>.log
	
If you are using the Multiprocess of Multiprocess Thrift mode, there is no need for you to worry about "Logging into single file from multi-process". The generated framework just deal with it for you. There is only one thread in main process that is logging to file while other processes just send their log records through socket to this thread. So there is ONLY one thread who will rotate the log file.
	
#### 5. Service Config
	
PYGEN implements config loading with "ConfigParser". You can find out the default config file as
	
	conf/<your_project_name>_service.cfg

Here you can set your worker number, your main logger port(to receive log record from other processes), your service port, database you use, etc.
	
#### 6. Signal Handler
	
The default signal handler implemented in PYGEN handle the signal SIGINT(2) and SIGTERM(15). You can do some clean-up thing in this handler method so that you can stop your service elegantly.

## Issues

1. Multiprocess Thrift service model can not run immediately after generating because it's an Thrift server which needs processor to be implemented with your own '.thrift' interface and 'gen-py'.

2. When you use `<your_project_name>.sh stop` on MacOS has some problems will fix it next version.
