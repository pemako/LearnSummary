#### vagrant

#### 1. 下载box并安装

```
# 版本：Vagrant 2.1.1
https://www.vagrantup.com/
https://app.vagrantup.com/ubuntu/boxes/xenial64

# ubuntu版本 http://releases.ubuntu.com/xenial/
wget https://vagrantcloud.com/ubuntu/boxes/xenial64/versions/20180615.0.0/providers/virtualbox.box

vagrant box add ubuntu/xenial64 virtualbox.box
vagrant box list

vagrant init virtualbox.box
vagrant up
vagrant ssh
```

##### 配置Vagrantfile 需要注意 [重新定义日志输出位置](https://github.com/joelhandwell/ubuntu_vagrant_boxes/blob/master/u16/Vagrantfile#L11)
```
config.vm.provider "virtualbox" do |v|
    v.memory = 4096
    v.cpus = 4
    # Basebox ubuntu/xenial64 comes with following Vagrantfile config and causes https://github.com/joelhandwell/ubuntu_vagrant_boxes/issues/1
    # vb.customize [ "modifyvm", :id, "--uart1", "0x3F8", "4" ]
    # vb.customize [ "modifyvm", :id, "--uartmode1", "file", File.join(Dir.pwd, "ubuntu-xenial-16.04-cloudimg-console.log") ]
    # following config will address the issue
    v.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
  end
  
# 查看端口占用 sudo lsof -i -P | grep -i "listen"
# 查看vagrant的状态 vagrant global-status
```

#### 2. 配置及软件安装

```
# 更新所有软件
sudo locale-gen zh_CN.UTF-8  # 更新语言包
sudo apt-get update

# 设置vim
echo "set nu" >> .vimrc

sudo apt-get install ruby

# 安装设置php7.2  https://thishosting.rocks/install-php-on-ubuntu/
#1. sudo apt-get install python-software-properties
#2. sudo add-apt-repository ppa:ondrej/php
#3. sudo apt-get update

sudo apt-get -y install php7.2
apt-get install mcrypt php7.2-json php-pear php7.2-curl php7.2-dev php7.2-gd php7.2-mbstring php7.2-zip php7.2-mysql php7.2-xml php7.2-fpm

# 注意如果Apache启动需要先进行stop 
# sudo /etc/init.d/apache2 stop
sudo apt-get -y install nginx
sudo apt-get -y install mysql-server

# 安装开发依赖的相关库 
sudo apt-get install build-essential

# 访问vagrant中的Nginx 
https://blog.csdn.net/rlanffy/article/details/49385635

# 设置PHP

vim /etc/php/7.2/fpm/php.ini 将cgi.fix_pathinfo=1改为cgi.fix_pathinfo=0
vim /etc/php/7.2/fpm/pool.d/www.conf 找到listen = /run/php/php7.0-fpm.sock修改为listen = 127.0.0.1:9000

sudo service php7.0-fpm stop && sudo service php7.0-fpm start

vim /etc/nginx/sites-available/default 中将下面的注释开启
        // 开启这块注释，解析php文件
        location ~ \.php$ {
            include snippets/fastcgi-php.conf;
        
        #   # With php7.0-cgi alone:
        // 两种方式 : 1.监听 9000 端口, 2.sock 链接, 推荐使用 1
                fastcgi_pass 127.0.0.1:9000;
        #       # With php7.0-fpm:
        #       fastcgi_pass unix:/run/php/php7.0-fpm.sock;
        }

# 安装composer
curl -sS https://getcomposer.org/installer | php && sudo mv composer.phar /usr/local/bin/composer

# 安装golang
https://www.admfactory.com/how-to-install-golang-1-10-on-ubuntu/

https://blog.csdn.net/hehexiaoxia/article/details/69942931


# 安装java

sudo apt-get update

sudo apt-get install openjdk-8-jdk  # 安装openjdk-8-jdk
java -version 

# 命令行方式安装oracle Java JDK
sudo apt-get install python-software-properties # 安装依赖包
sudo add-apt-repository ppa:webupd8team/java    # 添加仓库源

sudo apt-get update
sudo apt-get install oracle-java8-installer     # 安装java JDK

sudo update-alternatives --config java          # 选择不同版本

# 更新vim
sudo apt-get install lua5.2 liblua5.2-dev
git clone https://github.com/vim/vim.git

wget http://luajit.org/download/LuaJIT-2.0.4.tar.gz
tar -xzvf LuaJIT-2.0.4.tar.gz
cd LuaJIT-2.0.4
make && sudo make install

cd vim
./configure --prefix=/data/vim74 --with-features=huge --with-luajit --enable-luainterp=yes


# 安装 LISP https://blog.csdn.net/yin__ren/article/details/79420983
sudo apt-get install clisp emacs slime
mkdir ~/.slime
sudo vim ~/.emacs # 把下面的内容写入

`
;;; Lisp (SLIME) interaction 
(setq inferior-lisp-program "clisp") 
(add-to-list 'load-path "~/.slime") 
(require 'slime) 
(slime-setup)  

(global-font-lock-mode t) 
(show-paren-mode 1) 
(add-hook 'lisp-mode-hook '(lambda () 
      (local-set-key (kbd "RET") 'newline-and-indent))) 
`

# 升级python
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install python3.6 
sudo apt-get install --reinstall libpython3.6-dev
```

#### 3.打包box

```
vagrant package --base centos64 --output pemako_centos64_x86_64.box --vagrantfile FILE --include x,y,z
--base NAME name 是需要打包的虚拟主机的名字
--output NAME 输出要保存的文件名
--vagrantfile 打包一个Vagrantfile到box中，这个Vagrantfile将作为box使用的Vagrantfile load
--include x,y,z 附加一些文件到box中，这是让打包Vagrantfile执行附加任务

# 生成的文件太大达到github的限制 pemako_centos64_x86_64.box 文件后续上传到云盘下载
```

#### 4. 大文件上传注意 [git-lfs](https://git-lfs.github.com/)

```
# 1. Download git-lfs

Homebrew: brew install git-lfs
MacPorts: port install git-lfs

# 2. Download and install the Git command line extension. You only have to set up Git LFS once.

git lfs install

# 3. Select the file types you'd like Git LFS to manage (or directly edit your .gitattributes). You can configure additional file extensions at anytime.

git lfs track "*.psd"

# Make sure .gitattributes is tracked
git add .gitattributes

# 4. There is no step three. Just commit and push to GitHub as you normally would.
git add file.psd
git commit -m "Add design file"
git push origin master

# 注意最大单个文件为 2147483648 字节
```
