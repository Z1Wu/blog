---
title: "Service-Computing-01"
date: 2018-09-13T12:18:35+08:00
draft: false
tags: ["Service-Computing","Private Cloud"]
categories: ["Service-Computing"]
---

# 任务概述

搭建自己使用的私有桌面云

- 初步了解虚拟化技术，理解云计算的相关概念
- 为后续课程提供统一的编程与实验环境
- 理解系统工程师面临的困境

# 实验流程

本次的实验报告主要是来记录相关的本次任务中比较重要也比较麻烦的一个部分: 使用虚拟机平台搭建自己的私有云。

##  安装虚拟机软件

要搭建一个私有的云桌面，首先需要选择一个虚拟机创建平台，在目前有主要有两个选择(超链接是对应的下载连接):
- vmware player(免费版) / vmware workstation(专业版需要付费)  []
- oracle virtual box (开源软件) []  
使用上述两个平台都可以完成本次实验，处于演示目的，本文将会使用 `virutal box` 作为虚拟机平台。

以下是安装虚拟机的过程
### 下载virtual box安装包
在官网根据自己的计算机的相应情况，下载对应的安装器，本人是使用win10, 所以下面的教程都在winows环境下进行
![download from the offical website](/images/1.png)
### 在电脑上安装virtual box 
按照上一步下载得到的是一个exe，直接点开之后一直下一步就行，安装完按照提示重新启动一下

## 配置virtual box
### (optional)打开处理器虚拟化
如果是第一次使用虚拟机软件，可能会需要打开处理器的虚拟化功能，一种打开处理器虚拟化功能的方法通过在blos界面(可通过重新开机进入)打开，
详细的操作流程可以通过百度
### 配置默认的虚拟安装位置
在未设置的情况下，virtual box的默认安装位置都会是在vritual box安装目录下的文件中，由于处于速度考虑大部分人可能会把virtual box安装在SSD上，而这个可能是系统盘，按照默认的设置，在创建虚拟机的时候可能会占用系统盘太多空间。所以可以把安装位置改一下。
![](/images/test_gif.gif)
### 配置虚拟机内部虚拟网络
// 以下描述都是从网上的操作步骤是网上的教程的内容，本人对其中原理不是很懂
在安装虚拟机之前我们要先置好虚拟机的网卡，可以用来实现虚拟机与虚拟机之间和以及虚拟机和主机之间的连接。
配置的具体流程如下

1. 管理-》主机网络管理器-》创建虚拟网卡 (可以看到现在里面有两张网卡)
2. 修改虚拟网卡的地址，给这个新建的的网卡一个地址: 192.168.100.1/24
3. 最后在DHCP一栏点击启用

![](/images/network_setting.png)

### 检验配置的网络
在windows的终端(cmd, powershell 都可以)，输入ipconfig就可以看到这个网卡
![](/images/network_validation.png)

## 安装虚拟机
### 虚拟机镜像选择
根据课程要求，需要64bit的linux系统，在各种发行版中都要挺多可以选择的

- centos: 如果是选择centos，如果你不需要桌面，选择minimal版本即可，如果需要桌面，则下载完整版的

- ubuntu: 下载服务器版，

处于国内特殊环境的考虑，直接从官网上下载的速度，不是理想，可以改用从阿里云的源上下载[OSX](https://opsx.alibaba.com/mirror)
### 创建虚拟机
点击新建虚拟机
按照流程配置虚拟机的相关参数。在创建的时候只有内存和硬盘大小，在创建之后，就可以修改其他设置

![](/images/create_vm_2.png)
- CPU设置: 建议 1 -> 2
- 内存设置: 不低于2g
- 存储: 以后难以拓展，预先分配30g
- 网络: 
    - 第一块网卡需要设置为NAT
    - 第二块网卡设计host noly, 也就是在上一步设置的网卡
- 显示：如果有设置显卡的话，建议设置较高的显存

按照上述的步骤和要求设置完相关的配置之后，虚拟机的配置大致如下
![](/images/create_vm_final.png)
### 安装虚拟机

1. 双击左边栏的刚刚创建的虚拟机，就可以进行虚拟机的安装
2. 安装开始之前会出现提示，要求选择启动盘，实际上就是选择刚才下载的镜像，
![install](/images/install_vm1.png)
3. 选择语言(有条件可以选择英语，否则之后建立的文件都是中文命名，难以操作)
![install](/images/install_vm2.png)
4. 之后就是建立用户，设置root密码，等待安装结束
![install](/images/install_vm3.png)

### 配置虚拟机
1. 使用centos的包管理器yum，获取wget
    - yum: 类似与ubuntu下的apt，用于获取软件和以及安装软件(包括依赖处理等)和软件管理的包管理器
    - wget: web get，支持http和ftp协议从web上获取内容。(需要使用这个用于下一步软件源的更改)
2. 配置yum的包源: yum远程下载包的默认源是在国外速度不如在国内(...),所以把包的源改成国内的，比如[aliyun](https://opsx.alibaba.com/mirror)或者[163](http://mirrors.163.com/.help/centos.html))的源
    - 在aliyun或者163的网站上都有修改的详细教程.
3. 使用yum update 升级os内核( 需要下载之后再安装，需要消耗一定时间，而且安装需要重新启动)
4. 重启之后配置网络相关的内容
    - 使用nmtui，配置相关的网络设置，包括主机名和第二块网卡地址()
5. 通过ping，来验证网络设置是否正确
    - 在虚拟机内ping <主机的ip地址>
    - 在主机上ping <虚拟机的ip地址>

### 虚拟机上安装软件
在虚拟机上安装可以使用yum install <package_name> 直接从之前设置的源下载相应的软件
tips: 如果不知道相应的包的名字则可以使用 `yum whatprovides <keyword>` 查看了包含输入关键词的包

### 建立私有云
当上述的基本设置都完成之后就可以设立一个私有云，既然是云，一般都有多台虚拟机。
经过上面的步骤建立了之后，我们可以通过VirtualBox提供的虚拟机复制来创建多台和上面配置好的虚拟机相同的虚拟机
需要注意的是，再复制的时候需要选择重新初始化网卡的mac.
VirtualBox有两种复制方式链接复制和完全复制，根据VB(VirualBox)文档的描述

>完全复制(Full clone)：

>由原始虚拟机完全复制到新的虚拟机, 需要完整足够的硬盘空间, 新的虚拟机可以在没有原始虚拟机的状况下独立运行。

>链接复制(Linked clone)：

>是以原始虚拟机为基础, 快速复制成新的虚拟机, 但较完全复制节省空间, 只是新的虚拟机运行时需要原始虚拟机存在.
在这里使用连接复制即可

### 使用ssh连接
在上一步ping通之后就可以使用在宿主机(host)上连接。
在windows上，如果安装了git, 在携带的git bash中已经提供了ssh工具用于连接。
直接` ssh username@ip_address `
然后输入密码就可以连接。  

### 使用远程桌面服务
windows 用户可以使用 rdp(remote desktop protocol)提供远程桌面服务
1. 首先需要为VB安装相应拓展包

2. 为centos安装桌面( 由于上面提到使用的minial的iso, 所以需要手动安装桌面组件)

```shell
## 安装桌面环境
yum groupinstall "GNOME Desktop"

## 设置图形化组件为启动目标
ln -sf /lib/systemd/system/runlevel5.target /etc/systemd/system/default.target

## 重新启动就可以看到效果
shutdown -r now
```

3. 之后由于虚拟机使用的是centos，需要下载Xrdp，以及配置相关的文件，来使用远程桌面服务。

```shell
# 以下内容来自 https://siskonemilia.github.io/Service-Computing/Service-Computing-01-Private-Cloud-Service/
# 由于yum的包仓库没有Xrdp的包, 需要配置EPEL源，
yum install -y epel-release-latest.noarch
# 安装Xrdp相关组件
yum install xrdp tigervnc-server 
# 启动xrdp 服务，并设置开机启动，实际上是监听(listen)相应端口的rdp连接
systemctl start xrdp
systemctl enable xrdp
# 使用netstat查看端口的使用情况, 验证是否开启成功, 默认是使用3389来监听
netstat -antup | grep xrdp
# 调整防火墙设置
firewall-cmd --permanent --add-port=3389/tcp
firewall-cmd --reload
chcon --type=bin_t /usr/sbin/xrdp
chcon --type=bin_t /usr/sbin/xrdp-sesman
```

4. 之后就可以使用windows自带的rdc(remote desktop connection)，连接远程桌面
输入对应的虚拟机地址和端口号，以及用于登陆的用户名( centos 的用户)，即可完成连接
![](/images/rdc_win.png)