# oneword-web

## 开发

1. 安装 pipenv

```shell
brew install pipenv
# brew upgrade pipenv  # 升级
```

2. 初始化应用和启动

```shell
cd work  # 切换到工具目录
git clone git@github.com:lessc/oneword_web.git
cd oneword_web

pipenv install
pipenv shell

bin/start
```

3. 访问页面

```shell
http://127.0.0.1:5000/
http://127.0.0.1:5000/apidocs
```

## 资源

- [pipenv使用指南](https://crazygit.wiseturtles.com/2018/01/08/pipenv-tour/)
- [Flask文档](https://flask.palletsprojects.com/en/1.1.x/)
- [Swagger编写示例](https://github.com/flasgger/flasgger#using-docstrings-as-specification)