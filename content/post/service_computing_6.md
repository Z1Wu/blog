---
title: "Service_computing_6"
date: 2018-12-20T12:58:43+08:00
draft: false
tags: ["Service-Computing","Docker"]

---

# ServiceComputing homework--Docker初探

本文主要关注如何在 window10 专业版下安装 dockers，和相关的配置以及简单的使用。

## 安装

### 从官网下载 docker

### 安装流程

1. 按照官网给的教程，在 win10 pro 的环境下，应该首先打开 `hyper-v`(注意：打开 `hyper-v` 之后，如果不添加其他设置的话，android studio 中的虚拟机是无法打开的，原因暂时不太明白【猜测可能是和虚拟化方式的改变有关】)



2. 按照下载得到的 installer 的指示，完成安装即可。【没有截图。。。】 


## 配置

### 处理 docker pull 的问题

由于docker默认的源是在国外的，使用docker下载源上的 image 在默认情况下是无法完成的，一般会出现的错误都是访问超时，这种情况下有两种解决方法：

#### 把默认的源设置成国内的镜像

本次实验没有按照尝试这个方法，可以自行配置。

``` shell

$ docker pull registry.docker-cn.com/myname/myrepo:mytag

```

#### 设置代理

由于当前环境使用的ss进行代理，所以考虑设置为 dockers 客户端设置代理，目前使用的Windows，直接在dockers设置中就可以设置代理。

![](/images/service_computing/6/setup_proxy.png)

### 搭建前端镜像

这个是本次作业的一部分，顺便可以当成一个练习，实践一下，作业的要求是把上一次作业【swapi】的 web 应用容器化。

没能完全理解在本次作业在前端 docker 的在实际中如何发挥作用，出于练习和作业要求的目的，按照流程把 前端的镜像先搭建起来。

#### 创建 Dockerfile

根据官网教程的指示，首先应该使用 `dockerfile` 来创建一个镜像，由于本次实验是第一次接触 `vue`，不太熟悉，考虑这应该属于常见的应用场景，上`vue`官网应该能够搜索相关的 `dockerfile` 作为 starter，果然我们可以在[官方教程](https://vuejs.org/v2/cookbook/dockerize-vuejs-app.html#ad)中看到

``` shell

# 以下是从官网拉下来的例子

FROM node:9.11.1-alpine

# install simple http server for serving static content
RUN npm install -g http-server

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]

```

可以看到大致的流程，通过 `FROM` 基于一个另外一个镜像(image)进行开发，之后就是通过 node 搭建这个项目的过程。

需要注意的是这里使用到了 `COPY` 命令，把本地的文件移入到容器中，而且使用的是相对路径的写法，所以我们需要把这个 `Dcokerfile` 放在我们项目的根目录下。

#### 通过 Dockerfile 创建镜像

在根目录下输入以下命令，其中 -t 指代的是的这个镜像的名字，最后面的 `.`，指代的是对应的创建镜像的上下文`(contxext)`, 关于这个上下文对创建镜像的影响，可以参考[这里](https://yeasy.gitbooks.io/docker_practice/content/image/build.html)

``` shell 

docker build -t docker build -t my-swapi-vue:v1 .

```

如果网络环境良好的话，在这一步，应该就完成了构建。不过一般情况下，是完成不了的。报出的错误应该是 `npm request timeout` 之类的错误，查看 `Dockerfile` 可以发现，首先是 `From` 命令，由于我们已经在上面配置好了客户端的代理，这里应该是可以顺利完成的，但是之后又 `npm run install`，这个应该就是问题的所在，官网提供的 `node` 镜像，里面配置的源应该还是外国的源，而在我们构建镜像的时候，流量是不会通过我们 host 机的 shadowsocks 代理的，所以这个 install 应该是不会成功的。


发现问题之后我们可以通过修改 `Dockerfile` 来避开这个问题。

``` shell
FROM node:9.11.1-alpine

# install simple http server for serving static content
RUN npm install -g cnpm --registry=https://registry.npm.taobao.org && cnpm install -g http-server

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
# RUN npm install

RUN cnpm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]
```

可以看到主要的改动在于，修改了 `npm` 的源，以及之后的包安装操作都使用了`cnpm`。


#### 运行容器

``` shell

docker run -it -p 8080:8080 --rm --name dockerize-vuejs-app-1 my-swapi-vue:v1

```

由于上面是开发环境，构建了一个简单的 server, 而且是监听容器的 8080 端口，同时在 Dockefile 里面也指代了容器暴露的端口 `expose`，所以我们在运行的时候 -p 把 `host` 上的端口和容器的端口对应起来。

另外还需要注意的是

- -it => 指代的是 --interactive 和 --terminal 也就是保持容器的终端，让我们能和容器进行交互。

- --name => 指代的应该是容器的名字。

- --rm => 防止命名冲突，删除已经存在的同名container 

- 最后的应该是指定容器从哪一个镜像中启动。

## 参考

vue 教程：https://vuejs.org/v2/cookbook/dockerize-vuejs-app.html#ad

docker 官方文档：https://docs.docker.com/

docker-pratice：https://yeasy.gitbooks.io/docker_practice/content/

docker-china-mirror：https://www.docker-cn.com/registry-mirror
