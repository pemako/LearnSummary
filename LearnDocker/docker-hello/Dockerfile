# Dockerfile

# 使用Python运行时作为基础镜像
FROM python:3.7-slim

# 设置/app 为工作路径
WORKDIR /app

# 将当期目录所有内容复制到容器的 /app目录下
ADD . /app

# 安装 requirements.txt 中指定的包
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# 对容器外开放80端口
EXPOSE 80

# 定义环境变量
ENV NAME World

# 当容器启动时运行 app.py 
CMD ["python", "app.py"]
