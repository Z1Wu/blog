---
title: "Service-Computing-03"
date: 2018-10-04T18:52:33+08:00
draft: false
tags: ["Service-Computing","Golang", "pflag", "bufio"]
categories: ["Service-Computing"]
---

# 概述

这一次的实验是关于实现一个简单的命令行工具slepg, 关于这个工具的详细功能, 可以在这个[网页](
https://www.ibm.com/developerworks/cn/linux/shell/clutil/index.html
)中详细了解

由于本次实验的具体流程在上面的网站中已经给出了详细的C语言代码和伪代码，所以本次主要博客主要记录在用golang实现这个程序中出现的问题.

# pflag包相关

## pflag 初探
golang的标准库中提供了flag这个包，来为我们编写cli程序提供便利，但是本次的实验要求是要求我们的命令行程序的选项格式遵守
[Unix 命令行规范](http://www.gnu.org/software/libc/manual/html_node/Argument-Syntax.html)

所以考虑使用[pflag](https://github.com/ogier/pflag)

>pflag is a drop-in replacement for Go's flag package, implementing POSIX/GNU-style --flags.

> pflag is compatible with the GNU extensions to the POSIX recommendations for command-line options. For a more precise description, see the "Command-line flag syntax" section below.

> pflag is available under the same style of BSD license as the Go language, which can be found in the LICENSE file.

根据这个包作者的描述，这个包本身是符合相关的Unix命令函规范的，而且和flag包的用法差别不大, 而且如果你之前使用的是flag包的话，可以直接导入pflag 同时将名字改成flag，
如果你的选项都是通过flag提供的接口设置的，那么代码可以不改动。

```
import flag "github.com/ogier/pflag"
```

## 安装pflag

安装这个的过程和前面博客介绍的流程相同，直接使用

```
go get https://github.com/spf13/pflag
```

你就可以在go工作空间的pkg中看到相应的包，之后就可以在程序中直接`import`来使用了

{{< figure src="/images/service_computing/3/install_pflag.png" class="center" title="安装并导入pflag" >}}

## 定义相关的选项

根据题目的要求定义相关的选项

pflag 有两种定义flag/option的方式
- 不绑定选项和变量
```
// example,
var ip *int = flag.Int("flagname", 1234, "help message for flagname")
```
- 绑定选项和变量

```
// 吧flagname这个选项和变量flagvar绑定起来
flag.IntVar(&flagvar, "flagname", 1234, "help message for flagname")
```

## 问题

我们在写命令行工具的时候，会有这种情况， 就是有时两个选项不能同时出现，在这个包里面_似乎_没有直接提供相关的接口来实现这个功能，但是有提供默认为选项设置默认值这个选项，在一定条件下，设定一个非法输入作为默认选项，通过判断结果是否是错误的结果来判断用户是否有输入该选项，不过这样可能会导致返回的错误信息不是那么准确

```
pflag.IntVarP(&args.lineNumPerPage, "linenum", "l", specialNum, "specify the start page")
```

# io 相关

出于效率考虑本次的实验都是使用了bufio这个包来处理输入输出。

## bufio简介

bufio, 简单来讲就是包装io.Reader 和 io.Writer => 不是每次调用就使用一次读写，而是等整个缓冲区满了之后在进行一次读写，由于往下一级别的存储读写的代价比较高。所以使用buffer通常可以带来性能上的提升

## 部分接口展示

以下部分介绍这次实验中需要用到的接口
### buf.Reader

#### 简介
```go
//  buffer io 的内部实现， buf 就是用来暂时存储的缓冲区, rd是实际执行读取的部分，error记录出现的错误
type Reader struct {
	buf          []byte
	rd           io.Reader // reader provided by the client
	r, w         int       // buf read and write positions
	err          error
	lastByte     int
	lastRuneSize int
}
```

实验中用到的方法

- `bufio.NewReader(<io.Reader>)`: 接受一个io.Reader作为参数，创建一个有buffer的reader
    - 创建的buffer是默认大小的，要改变可以使用bufio.ReaderSize来改变
- `func (b *Reader) ReadString(delim byte) (string, error)`: 传入一个分隔符，每一次调用以string的形式返回

```go
// example
// input 是一个io.reader类型，创建一个bufio的reader
rd := bufio.NewReader(input) 
page, ferr := rd.ReadString('\f')
```


## 相关资料
- 相关的bufio的其他接口可以查看[官方文档]()
- 内部原理实现的解释[blog](https://medium.com/golangspec/introduction-to-bufio-package-in-golang-ad7d1877f762)
- 相关的源代码可以在[GitHub](https://github.com/golang/go/tree/1e3f563b145ad98d2a5fcd4809e25a6a0bc8f892/src/bufio)中看到

# 测试相关


## 测试前的准备(测试集)
这一次的程序对于输入的文件具有两种分页模式

1. 人为规定一个页的行数

2. 每次遇到ascii的控制字符'\f'(0x0c)作为一页

要测试我们的程序是否正确首先我们需要有相关的测试文件，以下是生成测试文件的方法**(主要是处理控制字符'\f'的插入问题)**

1. 使用程序随机生成正确编码的文件，记得在相应的地方插入'\f'字符，以便测试第二种方式

2. 使用vim文本编辑器可以直接在你想添加'\f'字符的，只需要在VIM的insert模式下,在你想要插入的地方按下`Control` +` L`即可，会显示一个` ^L`的字符就代表了需要的控制字符(分页) 

{{< figure src="/images/service_computing/3/add_page_break.png" class="center" title="使用VIM插入分页控制字符" >}}

## 测试过程

使用上一步生成的测试文件

- 测试第二种读取方式:
```shell
./selpg -s 1 -e 10 -f <test_file>
```

{{< figure src="/images/service_computing/3/test_f_type_reading.png" class="center"  >}}

- 测试重定向
由于这个 