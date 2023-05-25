# 使用官方 Python 镜像作为基础镜像
FROM python:3.11.2

# 设置工作目录
WORKDIR /particle

# 复制项目文件到容器中
COPY . /particle

# 安装依赖包
RUN pip install -r requirements.txt

# 启动 Django 服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:3001"]
