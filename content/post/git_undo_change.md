---
title: "Git_undo_change"
date: 2018-11-22T15:51:51+08:00
draft: true
---

# git 版本回退相关

在实践中通常有这样的场景

> 在一个分支开发到一定程度之后，突然有新想法，但是又不想直接抛弃到目前开发的内容，一般的考虑是把当前的进度 `stash` 下来，然后重新开一条 `branch` 再进行开发。

> [关于如何stash](./git_stash.md)


在上述场景中，一个问题就是，我们新开的分支并不想要以当前的 `commit` 作为分支点。而是想要回退到几个`commit`之前，再进行分支。所以这篇博客主要在于记录几种 `undo change` 的方法。


## git checkout

首先使用`git log` 查看 `commit history`, 每个commit都有对应的`sha1-hash`值作为标识号。找到想要回退的commit。使用`git checkout`到达对应的commit，这个时候`git HEAD`会指向我们checkout 的commmit，工作目录也会被替换成这个commit下的所有文件，值得注意的是，在这种情况下，仓库进入`detach head`状态，也就是HEAD不在任何一条分支，在这个状态下，我们可以对这个工作目录进行任意的修改，修改之后进行的commit，不会被归入任何一条分支，称为`orphan commit`，之后会被自动删除。所以如果需要重新开始的话，需要在这个地方重新新建一条分支，新建的分支会以当前的`commit`作为分支点。也就达到了我们的目的。具体操作如下。 

``` bash
# 查看当前分支的commit历史
git log 
# 返回到对应的commit，进入detach-head状态
git checkout {SHA1-HASH}
# 以这个commit为分叉点，新建一条分支。
git checkout -b {new_branch_name}

```

 

## git revert




## git 

## 参考

大部分内容来自 [bucket tutorial]，似乎没有找到中文翻译版本。
