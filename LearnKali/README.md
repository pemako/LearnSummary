# Kali 使用基本知识

## 电脑基本信息

- brew 环境信息

```
HOMEBREW_VERSION: 1.7.7
ORIGIN: https://github.com/Homebrew/brew
HEAD: c54a657cd5987cba2718f7012a55101324fde8b1
Last commit: 5 days ago
Core tap ORIGIN: https://github.com/Homebrew/homebrew-core
Core tap HEAD: 6ada89e003411006ee467eb764cc32f96aa3c924
Core tap last commit: 33 hours ago
HOMEBREW_PREFIX: /usr/local
CPU: quad-core 64-bit haswell
Homebrew Ruby: 2.3.7 => /System/Library/Frameworks/Ruby.framework/Versions/2.3/usr/bin/ruby
Clang: 10.0 build 1000
Git: 2.19.1 => /usr/local/bin/git
Curl: 7.54.0 => /usr/bin/curl
Java: 11
macOS: 10.14-x86_64
CLT: 10.0.0.0.1.1535735448
Xcode: 10.0
virtualbox: 5.2.18,124319
```

- 电脑信息

```
- uanme -a
Darwin mako 18.0.0 Darwin Kernel Version 18.0.0: Wed Aug 22 20:13:40 PDT 2018; root:xnu-4903.201.2~1/RELEASE_X86_64 x86_64

- sw_vers
ProductName:	Mac OS X
ProductVersion:	10.14
BuildVersion:	18A391
```

## 安装设置

[参照](https://study.163.com/course/courseMain.htm?courseId=1005094023) 课程进行kali的第一次全面设置主要包括下面内容

### 安装

![安装示例图](./imgs/kali-install-demo.gif)

- copy文件完成按照相应的提示进行操作安装即可


### 设置

- kali安装完成设置账号和密码 root/root
- 虚拟机增强工具安装 使用kali 官方推荐 open-vm-tools
    - apt update && apt -y full-upgrade
    - apt -y install open-vm-tools-desktop fuse
- 设置宿主机/虚拟机之间的复制粘贴
- 桌面环境设置
    - gnome-tweaks
    - gnome 扩展插件  https://extensions.gnome.org/  
    	- Netspeed
    	- OpenWeather
    - 中文输入法
    	- apt install ibus ibus-pinyin
    	- im-config
    	- reboot
    	- ibus-setup
    	- 区域和语言-添加输入法
   	- Conky 安装
   		- apt install conky-all conky-manager
   		- 下载配置文件（自己调整，自带的样式比较丑故自己下载）
   			- git clone https://github.com/zenzire/conkyrc.git ~/.conky
   			- ln -s ~/.conky/conkyrc ~/.conkyrc
   		- 使用conky-manager 打开管理设置是否开机启动及选择的样式
   		- 设置相应的城市编码
   			- https://weather.yahoo.com 找到对应的城市编码
   			- 把对应的城市编码在 .conkyrc 文件中替换默认城市的
   			- Conky-manager 会自动运行查找设定的城市编码
- 软件管理
	- Kali 衍生与Debian,并集成了APT包管理器
	- 安装软件前毕运行命令 apt update && apt full-upgrade
	- 查看软件源（强烈建议只使用官方软件仓库，除非有必要不要使用任何第三方软件仓库）
		- cat /etc/apt/source.list
		- 安装过程出现问题逐一屏幕提示信息
	- 库安装 apt install package_name
	- 安装DEB安装包
		- dekg -i name.deb  
		- apt install ./name.deb （如果可以安装不要使用上面的安装方式）

	- 字体安装 （安装window下的字体文件）
		- 微软字体 apt install ttf-mscorefonts-installer
		- 文泉译微米黑  apt install fonts-wqy-microhei
	- 安装常用工具 apt install mtr whois gcc git curl -y
	- 安装全部安全工具 apt install kali-linux-all
	- 翻译软件
		- apt install goldendict
		- 打开goldendict 进行设置有道查询搜索（后面不需要打开软件快速按两次 Control + C 进行快速翻译）
		- youdao http://dict.youado.com/search?q=%GDWORD%&ue=utf8
		- 增加开机启动
	- 办公软件
		- apt install libreoffice (体积比较大界面较丑，不推荐安装)
		- 推荐安装 Onlyoffice Desktop 的桌面软件
			- https://www.onlyoffice.com/download-desktop.aspx
			- apt install ./onlyoffice_destopeditors_amd64.deb 文件
	- 安装JAVA
		- add-apt-repository ppa:webupd8team/java
		- 修改 /etc/apt/source.list 文件添加下面两行文件
			- deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main
			- deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise main
			- apt update && apt full-upgrade
				- 注意如果出现问题按照提示解决（按照遇到文件如下）
				- W: GPG error: http://ppa.launchpad.net/webupd8team/java/ubuntu trusty InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY C2518248EEA14886
				- 解决办法采用 apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886
		- apt install java-common oracle-java8-installer
		- apt install oracle-java8-set-default

- Wireshark 每次启动时报错
	- gedit /usr/share/wireshark/init.lua
	- 注释倒数第二行文件 -- dofile(DATE_DIR.. "console.lua")
	- 某些情况需要把倒数第三行第四行也注释掉

- 设置虚拟机和宿主机文件共享和粘贴拷贝
	- 安装增强包工具
		- 安装好kali后，登录，然后在VirtualBox的菜单中选择 ”设备“-> ”安装增强功能“；此时kali桌面上回挂在一个光盘图标，这张光盘被自动加载到了文档。在弹出窗口选择run进行操作
		- cp /media/cdrom/VBoxLinuxAdditions.run ~/
		- ~/VBoxLinuxAdditions.run 
	- 为虚拟机设置共享文件夹
		- 选择 ”设备“->”共享目录“ 打开后进行设置即可
		- 勾选上 Auto-mount (自动挂载)和Make Permanent (永久有效)
	- 设置粘贴拷贝
		- 选择 ”设备“->”剪贴板“->”双向绑定“  （Devices->Shared Clipboard -> Bidirectional）
		- 选择 ”设备“->”托拽“-> “双向绑定” （Devices->Drag and Drop -> Bidirectional）

# 备注信息

- kali linux 下载
	- 百度网盘 链接:https://pan.baidu.com/s/1D_r2ECbhJyGDlWlyFUeT8w  密码:myd9
	- 官网下载对应版本 https://www.kali.org/downloads/
- VirtualBox 安装方法
	- `brew cask install virtualbox`
	- 官网下载对应版本 https://www.virtualbox.org/wiki/Downloads
- 第一次快照
	- 20181114 包含上面所有内容

