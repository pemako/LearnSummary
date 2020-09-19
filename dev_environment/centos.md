# The development environment

Vagrant + VirtualBox 虚拟机搭建过程

一、基础软件

1. 下载安装 VirtualBox 目前使用的是5.1.30版本
    - http://download.virtualbox.org/virtualbox/5.1.30/VirtualBox-5.1.30-118389-OSX.dmg

2. 下载安装 Vagrant 使用版本2.0.0
    - https://releases.hashicorp.com/vagrant/2.0.0/vagrant_2.0.0_x86_64.dmg

3. 下载Centos64-86_64 的 minimal 
    - https://github.com/2creatives/vagrant-centos/releases/download/v6.4.2/centos64-x86_64-20140116.box 

4. 自己打包的 box 下面的环境均已安装配置好
    - 链接:http://pan.baidu.com/s/1nuLhjDJ  密码:17ul

二、环境搭建

1. 添加 Box 镜像
    
- vagrant box add centos64 ~/vagrant/box/centos64-x86_64-20140116.box
- vagrant init centos64
- vagrant up
- vagrant ssh


2. 升级环境，必要如那件安装

- yum update -y
    - yum install vim
    - 设置.vimrc 文件

- 安装 python 多版多版本共存 pyenv
    - GitHub地址 https://github.com/pyenv/pyenv 
    - curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
    - pyenv install 2.7.14 & pyenv install 3.6.3
        - 中间可能会出现各种依赖没有安装只需 sudo yum install xxx -y 安装相应依赖即可
        - sudo yum install readline readline-devel readline-static openssl openssl-devel openssl-static sqlite-devel bzip2-devel bzip2-libs -y
        
- Java jdk9.0.1
    - http://www.oracle.com/technetwork/java/javase/downloads/index.html
    - 选择相应的版本下载

- Ruby 2.4.2 install

- PHP install
    - 源码安装参考 https://typecodes.com/web/centos7compilephp7.html
    - composer 安装 wget https://raw.githubusercontent.com/composer/getcomposer.org/1b137f8bf6db3e79a38a5bc45324414a6b1f9df2/web/installer -O - -q | php -- --quiet

- Mysql install
    - sudo yum install mysql mysql-server mysql-devel -y
    - sudo service mysqld start

- Nginx install
    1. 让 Nginx支持 rewrite
    - wget http://downloads.sourceforge.net/project/pcre/pcre/8.35/pcre-8.35.tar.gz && tar -zxvf pcre-8.5.tar.gz && cd pcre-8.5 && ./configure && make && sudo make install

    - wget http://nginx.org/download/nginx-1.12.2.tar.gz 
    - tar zxvf nginx-1.12.2.tar.gz && cd nginx-1.12.2
    - ./configure --prefix=/usr/local/nginx --with-http_stub_status_module --with-http_ssl_module --with-pcre=/usr/local/src/pcre-8.35

    - /usr/local/nginx/sbin/nginx -s {reload|reopen|stop} 重新载入配置，重启 停止

- Golang install


3. 打包 box
    
- vagrant package --base centos64 --output pemako_centos64_x86_64.box --vagrantfile FILE --include x,y,z
- --base NAME name 是需要打包的虚拟主机的名字
- --output NAME 输出要保存的文件名
- --vagrantfile 打包一个Vagrantfile到box中，这个Vagrantfile将作为box使用的Vagrantfile load
- --include x,y,z 附加一些文件到box中，这是让打包Vagrantfile执行附加任务 
