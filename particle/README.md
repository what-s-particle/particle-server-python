Run `/scripts/generate.sh` to generate the `.py` files corresponding to the protocol.

# Django写的Particle后端

```
├── config
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py

```

这些目录和文件的用处是：

- /config/__init__.py：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。如果你是 Python
  初学者，阅读官方文档中的 [更多关于包的知识](https://docs.python.org/3/tutorial/modules.html#tut-packages)。
- /config/settings.py：Django
  项目的配置文件。如果你想知道这个文件是如何工作的，请查看 [Django 配置](https://docs.djangoproject.com/zh-hans/3.1/topics/settings/)
  了解细节。
- /config/urls.py：Django 项目的 URL
  声明，就像你网站的“目录”。阅读 [URL调度器](https://docs.djangoproject.com/zh-hans/3.1/topics/http/urls/) 文档来获取更多关于
  URL 的内容。
- /config/asgi.py：作为你的项目的运行在 ASGI 兼容的 Web
  服务器上的入口。阅读  [如何使用ASGI 来部署](https://docs.djangoproject.com/zh-hans/3.1/howto/deployment/asgi/) 了解更多细节。
- /config/wsgi.py：作为你的项目的运行在 WSGI
  兼容的Web服务器上的入口。阅读 [如何使用 WSGI 进行部署](https://docs.djangoproject.com/zh-hans/3.1/howto/deployment/wsgi/)
  了解更多细节
- manage.py: 一个让你用各种方式管理 Django
  项目的命令行工具。你可以阅读 [django-admin 和 manage.py](https://docs.djangoproject.com/zh-hans/3.1/ref/django-admin/)
  获取所有 manage.py 的细节。

## 创建 moments 应用

### 项目 VS 应用

项目和应用有什么区别？
应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者小型的投票程序。
项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用。

```
python manage.py startapp moments

python manage.py migrate

python manage.py makemigrations moments

python manage.py migrate

```

- 编辑 models.py 文件，改变模型。
- 运行 python manage.py makemigrations 为模型的改变生成迁移文件。
- 运行 python manage.py migrate 来应用数据库迁移。

### 创建一个管理员账号

```
python manage.py createsuperuser
```

### Django REST 框架

https://blog.51cto.com/yuzhou1su/5357677

```
pip install djangorestframework
```

protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/addressbook.proto

protoc -I=. --python_out=. ./addressbook.proto

### unit test

```
python -m pip install pytest
```
