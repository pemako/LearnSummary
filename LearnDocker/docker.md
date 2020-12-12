# Docker学习

> 所有的命令记录基于`Docker`的一下版本

```
➜  ~ docker version
Client: Docker Engine - Community
 Version:           19.03.8
 API version:       1.40
 Go version:        go1.12.17
 Git commit:        afacb8b
 Built:             Wed Mar 11 01:21:11 2020
 OS/Arch:           darwin/amd64
 Experimental:      true

Server: Docker Engine - Community
 Engine:
  Version:          19.03.8
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.12.17
  Git commit:       afacb8b
  Built:            Wed Mar 11 01:29:16 2020
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          v1.2.13
  GitCommit:        7ad184331fa3e55e52b890ea95e65ba581ae3429
 runc:
  Version:          1.0.0-rc10
  GitCommit:        dc9208a3303feef5b3839f4323d9beb36df0a9dd
 docker-init:
  Version:          0.18.0
  GitCommit:        fec3683
 Kubernetes:
  Version:          Unknown
  StackAPI:         Unknown
```

## 1. Docker 命令

- `docker pull [选项] [Docker Registry 地址[:端口号]/]仓库名[:标签]` 拉取镜像
    - 拉取镜像的默认地址是 `Docker Hub`
    - 仓库名: `<用户名>/<软件名>` 对于`Docker Hub`如果不给出用户名，默认为`libray`也就是官方镜像

- `docker run -it --rm ubuntu:18.04 bash`
    - `-it`
        - `-i` 交互式操作
        - `-t` 是终端
    - `--rm` 这个参数是说容器退出后随之删除
    - `ubuntu:18.04` 指使用 `ubuntu:18.04`镜像为基础启动容器
    - `bash` 放到镜像名后的是命令，这里我们希望有个交互式的`Shell`,这里用的是`bash`
	- ` docker run --name webserver -d -p 80:80 nginx`
		- `--name webesrver` 指定启动镜像的名称
		- `nginx` 使用NGINX镜像启动一个容器 
		- `-p 80:80` 并且映射了 `80:80`端口
		- `-d` 后台启动并打印容器ID

- `docker images` 默认累出所有镜像
	
	```
 	-a, --all             Show all images (default hides intermediate images)
      	--digests         Show digests
  	-f, --filter filter   Filter output based on conditions provided
        --format string   Pretty-print images using a Go template
        --no-trunc        Don't truncate output
  	-q, --quiet           Only show numeric IDs
	```
	- `docker images --format "{{.ID}} {{.Respository}}" 只列出镜像ID和仓库名
	- `docker images --format "table {{.ID}}\t{{.Repository}}\t{{.Tag}}"`
		- 以表格显示，自定义列
	- `docker images -q` 仅列出镜像ID的值

- `docker image`
	```
	- build       Build an image from a Dockerfile
	- history     Show the history of an image
	- import      Import the contents from a tarball to create a filesystem image
	- inspect     Display detailed information on one or more images
	- load        Load an image from a tar archive or STDIN
	- ls          List images
	- prune       Remove unused images
	- pull        Pull an image or a repository from a registry
	- push        Push an image or a repository to a registry
	- rm          Remove one or more images
	- save        Save one or more images to a tar archive (streamed to STDOUT by default)
	- tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
	```
	
	- `docker image ls -f since=pemako/hello`
		- 列出在`pemako/hello`之后建立的镜像	
	- `docker image rm $(docker image ls -q pemako/hello)`
		- `docker image ls -q pemako/hello` 仅列出镜像`pemako/hello`的`ID`
		- `docker image rm` 删除累出的镜像`id`

- `docker system [df|events|info|prune]`
	- `df` 查看镜像，容器，数据卷所占用的空间
	- `events` 从服务器获取实时事件
	- `info` 显示系统相关信息
	- `prune` 删除无用的数据


## 2. `Dockefile`定制镜像

> `Dockerfile`是一个文本文件，其中包含了一系列的指令，每一条指令构建一层，因此每一调指令的内容，就是描述该层应当如何构建。

- [Dockfile最佳实践文档](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Dockfile官方文档](https://docs.docker.com/engine/reference/builder/)
- [Docker 官方镜像 Dockerfile](https://github.com/docker-library/docs)

### 2.1 编写Dockerfile文件

```Dockerfile
FROM nginx
RUN echo '<h1>Hello,Docker!</h1> /usr/share/nginx/html/idex.html
```

- FROM 指定基础镜像
	- 该值必须孩子定，并且必须是第一个指令
	- `FROM scratch` scratch是一个特殊的镜像，该镜像是虚拟的概念，并不实际存在，表示一个空白的镜像

- RUN 执行命令 有两种格式
	- `shell`格式
		- `RUN <命令>`
	- `exec`格式
		- `RUN ["可执行文件", "参数1", "参数2"]`

- COPY 复制文件
    - `COPY [--chown=<user>:<group>] <源路径>... <目标路径>`  命令行模式
    - `COPY [--chown=<user>:<group>] [<源路径1>, ... <目标路径>]` 函数调用方式

- ADD 复制文件在COPY基础上增加了一些功能
    > 尽可能的使用`COPY` 因为`COPY`的语音很明确，就是复制文件。最适合使用`ADD`的场合就是需要自动解压缩的场合。
    > 下面的场景非常适合使用ADD

    ```
    FROM scratch
    ADD ubuntu-xenial-core-clouding-amd64-root.tar.gz /
    ```

- CMD 容器启动命令
    > 在指令格式行，一般推荐`exec`格式，这类格式在解析时会被解析为`JSON`数组，因此一定更要使用双引号`""` 而不要使用单引号.
    > 如果使用shell 格式话的话，实际的命令会被包装为 `sh -c` 的参数的形式进行执行。 `CMD echo $HOME`在实际执行中会将其变
    > 更为 `CMD ["sh", "-c", "echo $HOME"]`

    - shell 格式: `CMD <命令>`
    - exec 格式: `CMD ["可执行文件", "参数1", "参数2" ...]`

- ENTRYPOINT 入口点
    > ENTRYPOINT的目录和CMD 一样，都是在指定容器启动程序及参数。

- ENV 设置环境变量
    - ENV <key> <value>
    - ENV <key1>=<value1> <key2>=<value2>...

    > 下列指令可以支持环境变量的展开 `ADD` `COPY` `ENV` `EXPOSE` `FROM` `LABEL` `USER` `WORKDIR` `VOLUME` `STOPSIGNAL` `ONBUILD`
    > `RUN`

- `ARG` 固件参数
    - ARG <参数名>[=<默认值>]
    
    > 构建参数和ENV 的效果一样，都是设置环境变量。所不同的是，ARG设置的构建环境的环境变量，在将来容器运行时是不会存在这些环境变量
    > 的。

- `VOLUME` 定义匿名卷
    - VOLUME ["<路径1>", "<路径2>"...]
    - VOLUME <路径>

- EXPOSE 声明端口
    > 要将 EXPOSE 和在运行时使用 -p <宿主端口>:<容器端口> 区分开来。-p 是映射宿主端口和容器端口。而EXPOSE 仅仅是声明容器单算使用什
    > 么端口而已，并不会自动在宿主进行端口映射。

- WORKDIR 指定工作目录

- USER 指定当前用户

- HEALTHCHECK 健康检查

- ONBUILD 

### 2.2 构建镜像

- docker build -t nginx:v3

#### 2.2.1 构建进行的几种方式

- `docker build https://github.com/twang2218/gitlab-ce-zh.git#11.1`
	- 直接用`git repo`进行构建
	- 默认指定`master`分支，构建目录为 `/11.1` ，然后`Docker`就会自己去`git clone`这个项目，切换到指定分支，并进入指定目录后开始构建
- `docker build http://server/context.tar.gz`
	- 如果给出的`URL`是一`tar`压缩包,那么`Docker`引擎会下载这个包，并自动解压缩，以其作为上下文，开始构建
- `docker build - < Dockerfile `  or `cat Dockerfile | docker build -`
	- 从标准输入中读取`Dockerfile`进行构建
- `docker build - < context.tar.gz`
	- 从标准输入中读取上下文压缩包进行构建
	- 如果标准输入为压缩包格式，将会使其为上下文压缩包，直接将其展开，将里面视为上下文，并开始构建

### 2.3 构建多种系统架构支持的Docker镜像

> docker manifest 命令

- 创建mainfest 列表
    - `docker manifest create username/test username/x8664-test username/arm64v8-test`
- 设置mainfest 列表
    - `docker manifest annotate username/test username/x8664-test --os linux --arch x86_64`
    - `docker manifest annotate username/test username/x8664-test --os linux --arch arm64 --variant v8`
- 查看mainfest 列表
    - `docker manifest inspect username/test`

- 推送mainfest 设置
    - `docker manifest push username/test`

