# 自动登陆脚本

### 基本信息 

- 环境要求 Bash >= 4.0 
- 目前版本为 v1.0.0 MacOS 没有问题


### 配置

根据自己的实际需求进行配置 `.config` 文件中的 `_server_config` 数据有以下4种使用方式。

- 1.直接登录到机器A,不执行相应命令

```
_server_config['A']="host user passwd port"
```

- 2.直接登录到机器B,且执行相应命令

`no` 为固定值，如`command`命令是 `ls -l`,则登录机器后执行 `ls -l` 命令

```
_server_config['B']="host user passwd port no 'command'"
```

- 3.通过机器A登录到机器C,不执行相应命令

这种情况是针对，目标机器有限定，只能从指定机器登陆时使用。

```
_server_config['C']="host user passwd port A"
```

- 4.通过机器A登录到机器C,执行相应命令
```
_server_config['C']="host user passwd port A 'command'"
```

#### 使用

- 1.clone code 修改成你需要的名字如 `to`,`fly`,`gg` ...
 
    `git clone https://github.com/pemako/to.git && cd to && mv to.sh youwish`

- 2.按照上面的配置进行相关脚本的配置，并在 `to` 中引入正确的配置

- 3.使用命令 `to key[配置的关键字]` 进行登录


### 示例

![demo.gif](demo.gif)

