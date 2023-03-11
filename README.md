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
- /config/__init__.py：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。如果你是 Python 初学者，阅读官方文档中的 [更多关于包的知识](https://docs.python.org/3/tutorial/modules.html#tut-packages)。
- /config/settings.py：Django 项目的配置文件。如果你想知道这个文件是如何工作的，请查看 [Django 配置](https://docs.djangoproject.com/zh-hans/3.1/topics/settings/) 了解细节。
- /config/urls.py：Django 项目的 URL 声明，就像你网站的“目录”。阅读 [URL调度器](https://docs.djangoproject.com/zh-hans/3.1/topics/http/urls/) 文档来获取更多关于 URL 的内容。
- /config/asgi.py：作为你的项目的运行在 ASGI 兼容的 Web 服务器上的入口。阅读  [如何使用ASGI 来部署](https://docs.djangoproject.com/zh-hans/3.1/howto/deployment/asgi/) 了解更多细节。
- /config/wsgi.py：作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。阅读 [如何使用 WSGI 进行部署](https://docs.djangoproject.com/zh-hans/3.1/howto/deployment/wsgi/) 了解更多细节
- manage.py: 一个让你用各种方式管理 Django 项目的命令行工具。你可以阅读 [django-admin 和 manage.py](https://docs.djangoproject.com/zh-hans/3.1/ref/django-admin/) 获取所有 manage.py 的细节。
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

### Chat about navigation design with GPT

Q: What is the essential difference between graph structure and tree structure?
A: Graph and tree structures are both commonly used in computer science and data structures. While they share some similarities, there are also some key differences between them.

A graph is a collection of vertices (also called nodes) and edges, where an edge is a connection between two vertices. Edges can be directed or undirected and can have weights (costs or distances). Graphs can be used to model relationships between entities, such as social networks, transportation networks, or computer networks. Graphs can be cyclic, meaning that it is possible to follow a path from a vertex back to itself.

A tree, on the other hand, is a type of graph where each node has exactly one parent, except for the root node which has no parent. Trees are used to represent hierarchical structures, such as file systems, organization charts, and family trees. Trees are always acyclic, meaning there are no cycles in the graph.

The key difference between graph and tree structures is that trees have a hierarchical structure with a single root node and a specific parent-child relationship between nodes, while graphs do not necessarily have a specific hierarchy or parent-child relationship between nodes. Additionally, trees are always acyclic, while graphs can be either cyclic or acyclic.



Q: So if I want to design a navigation between mobile pages, which structure should I use?
A: If you are designing a navigation between mobile pages, a tree structure would be a suitable choice. This is because mobile app navigation typically follows a hierarchical structure, where each screen is accessed through a series of parent-child relationships.

For example, consider the navigation of a typical e-commerce app: a user might start on a home screen, then navigate to a product category screen, then to a specific product screen, and finally to a shopping cart screen. This navigation follows a hierarchical structure, where each screen has a single parent (the screen that was accessed immediately before it) and multiple children (the screens that can be accessed directly from it).

Using a tree structure to represent the navigation between mobile pages allows you to easily visualize the hierarchy of the screens and the relationships between them. You can use a tree structure to organize your app's screens, with the home screen at the root of the tree and each subsequent screen represented as a child node. This can help you ensure that your app's navigation is intuitive and easy to use for your users.



Q: Not all pages have only one parent node. The navigation design of jetpack compose and swft UI looks more like a graph structure.
A: You are correct that not all mobile app screens have a single parent node, and some app navigations may require a more complex graph structure rather than a simple tree structure.

Jetpack Compose and SwiftUI are both examples of UI frameworks that use a graph structure to represent mobile app navigation. In these frameworks, screens are represented as nodes in a graph, with edges representing the possible navigational paths between them. This allows for more complex app navigations, where screens can have multiple parents and can be accessed through multiple paths.

A graph structure can be a good choice for more complex mobile app navigations, where screens can be accessed through multiple paths or where the app's structure is not hierarchical. However, it is important to ensure that the navigation remains intuitive and easy to use for your users, even with a more complex graph structure. You may want to consider using visual cues, such as color coding or icons, to help users understand the relationships between screens and to make it clear which navigational paths are available to them.





