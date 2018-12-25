---
title: "Service-Computing-02"
date: 2018-09-27T15:38:41+08:00
draft: false
tags: ["Service-Computing","Golang"]
categories: ["Service-Computing"]
---

# 概述
这次的实验是在虚拟机上搭建golang编程环境

# 1.Golang 初探

首先我们需要了解一下go 语言是什么

> 既然选择后台开发，自然建议你在 Linux 环境下安装 go 语言开发环境。这里仅是 centos 7 安装的部分内容。

# 2.实验流程

## 2.1实验环境

centos7 + virtualBox

## 2.2Golang 环境搭建

在centos7这个linux 发行版下搭建博客需要

### 2.2.1安装Golang

在centos上安装golang 有几个方式

#### 2.2.1.1 手动安装

可以从官网上下载对应平台(在centos对应的应该是amd64)的[发行文件](https://golang.org/dl/), 然后把这个解压到相应的路径之中。这样保证使用的最新版本的golang.

```shell
tar -C /usr/local -xzf go$VERSION.$OS-$ARCH.tar.gz
``` 

#### 2.2.1.2 使用包管理器

由于golang的有添加到centos的源中，所以我们可以使用 centos 默认的包管理器`yum`来下载这个包

```shell
# 从源下载 golang 文件
sudo yum install golang
# 查看安装文件的位置
# rpm => redhat package manager -q => query, -l list, 使用这个命令来查询已安装的包的位置
# | more => 把输出通过管道传入more程序中
rpm -ql golang |more

# 查看go版本验证安装
go version
```

这种安装比较简单方便会处理好所有的依赖关系，并安装到正确的地方。

#### 2.2.1.3 其他安装方法

在官网上还提到有其他的安装方法，比如从源文件编译等，由于水平有限就不在这里展开描述，详细教程看官网。

### 2.2.2 配置Golang环境

在安装完成之后，还不能直接使用Go, 如果你这个时候直接在bash里面输入go, 会收到命令不存在的报错，我们还需要一些其他的配置在来完成环境的安装

#### 2.2.2.1 创建工作空间

根据Go语言的要求，我们需要先为我们的源代码建立一个工作空间,实际上就是在特定的位置建立一个文件夹

```shell
mkdir $HOME/gowork  
```

#### 2.2.2.2 配置环境变量

在使用go之前需要为go设置相应的环境变量, 在centos中，如果使用的默认的终端(bash),可以在`.bashrc`中添加相应的环境变量EXPORT语句，也可以在`.bash_profile`里面修改，关于.bash_rc和`bash_profile`的区别: [详情点击](https://apple.stackexchange.com/questions/51036/what-is-the-difference-between-bash-profile-and-bashrc)

```shell
export GOPATH=$HOME/gowork
# 添加gowork中的bin文件到PATH中
export PATH=$PATH:$GOPATH/bin

```

设置完成之后可以通过, 输入一些简单的命令来查看是否生效

```shell
# 首先需要运行.bashrc/.bahs_profile，来让设置生效

source $HOME/.bashrc
# 检查是否配置成功
go env

```

如果配置成功的话应该可以看到相应的设置

![](/images/service_computing/second/env_var_setting_res.png)

#### 2.2.2.3 在vscode中配置go语言

vscode是微软的一款代码编辑器，编程效果拔群

> 如果你曾经是 Notepad++ 或 Sublime text 或 Atom 的用户，你不得不考虑改用微软 VSCode 做轻量级的编程。 它采用 JavaScript 技术，兼容几乎所有流行的操作系统，特别是对中文支持堪称完美！它不仅是跨平台多语言软件开发工具，而且是 Linux 平台写 Github Flavored Markdown 的神器。

centos 下的安装，直接戳[官网教程](https://code.visualstudio.com/docs/setup/linux)

创建一个简单的`hello_world.go`， 在创建完之后，vscode会提醒你下载extension(插件),来提供更好的支持。之间按照提示下载就行，插件的下载还是很顺利的
当时插件下载完之后，会提示你安装一些其他工具(analysing tools)，这个时候如果网络没有人工配置，就会出现以下错误:
![](/images/service_computing/second/gfw_error.png)

这个时候就需要一些奇技淫巧来解决，[详细原理](https://github.com/northbright/Notes/blob/master/Golang/china/get-golang-packages-on-golang-org-in-china.md)

具体的操作流程就是

- 下载源代码到本地
    - 这个部分的操作需要系统提前安装了git。

```shell

# optional：如果没有安装git，先安装git
sudo yum install git

# 创建文件夹
mkdir $GOPATH/src/golang.org/x/
# 下载源码, -d 下载之后不安装
go get -d github.com/golang/tools
# copy到相应的位置
cp $GOPATH/src/github.com/golang/tools $GOPATH/src/golang.org/x/ -rf
```

- 安装工具包

```shell

go install golang.org/x/tools/go/buildutil

```

上述操作完成之后就可以重新打开vscode根据就提示安装需要的tools.

**个人理解**：实际上在安装的vscode在提示的missing analsis tool,是指你的~/gowork/bin文件中没有存在vscode需要的可以用来分析代码的工具(包括golint, 
godocs之类的), 所有vscode使用的是 ` go get <import_path>` 命令来安装，从报错信息来看，它是到go的官方网站上去找了，然而官方网站被墙了，所以
返回错误，我们在上面的过程中，使用` go get <from_github> ` 从github下载，再把下载的源码移到import path里，这样的话，下次vscode调用`go get`
发现本地就有这个，就不会到远程去找了。

![](/images/service_computing/second/solved_gfw_error.png)

## 2.3运行第一个Go程序

经过上述的步骤之后就能够运行就能够运行相关的程序，在包所在的位置执行go install，进行编译包go源文件编译成相应的binary file，会自动把这个放到GOPATH/bin 文件中，之后就能直接在命令行使用了

![](/images/service_computing/second/compile_to_binary_file.png)

可以看到bin目录还有上一个步骤在vscode安装的分析工具

## 2.4 在vscode中调试GO程序

首先要保证提示的所有工具的安装好了

